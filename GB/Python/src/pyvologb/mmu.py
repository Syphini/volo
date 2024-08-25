import os
import pygame
from pyvologb.helpers import formatted_hex
from pyvologb.cartridge import Cartridge
from pyvologb.ppu import PPU


class MMU:
    def __init__(
        self, cartridge: Cartridge, use_boot_rom: bool = False, debug: bool = False
    ) -> None:

        self.BOOT_ROM = "/lib/bootrom.bin"
        self.CARTRIDGE = cartridge
        self.CURRENT_BANK = 0
        self.USE_BOOT_ROM = use_boot_rom

        self.DEBUG = debug

        io = IO(self, self.DEBUG)

        # ROM Memory is cartridge memory, and is therefore readonly unless there's an MBC chip
        self.ROM1 = bytearray(0x4000)  # 0000 -> 3FFF
        self.ROM2 = bytearray(0x4000)  # 4000 -> 7FFF

        # This memory is GB internal
        self.VRAM = bytearray(0x2000)  # 8000 -> 9FFF
        self.ERAM = bytearray(0x2000)  # A000 -> BFFF
        self.WRAM = bytearray(0x2000)  # C000 -> DFFF
        self.ECHO = bytearray(0x1E00)  # E000 -> FDFF
        self.OAM = bytearray(0xA0)  # FE00 -> FE9F
        self.EMPTY = bytearray(0x60)  # FEA0 -> FEFF
        self.IO = io  # FF00 -> FF7F
        self.HRAM = bytearray(0x7F)  # FF80 -> FFFE

        self.IME = False
        self.HALT = False

        self.switch_rom_bank(0)

        if self.USE_BOOT_ROM and self.IO.BANK == 0:
            with open(
                os.path.dirname(os.path.abspath(__file__)) + self.BOOT_ROM, "rb"
            ) as f:
                self.ROM1[0:0x100] = f.read()

        self.switch_rom_bank(1)

        # print(self.CARTRIDGE.HEADER.title)

    def switch_rom_bank(self, bank: int) -> None:
        match bank:
            case 0:
                bank_data = self.CARTRIDGE.MEMORY_BANKS[0].copy()
                self.ROM1 = bank_data
            case _:
                self.CURRENT_BANK = bank
                bank_data = self.CARTRIDGE.MEMORY_BANKS[bank].copy()
                self.ROM2 = bank_data

    def switch_ram_bank(self, bank: int) -> None:
        pass

    def get_memory(self, address: int) -> int:
        match address:
            case addr if 0x0000 <= addr <= 0x3FFF:
                return self.ROM1[address]
            case addr if 0x4000 <= addr <= 0x7FFF:
                return self.ROM2[address - 0x4000]
            case addr if 0x8000 <= addr <= 0x9FFF:
                return self.VRAM[address - 0x8000]
            case addr if 0xA000 <= addr <= 0xBFFF:
                return self.ERAM[address - 0xA000]
            case addr if 0xC000 <= addr <= 0xDFFF:
                return self.WRAM[address - 0xC000]
            case addr if 0xE000 <= addr <= 0xFDFF:
                return self.ECHO[address - 0xE000]
            case addr if 0xFE00 <= addr <= 0xFE9F:
                return self.OAM[address - 0xFE00]
            case addr if 0xFEA0 <= addr <= 0xFEFF:
                return 0x00
            case addr if 0xFF00 <= addr <= 0xFF7F:
                return self.IO.get(address)
            case addr if 0xFF80 <= addr <= 0xFFFE:
                return self.HRAM[address - 0xFF80]
            case 0xFFFF:
                return self.IO.IE.get()
            case _:
                raise Exception("Inaccessible Memory:", formatted_hex(address))

    def set_memory(self, address: int, value: int) -> None:
        match address:
            case addr if 0x0000 <= addr <= 0x1FFF:
                self.CARTRIDGE.toggle_ram_enable(value)
            case addr if 0x2000 <= addr <= 0x3FFF:
                self.switch_rom_bank((value & 0x1F) & (self.CARTRIDGE.MBC_COUNT - 1))
            case addr if 0x4000 <= addr <= 0x5FFF:
                print("TODO RAM Bank Number")
                pass
            case addr if 0x6000 <= addr <= 0x7FFF:
                print("TODO Banking Mode Select")
                pass
            case addr if 0x8000 <= addr <= 0x9FFF:
                self.VRAM[address - 0x8000] = value
            case addr if 0xA000 <= addr <= 0xBFFF:
                self.ERAM[address - 0xA000] = value
            case addr if 0xC000 <= addr <= 0xDFFF:
                self.WRAM[address - 0xC000] = value
            case addr if 0xE000 <= addr <= 0xFDFF:
                self.ECHO[address - 0xE000] = value
            case addr if 0xFE00 <= addr <= 0xFE9F:
                self.OAM[address - 0xFE00] = value
            case addr if 0xFEA0 <= addr <= 0xFEFF:
                pass  # ignore memory here??
            case addr if 0xFF00 <= addr <= 0xFF7F:
                self.IO.set(address, value)
            case addr if 0xFF80 <= addr <= 0xFFFE:
                self.HRAM[address - 0xFF80] = value
            case 0xFFFF:
                self.IO.IE.set(value)
            case _:
                raise Exception("Inaccessible Memory:", formatted_hex(address))

    def dump(self) -> None:
        # Hex Dump
        with open(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "logs/mem_dump.log"
            ),
            "w",
        ) as f:
            dump = bytearray.hex(
                self.ROM1
                + self.ROM2
                + self.VRAM
                + self.ERAM
                + self.WRAM
                + self.ECHO
                + self.OAM
                + self.EMPTY
                + self.IO.dump()
                + self.HRAM
                + bytearray([self.IO.IE.get()]),
                " ",
            ).upper()
            n = 48
            data = [
                f"{formatted_hex(i//3)} -- {dump[i:i+n]
                                             }"
                for i in range(0, len(dump), n)
            ]
            f.write("\n".join(data))


