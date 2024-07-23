import helpers
from ppu import PPU


class Registers:
    def __init__(self, mmu):

        self.mmu = mmu

        self.A = 0x01
        self.B = 0x00
        self.C = 0x13
        self.D = 0x00
        self.E = 0xD8
        self.H = 0x01
        self.L = 0x4D

        self.PC = 0x0  # Boot ROM is 0x0; Cartridge is 0x100
        self.SP = 0xFFFE

        self.ZERO = 1
        self.SUBTRACTION = 0
        self.HALFCARRY = 1
        self.CARRY = 1

    @property
    def F(self):
        return (
            self.ZERO << 7
            | self.SUBTRACTION << 6
            | self.HALFCARRY << 5
            | self.CARRY << 4
        )

    @property
    def AF(self):
        return self.A << 8 | self.F

    @AF.setter
    def AF(self, value: int):
        self.A = value >> 8
        self.ZERO = value >> 7 & 1
        self.SUBTRACTION = value >> 6 & 1
        self.HALFCARRY = value >> 5 & 1
        self.CARRY = value >> 4 & 1

    @property
    def BC(self):
        return self.B << 8 | self.C

    @BC.setter
    def BC(self, value: int):
        self.B = value >> 8
        self.C = value & 0xFF

    @property
    def DE(self):
        return self.D << 8 | self.E

    @DE.setter
    def DE(self, value: int):
        self.D = value >> 8
        self.E = value & 0xFF

    @property
    def HL(self):
        return self.H << 8 | self.L

    @HL.setter
    def HL(self, value: int):
        self.H = value >> 8
        self.L = value & 0xFF

    def PUSH(self, value: int):
        self.SP = helpers.wrap_16bit(self.SP - 1)
        self.mmu.set_memory(self.SP, value >> 8)

        self.SP = helpers.wrap_16bit(self.SP - 1)
        self.mmu.set_memory(self.SP, value & 0xFF)

    def POP(self):
        lower = self.mmu.get_memory(self.SP)
        self.SP = helpers.wrap_16bit(self.SP + 1)

        higher = self.mmu.get_memory(self.SP)
        self.SP = helpers.wrap_16bit(self.SP + 1)

        return higher << 8 | lower

    def INCREMENT_PC(self, value: int):
        self.PC += value

    def debug(self):
        data = {
            "A": self.A,
            "B": self.B,
            "C": self.C,
            "D": self.D,
            "E": self.E,
            "F": self.ZERO << 7
            | self.SUBTRACTION << 6
            | self.HALFCARRY << 5
            | self.CARRY << 4,
            "H": self.H,
            "L": self.L,
            "PC": self.PC,
            "SP": self.SP,
        }
        print([{c: helpers.formatted_hex(data[c])} for c in data])
        print(
            {
                "Z": self.ZERO,
                "N": self.SUBTRACTION,
                "H": self.HALFCARRY,
                "C": self.CARRY,
            }
        )


