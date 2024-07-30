import os
import helpers
from cartridge import Cartridge
from registers import IO


class MMU:
    def __init__(self, cartridge: Cartridge, use_boot_rom=False):

        io = IO(self)

        self.BOOT_ROM = "/lib/DMG_ROM.bin"
        self.CARTRIDGE = cartridge

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

        self.switch_bank(0)
        # TODO map boot rom over the top of BANK 0

        if use_boot_rom:
            with open(
                os.path.dirname(os.path.abspath(__file__)) + self.BOOT_ROM, "rb"
            ) as f:
                self.ROM1[0:0x100] = f.read()

        self.switch_bank(1)

        print(self.CARTRIDGE.HEADER.title)

    def switch_bank(self, bank):
        match bank:
            case 0:
                self.ROM1 = self.CARTRIDGE.MEMORY_BANKS[0]
            case _:
                self.ROM2 = self.CARTRIDGE.MEMORY_BANKS[bank]

    def get_memory(self, address):
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
                raise Exception("Inaccessible Memory:", helpers.formatted_hex(address))

    def set_memory(self, address, value):
        match address:
            case addr if 0x0000 <= addr <= 0x7FFF:
                # TODO handle ROM Banking
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
                raise Exception("Inaccessible Memory:", helpers.formatted_hex(address))

    def dump(self):
        # Hex Dump
        with open("GB\ROM\dump.md", "w") as f:
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
                f"{helpers.formatted_hex(i//3)} -- {dump[i:i+n]
                                             }"
                for i in range(0, len(dump), n)
            ]
            f.write("\n".join(data))