class IO:
    def __init__(self, mmu: MMU, debug: bool = False) -> None:

        self.MMU = mmu

        self.JOYP = Joypad(self)  # FF00
        self.SERIAL = Serial(debug)  # FF01 -> FF02
        self._TIMER = Timer(self)  # FF04 -> FF07
        self.IF = Interrupts(0xE1, upper_bits=True)  # FF0F

        self.AUDIO = Audio()

        self.WAVE = bytearray(0x10)  # FF30 -> FF3F
        self.LCD = PPU(mmu, debug)  # FF40 -> FF4B
        # ???
        self.BANK = (not mmu.USE_BOOT_ROM) & 1  # FF50
        self.IE = Interrupts()  # FFFF

    def get(self, address: int) -> int:
        match address:
            case 0xFF00:
                return self.JOYP.get()
            case 0xFF01:
                print(self.SERIAL.get_serial())
                return self.SERIAL.SB
            case 0xFF02:
                return self.SERIAL.SC
            case addr if 0xFF04 <= addr <= 0xFF07:
                return self._TIMER.get(addr)
            case 0xFF0F:
                return self.IF.get()
            case addr if 0xFF10 <= addr <= 0xFF26:
                return self.AUDIO.get(addr)
            case addr if 0xFF30 <= addr <= 0xFF3F:
                return self.WAVE[address - 0xFF30]
            case addr if 0xFF40 <= addr <= 0xFF4B:
                return self.LCD.get(addr)
            case _:
                print(f"Ignoring IO Address GET: {formatted_hex(address)}")
                return 0xFF

    def set(self, address: int, value: int) -> None:
        match address:
            case 0xFF00:
                self.JOYP.set(value)
            case 0xFF01:
                self.SERIAL.SB = value
            case 0xFF02:
                self.SERIAL.SC = value
            case addr if 0xFF04 <= addr <= 0xFF07:
                self._TIMER.set(addr, value)
            case 0xFF0F:
                self.IF.set(value)
            case addr if 0xFF10 <= addr <= 0xFF26:
                self.AUDIO.set(addr, value)
            case addr if 0xFF30 <= addr <= 0xFF3F:
                self.WAVE[address - 0xFF30] = value
            case addr if 0xFF40 <= addr <= 0xFF4B:
                self.LCD.set(addr, value)
            case 0xFF50:
                self.BANK = value
                if self.BANK != 0:
                    self.MMU.switch_rom_bank(0)
            case _:
                print(
                    f"Ignoring IO Address SET: {formatted_hex(address)} {formatted_hex(value)}"
                )

    def tick(self, cycles: int) -> None:
        self._TIMER.tick(cycles)
        self.LCD.tick(cycles)
        self.AUDIO.tick(cycles)

    def dump(self) -> bytearray:
        data = bytearray(
            [
                self.JOYP.get(),
                self.SERIAL.SB,
                self.SERIAL.SC,
                0x00,
                self._TIMER.DIV,
                self._TIMER.TIMA,
                self._TIMER.TMA,
                self._TIMER.TAC,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                self.IF.get(),
            ]
        )
        data.extend(self.AUDIO.dump())
        data.extend(bytearray(0x09))
        data.extend(self.WAVE)
        data.extend(self.LCD.dump())
        data.extend(bytearray(0x4))
        data.extend(bytearray([self.BANK]))
        data.extend(bytearray(0x2F))

        return data


