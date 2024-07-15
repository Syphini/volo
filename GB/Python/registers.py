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
        self.HALFCARRY = 1  # temp
        self.CARRY = 1  # temp

    @property
    def AF(self):
        return self.A << 8 | (
            self.ZERO << 7
            | self.SUBTRACTION << 6
            | self.HALFCARRY << 5
            | self.CARRY << 4
        )

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
        self.SP = helpers.wrap_16(self.SP - 1)
        self.mmu.set_memory(self.SP, value >> 8)

        self.SP = helpers.wrap_16(self.SP - 1)
        self.mmu.set_memory(self.SP, value & 0xFF)

    def POP(self):
        lower = self.mmu.get_memory(self.SP)
        self.SP = helpers.wrap_16(self.SP + 1)

        higher = self.mmu.get_memory(self.SP)
        self.SP = helpers.wrap_16(self.SP + 1)

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
            "F": 0,
            "H": self.H,
            "L": self.L,
            "PC": self.PC,
            "SP": self.SP,
        }
        print([{c: hex(data[c])} for c in data])
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
        lcd = PPU(mmu)

        self.P1 = 0xCF  # FF00
        self.SB = 0x00  # FF01
        self.SC = 0x73  # FF02
        self.DIV = 0xAB  # FF04
        self.TIMA = 0x00  # FF05
        self.TMA = 0x00  # FF06
        self.TAC = 0xF8  # FF07
        self.NR10 = 0x80  # FF10
        self.NR11 = 0xBF  # FF11
        self.NR12 = 0xF3  # FF12
        self.NR13 = 0xFF  # FF13
        self.NR14 = 0xBF  # FF14
        self.NR21 = 0x3F  # FF16
        self.RN22 = 0x00  # FF17
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
        self.LCD = lcd  # FF40 -> FF4B
        # ???

        self._IF = Interrupts(0xE1)  # FF0F
        self._IE = Interrupts()  # FFFF

    @property
    def IE(self):
        return self._IE.get()

    @IE.setter
    def IE(self, value):
        self._IE.set(value)

    @property
    def IF(self):
        return self._IF.get()

    @IF.setter
    def IF(self, value):
        self._IF.set(value)


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
            self.JOYPAD << 4
            | self.SERIAL << 3
            | self.TIMER << 2
            | self.LCD << 1
            | self.VBLANK
        )
