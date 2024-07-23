import helpers
from registers import IO


class MMU:
    def __init__(self):

        io = IO(self)

        self.RAM = bytearray(0x8000)  # 0000 -> 7FFF
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

    def get_memory(self, address):
        match address:
            case addr if 0x0000 <= addr <= 0x7FFF:
                return self.RAM[address]
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
                self.RAM[address] = value
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
                self.RAM
                + self.VRAM
                + self.ERAM
                + self.WRAM
                + self.OAM
                + self.ECHO
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