class Timer:
    def __init__(self, IO: IO) -> None:

        self.IO = IO

        self._DIVIDER = 0xAB00  # 16 bit register

        # DIV - FF04

        self.TIMA = 0x00  # FF05
        self.TMA = 0x00  # FF06

        self._TAC_ENABLE = 0
        self._TAC_CLOCK_SELECT = 0

        self.TAC = 0xF8  # FF07

        self.CLOCK = 0

    @property
    def TAC(self) -> int:
        return 0xF << 4 | 1 << 3 | self._TAC_ENABLE << 2 | self._TAC_CLOCK_SELECT

    @TAC.setter
    def TAC(self, value: int) -> None:
        self._TAC_ENABLE = value >> 2
        self._TAC_CLOCK_SELECT = value & 0x3
        self.reset_clock()

    @property
    def DIV(self) -> int:
        return self._DIVIDER >> 8

    @DIV.setter
    def DIV(self, _: int) -> None:
        self._DIVIDER = 0x0

    def get(self, address: int) -> int:
        match address:
            case 0xFF04:
                return self.DIV
            case 0xFF05:
                return self.TIMA
            case 0xFF06:
                return self.TMA
            case 0xFF07:
                return self.TAC
        return 0xFF

    def set(self, address: int, value: int) -> None:
        match address:
            case 0xFF04:
                self.DIV = 0x0
            case 0xFF05:
                self.TIMA = value
            case 0xFF06:
                self.TMA = value
            case 0xFF07:
                self.TAC = value

    def reset_clock(self) -> None:
        match self._TAC_CLOCK_SELECT:
            case 0:
                self.CLOCK = 1024
            case 1:
                self.CLOCK = 16
            case 2:
                self.CLOCK = 64
            case 3:
                self.CLOCK = 256

    def tick(self, cycles: int) -> None:
        for _ in range(cycles):
            self._DIVIDER = (self._DIVIDER + 1) & 0xFFFF

            if self._TAC_ENABLE == 1:
                self.CLOCK -= 1

                if self.CLOCK <= 0:
                    self.reset_clock()
                    calc = self.TIMA + 1
                    if calc > 0xFF:
                        self.IO.IF.TIMER = 1
                        self.TIMA = self.TMA
                        self.IO.IF.TIMER = 1
                    else:
                        self.TIMA = calc


