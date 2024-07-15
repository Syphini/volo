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
            case 0xFF00:
                return self.IO.P1
            case 0xFF00:
                print("TODO handle input", hex(address))
            case addr if 0xFF01 <= addr <= 0xFF02:
                print("TODO handle serial", hex(address))
            case addr if 0xFF04 <= addr <= 0xFF07:
                print("TODO handle timer registers", hex(address))
            case 0xFF0F:
                return self.IO.IF
            case addr if 0xFF10 <= addr <= 0xFF26:
                print("TODO handle audio registers", hex(address))
            case addr if 0xFF30 <= addr <= 0xFF3F:
                return self.IO.WAVE[address - 0xFF30]
            case addr if 0xFF40 <= addr <= 0xFF4B:
                return self.IO.LCD.get(addr)
            case addr if 0xFF80 <= addr <= 0xFFFE:
                return self.HRAM[address - 0xFF80]
            case 0xFFFF:
                return self.IO.IE
            case _:
                raise Exception("Inaccessible Memory:", hex(address))

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
            case 0xFF00:
                self.IO.P1 = value
            case 0xFF00:
                print("TODO handle input", hex(address))
            case addr if 0xFF01 <= addr <= 0xFF02:
                print("TODO handle serial", hex(address))
            case addr if 0xFF04 <= addr <= 0xFF07:
                print("TODO handle timer registers", hex(address))
            case 0xFF0F:
                self.IO.IF = value
            case addr if 0xFF10 <= addr <= 0xFF26:
                print("TODO handle audio registers", hex(address))
            case addr if 0xFF30 <= addr <= 0xFF3F:
                self.IO.WAVE[address - 0xFF30] = value
            case addr if 0xFF40 <= addr <= 0xFF4B:
                self.IO.LCD.set(addr, value)
            case addr if 0xFF80 <= addr <= 0xFFFE:
                self.HRAM[address - 0xFF80] = value
            case 0xFFFF:
                self.IO.IE = value
            case _:
                raise Exception("Inaccessible Memory:", hex(address))

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
                + bytearray(0x80)
                + self.HRAM,
                " ",
            ).upper()
            n = 48
            data = [
                f"{helpers.int_to_hex(i//3)} -- {dump[i:i+n]
                                             }"
                for i in range(0, len(dump), n)
            ]
            f.write("\n".join(data))