class IO:
    def __init__(self, mmu):
        self.JOYP = Joypad()  # FF00
        self.SB = 0x00  # FF01
        self.SC = 0x73  # FF02
        self._TIMER = Timer(self)  # FF04 -> FF07
        self.IF = Interrupts(0xE1)  # FF0F
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
        self.WAVE = bytearray(0x10)  # FF30 -> FF3F
        self.LCD = PPU(mmu)  # FF40 -> FF4B
        # ???
        self.IE = Interrupts()  # FFFF

    def get(self, address):
        match address:
            case 0xFF00:
                return self.JOYP.get()
            case addr if 0xFF01 <= addr <= 0xFF02:
                print("TODO handle serial", helpers.formatted_hex(address))
                return 0xFF
            case addr if 0xFF04 <= addr <= 0xFF07:
                return self._TIMER.get(addr)
            case 0xFF0F:
                return self.IF.get()
            case addr if 0xFF10 <= addr <= 0xFF26:
                print("TODO handle audio registers", helpers.formatted_hex(address))
                return 0xFF
            case addr if 0xFF30 <= addr <= 0xFF3F:
                return self.WAVE[address - 0xFF30]
            case addr if 0xFF40 <= addr <= 0xFF4B:
                return self.LCD.get(addr)
            case _:
                print(f"Ignoring IO Address GET: {helpers.formatted_hex(address)}")
                return 0xFF

    def set(self, address, value):
        match address:
            case 0xFF00:
                self.JOYP.set(value)
            case addr if 0xFF01 <= addr <= 0xFF02:
                print("TODO handle serial", helpers.formatted_hex(address))
            case addr if 0xFF04 <= addr <= 0xFF07:
                self._TIMER.set(addr, value)
            case 0xFF0F:
                self.IF.set(value)
            case addr if 0xFF10 <= addr <= 0xFF26:
                print("TODO handle audio registers", helpers.formatted_hex(address))
            case addr if 0xFF30 <= addr <= 0xFF3F:
                self.WAVE[address - 0xFF30] = value
            case addr if 0xFF40 <= addr <= 0xFF4B:
                self.LCD.set(addr, value)
            case _:
                print(
                    f"Ignoring IO Address SET: {helpers.formatted_hex(address)} {helpers.formatted_hex(value)}"
                )

    def dump(self):
        data = bytearray(
            [
                self.JOYP.get(),
                self.SB,
                self.SC,
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
        data.extend(
            bytearray(
                [
                    self.NR10,
                    self.NR11,
                    self.NR12,
                    self.NR13,
                    self.NR14,
                    0x00,
                    self.NR21,
                    self.NR22,
                    self.NR23,
                    self.NR24,
                    self.NR30,
                    self.NR31,
                    self.NR32,
                    self.NR33,
                    self.NR34,
                    0x00,
                    self.NR41,
                    self.NR42,
                    self.NR43,
                    self.NR44,
                    self.NR50,
                    self.NR51,
                    self.NR52,
                    0x00,
                    0x00,
                    0x00,
                    0x00,
                    0x00,
                    0x00,
                    0x00,
                    0x00,
                    0x00,
                ]
            )
        )

        data.extend(self.WAVE)
        data.extend(self.LCD.dump())
        data.extend(bytearray(0x34))

        return data


class Timer:
    def __init__(self, IO: IO):

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
    def TAC(self):
        return 0xF << 4 | 1 << 3 | self._TAC_ENABLE << 2 | self._TAC_CLOCK_SELECT

    @TAC.setter
    def TAC(self, value):
        self._TAC_ENABLE = value >> 2
        self._TAC_CLOCK_SELECT = value & 0x3
        self.reset_clock()

    @property
    def DIV(self):
        return self._DIVIDER >> 8

    @DIV.setter
    def DIV(self, _):
        self._DIVIDER = 0x0

    def get(self, address):
        match address:
            case 0xFF04:
                return self.DIV
            case 0xFF05:
                return self.TIMA
            case 0xFF06:
                return self.TMA
            case 0xFF07:
                return self.TAC

    def set(self, address, value):
        match address:
            case 0xFF04:
                self.DIV = 0x0
            case 0xFF05:
                self.TIMA = value
            case 0xFF06:
                self.TMA = value
            case 0xFF07:
                self.TAC = value

    def reset_clock(self):
        match self._TAC_CLOCK_SELECT:
            case 0:
                self.CLOCK = 1024
            case 1:
                self.CLOCK = 16
            case 2:
                self.CLOCK = 64
            case 3:
                self.CLOCK = 256

    def tick(self, cycles):
        for _ in range(cycles):
            self._DIVIDER = helpers.wrap_16bit(self._DIVIDER + 1)

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
    def __init__(self, value=0x00):
        self.set(value)

    def set(self, value):
        self.JOYPAD = value >> 4 & 1
        self.SERIAL = value >> 3 & 1
        self.TIMER = value >> 2 & 1
        self.LCD = value >> 1 & 1
        self.VBLANK = value & 1

    def get(self):
        return (
            # 7 << 5 |
            self.JOYPAD << 4
            | self.SERIAL << 3
            | self.TIMER << 2
            | self.LCD << 1
            | self.VBLANK
        )


class Joypad:
    # 0xCF -> 11001111
    # 0 is True, 1 is False
    def __init__(self):
        self.USE_SELECT = True
        self.USE_DPAD = True

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

    def get(self):
        return (
            self.USE_SELECT << 5
            | self.USE_DPAD << 4
            | ((not self.START) or (not self.DOWN)) << 3
            | ((not self.SELECT) or (not self.UP)) << 2
            | ((not self.B) or (not self.LEFT)) << 1
            | ((not self.A) or (not self.RIGHT))
        )

    def set(self, value):
        self.USE_SELECT = not (value >> 5 & 1)
        self.USE_DPAD = not (value >> 4 & 1)