class Interrupts:
    def __init__(self, value: int = 0x00, upper_bits: bool = False) -> None:
        self.set(value)
        self.UPPER_F = upper_bits

    def set(self, value: int) -> None:
        self.JOYPAD = value >> 4 & 1
        self.SERIAL = value >> 3 & 1
        self.TIMER = value >> 2 & 1
        self.LCD = value >> 1 & 1
        self.VBLANK = value & 1

    def get(self) -> int:
        return (
            (7 << 5 if self.UPPER_F else 0)
            | self.JOYPAD << 4
            | self.SERIAL << 3
            | self.TIMER << 2
            | self.LCD << 1
            | self.VBLANK
        )


class Joypad:
    # 0xCF -> 11001111
    # 0 is True, 1 is False
    def __init__(self, IO: IO) -> None:

        self.IO = IO

        self.USE_SELECT = False
        self.USE_DPAD = False

        self.reset_keys()

    def reset_keys(self) -> None:
        # SsBA
        self.START = False
        self.SELECT = False
        self.B = False
        self.A = False

        # DPAD
        self.DOWN = False
        self.UP = False
        self.LEFT = False
        self.RIGHT = False

    def get(self) -> int:
        final = 0xF
        if self.USE_SELECT:
            final = (
                (not (self.START) & 1) << 3
                | (not (self.SELECT) & 1) << 2
                | (not (self.B) & 1) << 1
                | (not (self.A) & 1)
            )
        if self.USE_DPAD:
            final = (
                (not (self.DOWN) & 1) << 3
                | (not (self.UP) & 1) << 2
                | (not (self.LEFT) & 1) << 1
                | (not (self.RIGHT) & 1)
            )

        return (
            7 << 5
            | (not (self.USE_SELECT) & 1) << 5
            | (not (self.USE_DPAD) & 1) << 4
            | final
        )

    def set(self, value: int) -> None:
        self.USE_SELECT = not (value >> 5 & 1)
        self.USE_DPAD = not (value >> 4 & 1)

    def set_keys(self, scancode: int, value: bool) -> None:
        match scancode:
            case pygame.KSCAN_DOWN:
                self.DOWN = value
            case pygame.KSCAN_UP:
                self.UP = value
            case pygame.KSCAN_LEFT:
                self.LEFT = value
            case pygame.KSCAN_RIGHT:
                self.RIGHT = value
            case pygame.KSCAN_RETURN:
                self.START = value
            case pygame.KSCAN_LSHIFT:
                self.SELECT = value
            case pygame.KSCAN_A:
                self.B = value
            case pygame.KSCAN_S:
                self.A = value

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            self.set_keys(event.scancode, True)
            self.IO.IF.JOYPAD = 1
        if event.type == pygame.KEYUP:
            self.set_keys(event.scancode, False)


class Serial:
    def __init__(self, debug: bool = False) -> None:
        self.DEBUG = debug

        self.BUFFER: list[int] = []
        self.BUFFER_LAST = 0

        self.SB = 0x00  # FF01
        self.SC = 0x7E  # FF02

    def get_serial(self) -> str:
        ret = "".join([chr(x) for x in self.BUFFER])
        if not self.DEBUG:
            self.BUFFER.clear()
        return ret

    @property
    def SB(self) -> int:
        return self.BUFFER_LAST

    @SB.setter
    def SB(self, value: int) -> None:
        self.BUFFER.append(value)
        self.BUFFER_LAST = value

        if self.DEBUG:
            print("SERIAL:\n", self.get_serial())

    @property
    def SC(self) -> int:
        return self.ENABLE << 7 | 0x1F << 2 | self.SPEED << 1 | self.SELECT

    @SC.setter
    def SC(self, value: int) -> None:
        self.ENABLE = value >> 7 & 1
        self.SPEED = value >> 1 & 1
        self.SELECT = value & 1


