import helpers
from mmu import MMU


class Registers:
    def __init__(self, mmu: MMU) -> None:

        self.mmu = mmu

        self.A = 0x01
        self.B = 0x00
        self.C = 0x13
        self.D = 0x00
        self.E = 0xD8
        self.H = 0x01
        self.L = 0x4D

        self.PC = (
            0x0 if mmu.USE_BOOT_ROM else 0x100
        )  # Boot ROM is 0x0; Cartridge is 0x100
        self.SP = 0xFFFE

        self.ZERO = 1
        self.SUBTRACTION = 0
        self.HALFCARRY = 1
        self.CARRY = 1

    @property
    def F(self) -> int:
        return (
            self.ZERO << 7
            | self.SUBTRACTION << 6
            | self.HALFCARRY << 5
            | self.CARRY << 4
        )

    @property
    def AF(self) -> int:
        return self.A << 8 | self.F

    @AF.setter
    def AF(self, value: int) -> None:
        self.A = value >> 8
        self.ZERO = value >> 7 & 1
        self.SUBTRACTION = value >> 6 & 1
        self.HALFCARRY = value >> 5 & 1
        self.CARRY = value >> 4 & 1

    @property
    def BC(self) -> int:
        return self.B << 8 | self.C

    @BC.setter
    def BC(self, value: int) -> None:
        self.B = value >> 8
        self.C = value & 0xFF

    @property
    def DE(self) -> int:
        return self.D << 8 | self.E

    @DE.setter
    def DE(self, value: int) -> None:
        self.D = value >> 8
        self.E = value & 0xFF

    @property
    def HL(self) -> int:
        return self.H << 8 | self.L

    @HL.setter
    def HL(self, value: int) -> None:
        self.H = value >> 8
        self.L = value & 0xFF

    def PUSH(self, value: int) -> None:
        self.SP = (self.SP - 1) & 0xFFFF
        self.mmu.set_memory(self.SP, value >> 8)

        self.SP = (self.SP - 1) & 0xFFFF
        self.mmu.set_memory(self.SP, value & 0xFF)

    def POP(self) -> int:
        lower = self.mmu.get_memory(self.SP)
        self.SP = (self.SP + 1) & 0xFFFF

        higher = self.mmu.get_memory(self.SP)
        self.SP = (self.SP + 1) & 0xFFFF

        return higher << 8 | lower

    def debug(self) -> None:
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