class Audio:
    def __init__(self) -> None:

        self.PULSE_CHANNEL = self.Pulse()

        self.NR10 = 0x80  # FF10
        self.NR11 = 0xBF  # FF11
        self.NR12 = 0xF3  # FF12
        self.NR13 = 0xFF  # FF13
        self.NR14 = 0xBF  # FF14

        self.NR21 = 0x3F  # FF16
        self.NR22 = 0x00  # FF17
        self.NR23 = 0xFF  # FF18
        self.NR24 = 0xBF  # FF19

        self.NR30 = 0x7F  # FF1A
        self.NR31 = 0xFF  # FF1B
        self.NR32 = 0x9F  # FF1C
        self.NR33 = 0xFF  # FF1D
        self.NR34 = 0xBF  # FF1E

        self.NR41 = 0xFF  # FF20
        self.NR42 = 0x00  # FF21
        self.NR43 = 0x00  # FF22
        self.NR44 = 0xBF  # FF23

        self.NR50 = 0x77  # FF24
        self.NR51 = 0xF3  # FF25
        self.NR52 = 0xF1  # FF26

    def get(self, addr: int) -> int:
        match addr:
            case 0xFF16:
                return self.PULSE_CHANNEL.get(1)
            case 0xFF17:
                return self.PULSE_CHANNEL.get(2)
            case 0xFF18:
                return self.PULSE_CHANNEL.get(3)
            case 0xFF19:
                return self.PULSE_CHANNEL.get(4)
            case _:
                print("Audio register not implemented", formatted_hex(addr))
                return 0xFF

    def set(self, addr: int, value: int) -> None:
        match addr:
            case 0xFF16:
                self.PULSE_CHANNEL.set(1, value)
            case 0xFF17:
                self.PULSE_CHANNEL.set(2, value)
            case 0xFF18:
                self.PULSE_CHANNEL.set(3, value)
            case 0xFF19:
                self.PULSE_CHANNEL.set(4, value)
            case _:
                print(
                    "Audio register not implemented",
                    formatted_hex(addr),
                    formatted_hex(value),
                )

    def tick(self, cycles: int) -> None:
        pass

    def dump(self) -> bytearray:
        return bytearray(23)

    class Pulse:
        def __init__(self) -> None:
            self.PERIOD_TIMER = 0
            self.LENGTH_TIMER = 64

            self.WAVEFORMS = [
                [0, 0, 0, 0, 0, 0, 0, 1],  # Low 7 High 1 - 12.5%
                [0, 0, 0, 0, 0, 0, 1, 1],  # Low 6 High 2 - 25%
                [0, 0, 0, 0, 1, 1, 1, 1],  # Low 4 High 4 - 50%
                [1, 1, 1, 1, 1, 1, 0, 0],  # High 6 Low 2 - 75%
            ]

            self.WAVE_DUTY = 0
            self.LENGTH_INIT = 0
            self.VOL_INIT = 0
            self.ENV_DIR = 0  # 0 decrease, 1 increase
            self.PERIOD = 0  # 11bit
            self.LENGTH_ENABLE = 0

        def get(self, register: int) -> int:
            match register:
                case 1:
                    return self.WAVE_DUTY << 6
                case 2:
                    return self.VOL_INIT << 4 | self.ENV_DIR << 3 | (self.PERIOD >> 8)
                case 3:
                    return 0  # write only
                case 4:
                    return self.LENGTH_ENABLE << 6

        def set(self, register: int, value: int) -> None:
            match register:
                case 1:
                    self.WAVE_DUTY = value >> 6 & 0x3
                    self.LENGTH_INIT = value & 0x3F
                case 2:
                    self.VOL_INIT = value >> 3 & 0xF
                    self.ENV_DIR = value >> 2 & 1
                case 3:
                    self.PERIOD = (self.PERIOD & 0x700) | (value & 0xFF)
                case 4:
                    if value & 0x80:
                        self.trigger()
                    self.LENGTH_ENABLE = value >> 6 & 1
                    self.PERIOD = value & 0x7 << 8 | self.PERIOD & 0xFF

        def trigger(self) -> None:
            pass
