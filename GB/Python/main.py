import sys
import json
import pygame
import time
import traceback
import helpers
from mmu import MMU
from registers import Registers

print()

with open("GB/opcodes.json") as f:
    opcodes = json.loads(f.read())

ROM_FILE = "GB/ROM/DMG_ROM.bin"

# region Registers

mmu = MMU()
R = Registers(mmu)

IME = False

# endregion

with open(ROM_FILE, "rb") as f:
    for cycle_count, b in enumerate(f.read()):
        mmu.set_memory(cycle_count, b)

# region Graphics


pygame.init()

# Variables
PIXEL_SIZE = 2
TILE_SIZE = 1
# 160 x 144 screen size
# 256 x 256 tilemap
SCREEN_X = 256
SCREEN_Y = 256
CANVAS_SIZE = (SCREEN_X * PIXEL_SIZE, SCREEN_Y * PIXEL_SIZE)

# Pixel States
PIXEL_STATE = [(255, 246, 211), (249, 168, 117), (235, 107, 111), (124, 63, 88)]

# Canvas
canvas = pygame.display.set_mode(CANVAS_SIZE)
pygame.display.set_caption("GB Test")


def get_tile(byte_data: bytearray):
    TILE_DATA = []
    for c in range(len(byte_data) - 1):
        if c % 2 == 1:
            continue

        BYTE_1 = byte_data[c]
        BYTE_2 = byte_data[c + 1]

        colour_ids = []
        for i in range(8):
            b1 = bin(BYTE_1)[2:].zfill(8)
            b2 = bin(BYTE_2)[2:].zfill(8)
            calc = b2[i] + b1[i]
            colour_ids.append(int(calc, 2))

        TILE_DATA.append(colour_ids)
    return TILE_DATA


def draw_vram():
    """Draw the VRAM"""
    offset_x = 160
    for y in range(32):
        for x in range(32):
            tileIndex = mmu.VRAM[(0x1800 + (y * 32) + x)]
            if tileIndex != 0:
                tileData = get_tile(
                    mmu.VRAM[tileIndex * 16 : ((tileIndex + 1) * 16) - 1]
                )
                draw_tile((offset_x + x, y), tileData)


def update_display():
    """Update the display to render the current canvas"""
    pygame.display.update()


def get_pixel(x_y):
    """True or False if pixel at x_y is ON or OFF"""
    x = x_y[0] * PIXEL_SIZE
    y = x_y[1] * PIXEL_SIZE

    return canvas.get_at((x, y)) != PIXEL_STATE[0]


def draw(x_y, colour_id):
    """Draw a pixel to the canvas"""
    x = x_y[0] * PIXEL_SIZE
    y = x_y[1] * PIXEL_SIZE

    canvas.fill(PIXEL_STATE[colour_id], pygame.Rect(x, y, PIXEL_SIZE, PIXEL_SIZE))


def draw_tile(x_y, tile_data):
    """Draw a Tile to the canvas"""
    x_offset = x_y[0] * TILE_SIZE
    y_offset = x_y[1] * TILE_SIZE
    for y, t in enumerate(tile_data):
        for x, i in enumerate(t):
            draw(((x + x_offset), y + y_offset), i)


def clear_display():
    """Clear the canvas"""
    canvas.fill(PIXEL_STATE[0], pygame.Rect(0, 0, CANVAS_SIZE[0], CANVAS_SIZE[1]))


# endregion

# region Opcodes


def NOP_00():
    """NOP"""
    pass


def LD_01(value: int):
    """LD BC,n16"""
    R.BC = value


def LD_02():
    """LD [BC],A"""
    mmu.set_memory(R.BC, R.A)


def INC_03():
    """INC BC"""
    R.BC += 1


def INC_R8(register):
    initial = register
    calc = initial + 1
    final = calc % 256
    R.ZERO = 1 if final == 0 else 0
    R.SUBTRACTION = (0,)
    R.HALFCARRY = (
        1 if helpers.getLowerNibble(initial) > helpers.getLowerNibble(calc) else 0
    )
    R.INCREMENT_PC(1)
    return final


def INC_04():
    """INC B"""
    R.B = INC_R8(R.B)


def DEC_R8(register):
    initial = register
    calc = initial - 1
    final = calc % 256
    R.ZERO = 1 if final == 0 else 0
    R.SUBTRACTION = (1,)
    R.HALFCARRY = (
        1 if helpers.getLowerNibble(calc) > helpers.getLowerNibble(initial) else 0
    )
    return final


def DEC_05():
    """DEC B"""
    R.B = DEC_R8(R.B)


def LD_06(value):
    """LD B,n8"""
    R.B = value


def RLCA_07():
    initial = R.A
    carryBit = initial >> 7
    calc = (initial << 1) & 0b11111110 | carryBit
    R.A = calc
    R.ZERO = 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = carryBit


def ADD_09():
    """ADD HL,BC"""
    calc = R.HL + R.BC()
    R.HL = calc % 65536
    R.SUBTRACTION = 0
    R.HALFCARRY = 1 if calc > 2047 else 0
    R.CARRY = 1 if calc > 65535 else 0


def LD_0A():
    """LD A,[BC]"""
    R.A = mmu.get_memory(R.BC)


def DEC_0B():
    """DEC BC"""
    R.BC -= 1


def INC_0C():
    """INC C"""
    R.C = INC_R8(R.C)


def DEC_0D():
    """DEC C"""
    R.C = DEC_R8(R.C)


def LD_0E(value):
    """LD C,n8"""
    R.C = value


def RRCA_0F():
    initial = R.A
    carryBit = initial & 0b1
    calc = (carryBit << 7) | initial >> 1
    R.A = calc
    R.ZERO = 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = carryBit


def LD_11(value: int):
    """LD DE,n16"""
    R.DE = value


def LD_12():
    """LD [DE],A"""
    mmu.set_memory(R.DE, R.A)


def INC_13():
    """INC DE"""
    R.DE += 1


def INC_14():
    """INC D"""
    R.D = INC_R8(R.D)


def DEC_15():
    """DEC D"""
    R.D = DEC_R8(R.D)


def LD_16(value):
    """LD D,n8"""
    R.D = value


def RLA_17():
    initial = R.A
    carryBit = initial >> 7
    calc = (initial << 1) & 0b11111110 | R.CARRY
    R.A = calc
    R.ZERO = 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = carryBit


def JR_18(value):
    """JR e8"""
    if (value & (1 << 7)) != 0:
        addr = -(128 - (value - (1 << 7)))
        R.INCREMENT_PC(addr)
        return
    R.INCREMENT_PC(value)


def ADD_19():
    """ADD HL,DE"""
    calc = R.HL + R.DE
    R.HL = calc % 65536
    R.SUBTRACTION = 0
    R.HALFCARRY = 1 if calc > 2047 else 0
    R.CARRY = 1 if calc > 65535 else 0


def LD_1A():
    """LD A,[DE]"""
    R.A = mmu.get_memory(R.DE)


def DEC_1B():
    """DEC DE"""
    R.DE -= 1


def INC_1C():
    """INC E"""
    R.E = INC_R8(R.E)


def DEC_1D():
    """DEC E"""
    R.E = DEC_R8(R.E)


def LD_1E(value):
    """LD E,n8"""
    R.E = value


def RRA_1F(register):
    initial = register
    carryBit = initial & 0b1
    calc = (R.CARRY << 7) | initial >> 1
    R.ZERO = 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = carryBit
    return calc


def JR_20(value):
    """JR NZ,e8"""
    if R.ZERO == 0:
        JR_18(value)


def LD_21(value: int):
    """LD HL,n16"""
    R.HL = value


def LD_22():
    """LD [HLI],A"""
    mmu.set_memory(R.HL, R.A)
    R.HL += 1


def INC_23():
    """INC HL"""
    R.HL += 1


def INC_24():
    """INC H"""
    R.H = INC_R8(R.H)


def DEC_25():
    """DEC H"""
    R.H = DEC_R8(R.H)


def LD_26(value):
    """LD H,n8"""
    R.H = value


def JR_28(value):
    """JR Z,e8"""
    if R.ZERO == 1:
        JR_18(value)


def ADD_29():
    """ADD HL,HL"""
    calc = R.HL + R.HL
    R.HL = calc % 65536
    R.SUBTRACTION = 0
    R.HALFCARRY = 1 if calc > 2047 else 0
    R.CARRY = 1 if calc > 65535 else 0


def LD_2A():
    """LD A,[HLI]"""
    R.A = mmu.get_memory(R.HL)
    R.HL += 1


def DEC_2B():
    """DEC HL"""
    R.HL -= 1


def INC_2C():
    """INC L"""
    R.L - INC_R8(R.L)


def DEC_2D():
    """DEC L"""
    R.L = DEC_R8(R.L)


def LD_2E(value):
    """LD L,n8"""
    R.L = value


def CPL_2F():
    """CPL"""
    R.A = R.A ^ 0b11111111
    R.SUBTRACTION = 1
    R.HALFCARRY = 1


def JR_30(value):
    """JR NC,e8"""
    if R.CARRY == 0:
        JR_18(value)


def LD_31(value: int):
    """LD SP,n16"""
    R.SP = value


def LD_32():
    """LD [HLD],A"""
    mmu.set_memory(R.HL, R.A)
    R.HL -= 1


def INC_33():
    """INC SP"""
    R.SP += 1


def INC_34():
    """INC [HL]"""
    mmu.set_memory(R.HL, mmu.get_memory(R.HL) + 1)


def DEC_35():
    """DEC [HL]"""
    mmu.set_memory(R.HL, mmu.get_memory(R.HL) - 1)


def LD_36(value):
    """LD [HL],n8"""
    mmu.set_memory(R.HL, value)


def SCF_37():
    """SCF"""
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = 1


def JR_38(value):
    """JR C,e8"""
    if R.CARRY == 1:
        JR_18(value)


def ADD_39():
    """ADD HL,SP"""
    calc = R.HL + R.SP
    R.HL = calc % 65536
    R.SUBTRACTION = 0
    R.HALFCARRY = 1 if calc > 2047 else 0
    R.CARRY = 1 if calc > 65535 else 0


def LD_3A():
    """LD A,[HLD]"""
    R.A = mmu.get_memory(R.HL)
    R.HL -= 1


def DEC_3B():
    """DEC SP"""
    R.SP -= 1


def INC_3C():
    """INC A"""
    R.A = INC_R8(R.A)


def DEC_3D():
    """DEC A"""
    R.A = DEC_R8(R.A)


def LD_3E(value):
    """LD A,n8"""
    R.A = value


def CCF_3F():
    """CCF"""
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = 1 if R.CARRY == 0 else 0


def LD_40():
    """LD B,B"""
    R.B = R.B


def LD_41():
    """LD B,C"""
    R.B = R.C


def LD_42():
    """LD B,D"""
    R.B = R.D


def LD_43():
    """LD B,E"""
    R.B = R.E


def LD_44():
    """LD B,H"""
    R.B = R.H


def LD_45():
    """LD B,L"""
    R.B = R.L


def LD_46():
    """LD B,[HL]"""
    R.B = mmu.get_memory(R.HL)


def LD_47():
    """LD B,A"""
    R.B = R.A


def LD_48():
    """LD C,B"""
    R.C = R.B


def LD_49():
    """LD C,C"""
    R.C = R.C


def LD_4A():
    """LD C,D"""
    R.C = R.D


def LD_4B():
    """LD C,E"""
    R.C = R.E


def LD_4C():
    """LD C,H"""
    R.C = R.H


def LD_4D():
    """LD C,L"""
    R.C = R.L


def LD_4E():
    """LD C,[HL]"""
    R.C = mmu.get_memory(R.HL)


def LD_4F():
    """LD C,A"""
    R.C = R.A


def LD_50():
    """LD D,B"""
    R.D = R.B


def LD_51():
    """LD D,C"""
    R.D = R.C


def LD_52():
    """LD D,D"""
    R.D = R.D


def LD_53():
    """LD D,E"""
    R.D = R.E


def LD_54():
    """LD D,H"""
    R.D = R.H


def LD_55():
    """LD D,L"""
    R.D = R.L


def LD_56():
    """LD D,[HL]"""
    R.D = mmu.get_memory(R.HL)


def LD_57():
    """LD D,A"""
    R.D = R.A


def LD_58():
    """LD E,B"""
    R.E = R.B


def LD_59():
    """LD E,C"""
    R.E = R.C


def LD_5A():
    """LD E,D"""
    R.E = R.D


def LD_5B():
    """LD E,E"""
    R.E = R.E


def LD_5C():
    """LD E,H"""
    R.E = R.H


def LD_5D():
    """LD E,L"""
    R.E = R.L


def LD_5E():
    """LD E,[HL]"""
    R.E = mmu.get_memory(R.HL)


def LD_5F():
    """LD E,A"""
    R.E = R.A


def LD_60():
    """LD H,B"""
    R.H = R.B


def LD_61():
    """LD H,C"""
    R.H = R.C


def LD_62():
    """LD H,D"""
    R.H = R.D


def LD_63():
    """LD H,E"""
    R.H = R.E


def LD_64():
    """LD H,H"""
    R.H = R.H


def LD_65():
    """LD H,L"""
    R.H = R.L


def LD_66():
    """LD H,[HL]"""
    R.H = mmu.get_memory(R.HL)


def LD_67():
    """LD H,A"""
    R.H = R.A


def LD_68():
    """LD L,B"""
    R.L = R.B


def LD_69():
    """LD L,C"""
    R.L = R.C


def LD_6A():
    """LD L,D"""
    R.L = R.D


def LD_6B():
    """LD L,E"""
    R.L = R.E


def LD_6C():
    """LD L,H"""
    R.L = R.H


def LD_6D():
    """LD L,L"""
    R.L = R.L


def LD_6E():
    """LD L,[HL]"""
    R.L = mmu.get_memory(R.HL)


def LD_6F():
    """LD L,A"""
    R.L = R.A


def LD_70():
    """LD [HL],B"""
    mmu.set_memory(R.HL, R.B)


def LD_71():
    """LD [HL],C"""
    mmu.set_memory(R.HL, R.C)


def LD_72():
    """LD [HL],D"""
    mmu.set_memory(R.HL, R.D)


def LD_73():
    """LD [HL],E"""
    mmu.set_memory(R.HL, R.E)


def LD_74():
    """LD [HL],H"""
    mmu.set_memory(R.HL, R.H)


def LD_75():
    """LD [HL],L"""
    mmu.set_memory(R.HL, R.L)


def HALT_76():
    """HALT"""
    raise Exception("HALT")


def LD_77():
    """LD [HL],A"""
    mmu.set_memory(R.HL, R.A)


def LD_78():
    """LD A,B"""
    R.A = R.B


def LD_79():
    """LD A,C"""
    R.A = R.C


def LD_7A():
    """LD A,D"""
    R.A = R.D


def LD_7B():
    """LD A,E"""
    R.A = R.E


def LD_7C():
    """LD A,H"""
    R.A = R.H


def LD_7D():
    """LD A,L"""
    R.A = R.L


def LD_7E():
    """LD A,[HL]"""
    R.A = mmu.get_memory(R.HL)


def LD_7F():
    """LD A,A"""
    R.A = R.A


def ADD_A_N8(value):
    initial = R.A
    calc = initial + value
    final = calc % 256
    R.A = final
    R.ZERO = 1 if final == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = (
        1 if helpers.getLowerNibble(initial) > helpers.getLowerNibble(value) else 0
    )
    R.CARRY = 1 if calc > 255 else 0


def ADD_80():
    """ADD A,B"""
    ADD_A_N8(R.B)


def ADD_81():
    """ADD A,C"""
    ADD_A_N8(R.C)


def ADD_82():
    """ADD A,D"""
    ADD_A_N8(R.D)


def ADD_83():
    """ADD A,E"""
    ADD_A_N8(R.E)


def ADD_84():
    """ADD A,H"""
    ADD_A_N8(R.H)


def ADD_85():
    """ADD A,L"""
    ADD_A_N8(R.L)


def ADD_86():
    """ADD A,[HL]"""
    ADD_A_N8(mmu.get_memory(R.HL))


def ADD_87():
    """ADD A,A"""
    ADD_A_N8(R.A)


def ADC_A_N8(value):
    initial = R.A
    value = value + R.CARRY
    calc = initial + value
    final = calc % 256
    R.A = final
    R.ZERO = 1 if final == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = (
        1 if helpers.getLowerNibble(initial) > helpers.getLowerNibble(value) else 0
    )
    R.CARRY = 1 if calc > 255 else 0


def ADC_88():
    """ADC A,B"""
    ADC_A_N8(R.B)


def ADC_89():
    """ADC A,C"""
    ADC_A_N8(R.C)


def ADC_8A():
    """ADC A,D"""
    ADC_A_N8(R.D)


def ADC_8B():
    """ADC A,E"""
    ADC_A_N8(R.E)


def ADC_8C():
    """ADC A,H"""
    ADC_A_N8(R.H)


def ADC_8D():
    """ADC A,L"""
    ADC_A_N8(R.L)


def ADC_8E():
    """ADC A,[HL]"""
    ADC_A_N8(mmu.get_memory(R.HL))


def ADC_8F():
    """ADC A,A"""
    ADC_A_N8(R.A)


def SUB_A_N8(value):
    initial = R.A
    calc = initial - value
    final = calc % 256
    R.A = final
    R.ZERO = 1 if final == 0 else 0
    R.SUBTRACTION = 1
    R.HALFCARRY = (
        1 if helpers.getLowerNibble(value) > helpers.getLowerNibble(initial) else 0
    )
    R.CARRY = 1 if calc < 0 else 0


def SUB_90():
    """SUB A,B"""
    SUB_A_N8(R.B)


def SUB_91():
    """SUB A,C"""
    SUB_A_N8(R.C)


def SUB_92():
    """SUB A,D"""
    SUB_A_N8(R.D)


def SUB_93():
    """SUB A,E"""
    SUB_A_N8(R.E)


def SUB_94():
    """SUB A,H"""
    SUB_A_N8(R.H)


def SUB_95():
    """SUB A,L"""
    SUB_A_N8(R.L)


def SUB_96():
    """SUB A,[HL]"""
    SUB_A_N8(mmu.get_memory(R.HL))


def SUB_97():
    """SUB A,A"""
    SUB_A_N8(R.A)


def SBC_A_N8(value):
    initial = R.A
    value = value + R.CARRY
    calc = initial - value
    final = calc % 256
    R.A = final
    R.ZERO = 1 if final == 0 else 0
    R.SUBTRACTION = 1
    R.HALFCARRY = (
        1 if helpers.getLowerNibble(value) > helpers.getLowerNibble(initial) else 0
    )
    R.CARRY = 1 if calc < 0 else 0


def SBC_98():
    """SBC A,B"""
    SBC_A_N8(R.B)


def SBC_99():
    """SBC A,C"""
    SBC_A_N8(R.C)


def SBC_9A():
    """SBC A,D"""
    SBC_A_N8(R.D)


def SBC_9B():
    """SBC A,E"""
    SBC_A_N8(R.E)


def SBC_9C():
    """SBC A,H"""
    SBC_A_N8(R.H)


def SBC_9D():
    """SBC A,L"""
    SBC_A_N8(R.L)


def SBC_9E():
    """SBC A,[HL]"""
    SBC_A_N8(mmu.get_memory(R.HL))


def SBC_9F():
    """SBC A,A"""
    SBC_A_N8(R.A)


def AND_A_N8(value):
    initial = R.A
    calc = initial & value
    R.A = calc
    R.ZERO = 1 if calc == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 1
    R.CARRY = 0


def AND_A0():
    """AND A,B"""
    AND_A_N8(R.B)


def AND_A1():
    """AND A,C"""
    AND_A_N8(R.C)


def AND_A2():
    """AND A,D"""
    AND_A_N8(R.D)


def AND_A3():
    """AND A,E"""
    AND_A_N8(R.E)


def AND_A4():
    """AND A,H"""
    AND_A_N8(R.H)


def AND_A5():
    """AND A,L"""
    AND_A_N8(R.L)


def AND_A6():
    """AND A,[HL]"""
    AND_A_N8(mmu.get_memory(R.HL))


def AND_A7():
    """AND A,A"""
    AND_A_N8(R.A)


def XOR_A_N8(value):
    initial = R.A
    calc = initial ^ value
    R.A = calc
    R.ZERO = 1 if calc == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = 0


def XOR_A8():
    """XOR A,B"""
    XOR_A_N8(R.B)


def XOR_A9():
    """XOR A,C"""
    XOR_A_N8(R.C)


def XOR_AA():
    """XOR A,D"""
    XOR_A_N8(R.D)


def XOR_AB():
    """XOR A,E"""
    XOR_A_N8(R.E)


def XOR_AC():
    """XOR A,H"""
    XOR_A_N8(R.H)


def XOR_AD():
    """XOR A,L"""
    XOR_A_N8(R.L)


def XOR_AE():
    """XOR A,[HL]"""
    XOR_A_N8(mmu.get_memory(R.HL))


def XOR_AF():
    """XOR A,A"""
    XOR_A_N8(R.A)


def OR_A_N8(value):
    initial = R.A
    calc = initial | value
    R.A = calc
    R.ZERO = 1 if calc == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = 0


def OR_B0():
    """OR A,B"""
    OR_A_N8(R.B)


def OR_B1():
    """OR A,C"""
    OR_A_N8(R.C)


def OR_B2():
    """OR A,D"""
    OR_A_N8(R.D)


def OR_B3():
    """OR A,E"""
    OR_A_N8(R.E)


def OR_B4():
    """OR A,H"""
    OR_A_N8(R.H)


def OR_B5():
    """OR A,L"""
    OR_A_N8(R.L)


def OR_B6():
    """OR A,[HL]"""
    OR_A_N8(mmu.get_memory(R.HL))


def OR_B7():
    """OR A,A"""
    OR_A_N8(R.A)


def CP_A_N8(value):
    initial = R.A
    calc = initial - value
    final = calc % 256
    R.ZERO = 1 if final == 0 else 0
    R.SUBTRACTION = 1
    R.HALFCARRY = (
        1 if helpers.getLowerNibble(value) > helpers.getLowerNibble(initial) else 0
    )
    R.CARRY = 1 if calc < 0 else 0


def CP_B8():
    """CP A,B"""
    CP_A_N8(R.B)


def CP_B9():
    """CP A,C"""
    CP_A_N8(R.C)


def CP_BA():
    """CP A,D"""
    CP_A_N8(R.D)


def CP_BB():
    """CP A,E"""
    CP_A_N8(R.E)


def CP_BC():
    """CP A,H"""
    CP_A_N8(R.H)


def CP_BD():
    """CP A,L"""
    CP_A_N8(R.L)


def CP_BE():
    """CP A,[HL]"""
    CP_A_N8(mmu.get_memory(R.HL))


def CP_BF():
    """CP A,A"""
    CP_A_N8(R.A)


def RET_C0():
    """RET NZ"""
    if R.ZERO == 0:
        JP_C3(R.POP())


def POP_C1():
    """POP BC"""
    R.BC = R.POP()


def JP_C2(value):
    """JP NZ,n16"""
    if R.ZERO == 0:
        R.PC = value


def JP_C3(value):
    """JP n16"""
    R.PC = value


def CALL_C4(value):
    """CALL NZ,n16"""
    if R.ZERO == 0:
        R.PUSH(R.PC)
        JP_C3(value)


def PUSH_C5():
    """PUSH BC"""
    R.PUSH(R.BC)


def ADD_C6(value):
    """ADD A,n8"""
    ADD_A_N8(value)


def RET_C8():
    """RET Z"""
    if R.ZERO == 1:
        JP_C3(R.POP())


def RET_C9():
    """RET"""
    JP_C3(R.POP())


def JP_CA(value):
    """JP Z,n16"""
    if R.ZERO == 1:
        R.PC = value


def RLC_R8(value):
    initial = value
    carryBit = initial >> 7
    calc = (initial << 1) & 0b11111110 | carryBit
    R.ZERO = 1 if calc == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = carryBit
    return calc


def RLC_CB00():
    """RLC B"""
    R.B = RLC_R8(R.B)


def RLC_CB01():
    """RLC C"""
    R.C = RLC_R8(R.C)


def RLC_CB02():
    """RLC D"""
    R.D = RLC_R8(R.D)


def RLC_CB03():
    """RLC E"""
    R.E = RLC_R8(R.E)


def RLC_CB04():
    """RLC H"""
    R.H = RLC_R8(R.H)


def RLC_CB05():
    """RLC L"""
    R.L = RLC_R8(R.L)


def RLC_CB06():
    """RLC [HL]"""
    mmu.set_memory(R.HL, RLC_R8(mmu.get_memory(R.HL)))


def RLC_CB07():
    """RLC A"""
    R.A = RLC_R8(R.A)


def RRC_R8(register):
    initial = register
    carryBit = initial & 0b1
    calc = (carryBit << 7) | initial >> 1
    R.ZERO = 1 if calc == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = carryBit
    return calc


def RRC_CB08():
    """RRC B"""
    R.B = RRC_R8(R.B)


def RRC_CB09():
    """RRC C"""
    R.C = RRC_R8(R.C)


def RRC_CB0A():
    """RRC D"""
    R.D = RRC_R8(R.D)


def RRC_CB0B():
    """RRC E"""
    R.E = RRC_R8(R.E)


def RRC_CB0C():
    """RRC H"""
    R.H = RRC_R8(R.H)


def RRC_CB0D():
    """RRC L"""
    R.L = RRC_R8(R.L)


def RRC_CB0E():
    """RRC [HL]"""
    mmu.set_memory(R.HL, RRC_R8(mmu.get_memory(R.HL)))


def RRC_CB0F():
    """RRC A"""
    R.A = RRC_R8(R.A)


def RL_R8(register):
    initial = register
    carryBit = initial >> 7
    calc = (initial << 1) & 0b11111110 | R.CARRY
    R.ZERO = 1 if calc == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = carryBit
    return calc


def RL_CB10():
    """RL B"""
    R.B = RL_R8(R.B)


def RL_CB11():
    """RL C"""
    R.C = RL_R8(R.C)


def RL_CB12():
    """RL D"""
    R.D = RL_R8(R.D)


def RL_CB13():
    """RL E"""
    R.E = RL_R8(R.E)


def RL_CB14():
    """RL H"""
    R.H = RL_R8(R.H)


def RL_CB15():
    """RL L"""
    R.L = RL_R8(R.L)


def RL_CB16():
    """RL [HL]"""
    mmu.set_memory(R.HL, RL_R8(mmu.get_memory(R.HL)))


def RL_CB17():
    """RL A"""
    R.A = RL_R8(R.A)


def RR_R8(register):
    initial = register
    carryBit = initial & 0b1
    calc = (R.CARRY << 7) | initial >> 1
    R.ZERO = 1 if calc == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = carryBit
    return calc


def RR_CB18():
    """RR B"""
    R.B = RR_R8(R.B)


def RR_CB19():
    """RR C"""
    R.C = RR_R8(R.C)


def RR_CB1A():
    """RR D"""
    R.D = RR_R8(R.D)


def RR_CB1B():
    """RR E"""
    R.E = RR_R8(R.E)


def RR_CB1C():
    """RR H"""
    R.H = RR_R8(R.H)


def RR_CB1D():
    """RR L"""
    R.L = RR_R8(R.L)


def RR_CB1E():
    """RR [HL]"""
    mmu.set_memory(R.HL, RR_R8(mmu.get_memory(R.HL)))


def RR_CB1F():
    """RR A"""
    R.A = RR_R8(R.A)


def SLA_R8(register):
    initial = register
    carryBit = initial >> 7
    calc = (initial << 1) & 0b11111110
    R.ZERO = 1 if calc == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = carryBit
    return calc


def SLA_CB20():
    """SLA B"""
    R.B = SLA_R8(R.B)


def SLA_CB21():
    """SLA C"""
    R.C = SLA_R8(R.C)


def SLA_CB22():
    """SLA D"""
    R.D = SLA_R8(R.D)


def SLA_CB23():
    """SLA E"""
    R.E = SLA_R8(R.E)


def SLA_CB24():
    """SLA H"""
    R.H = SLA_R8(R.H)


def SLA_CB25():
    """SLA L"""
    R.L = SLA_R8(R.L)


def SLA_CB26():
    """SLA [HL]"""
    mmu.set_memory(R.HL, SLA_R8(mmu.get_memory(R.HL)))


def SLA_CB27():
    """SLA A"""
    R.A = SLA_R8(R.A)


def SRA_R8(register):
    initial = register
    carryBit = initial & 0b1
    calc = (initial >> 7) << 7 | initial >> 1
    R.ZERO = 1 if calc == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = carryBit
    return calc


def SRA_CB28():
    """SRA B"""
    R.B = SRA_R8(R.B)


def SRA_CB29():
    """SRA C"""
    R.C = SRA_R8(R.C)


def SRA_CB2A():
    """SRA D"""
    R.D = SRA_R8(R.D)


def SRA_CB2B():
    """SRA E"""
    R.E = SRA_R8(R.E)


def SRA_CB2C():
    """SRA H"""
    R.H = SRA_R8(R.H)


def SRA_CB2D():
    """SRA L"""
    R.L = SRA_R8(R.L)


def SRA_CB2E():
    """SRA [HL]"""
    mmu.set_memory(R.HL, SRA_R8(mmu.get_memory(R.HL)))


def SRA_CB2F():
    """SRA A"""
    R.A = SRA_R8(R.A)


def SWAP_R8(register):
    initial = register
    calc = (initial & 0b1111) << 4 | (initial >> 4)
    R.ZERO = 1 if calc == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = 0
    return calc


def SWAP_CB30():
    """SWAP B"""
    R.B = SWAP_R8(R.B)


def SWAP_CB31():
    """SWAP C"""
    R.C = SWAP_R8(R.C)


def SWAP_CB32():
    """SWAP D"""
    R.D = SWAP_R8(R.D)


def SWAP_CB33():
    """SWAP E"""
    R.E = SWAP_R8(R.E)


def SWAP_CB34():
    """SWAP H"""
    R.H = SWAP_R8(R.H)


def SWAP_CB35():
    """SWAP L"""
    R.L = SWAP_R8(R.L)


def SWAP_CB36():
    """SWAP [HL]"""
    mmu.set_memory(R.HL, SWAP_R8(mmu.get_memory(R.HL)))


def SWAP_CB37():
    """SWAP A"""
    R.A = SWAP_R8(R.A)


def SRL_R8(register):
    initial = register
    carryBit = initial & 0b1
    calc = initial >> 1 & 0b011111111
    R.ZERO = 1 if calc == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 0
    R.CARRY = carryBit
    return calc


def SRL_CB38():
    """SRL B"""
    R.B = SRL_R8(R.B)


def SRL_CB39():
    """SRL C"""
    R.C = SRL_R8(R.C)


def SRL_CB3A():
    """SRL D"""
    R.D = SRL_R8(R.D)


def SRL_CB3B():
    """SRL E"""
    R.E = SRL_R8(R.E)


def SRL_CB3C():
    """SRL H"""
    R.H = SRL_R8(R.H)


def SRL_CB3D():
    """SRL L"""
    R.L = SRL_R8(R.L)


def SRL_CB3E():
    """SRL [HL]"""
    mmu.set_memory(R.HL, SRL_R8(mmu.get_memory(R.HL)))


def SRL_CB3F():
    """SRL A"""
    R.A = SRL_R8(R.A)


def BIT_U3R8(register, value):
    initial = register
    calc = initial >> (value) & 0b1
    R.ZERO = 1 if calc == 0 else 0
    R.SUBTRACTION = 0
    R.HALFCARRY = 1


def BIT_CB40():
    """BIT 0,B"""
    BIT_U3R8(R.B, 0)


def BIT_CB41():
    """BIT 0,C"""
    BIT_U3R8(R.C, 0)


def BIT_CB42():
    """BIT 0,D"""
    BIT_U3R8(R.D, 0)


def BIT_CB43():
    """BIT 0,E"""
    BIT_U3R8(R.E, 0)


def BIT_CB44():
    """BIT 0,H"""
    BIT_U3R8(R.H, 0)


def BIT_CB45():
    """BIT 0,L"""
    BIT_U3R8(R.L, 0)


def BIT_CB46():
    """BIT 0,[HL]"""
    BIT_U3R8(mmu.get_memory(R.HL), 0)


def BIT_CB47():
    """BIT 0,A"""
    BIT_U3R8(R.A, 0)


def BIT_CB48():
    """BIT 1,B"""
    BIT_U3R8(R.B, 1)


def BIT_CB49():
    """BIT 1,C"""
    BIT_U3R8(R.C, 1)


def BIT_CB4A():
    """BIT 1,D"""
    BIT_U3R8(R.D, 1)


def BIT_CB4B():
    """BIT 1,E"""
    BIT_U3R8(R.E, 1)


def BIT_CB4C():
    """BIT 1,H"""
    BIT_U3R8(R.H, 1)


def BIT_CB4D():
    """BIT 1,L"""
    BIT_U3R8(R.L, 1)


def BIT_CB4E():
    """BIT 1,[HL]"""
    BIT_U3R8(mmu.get_memory(R.HL), 1)


def BIT_CB4F():
    """BIT 1,A"""
    BIT_U3R8(R.A, 1)


def BIT_CB50():
    """BIT 2,B"""
    BIT_U3R8(R.B, 2)


def BIT_CB51():
    """BIT 2,C"""
    BIT_U3R8(R.C, 2)


def BIT_CB52():
    """BIT 2,D"""
    BIT_U3R8(R.D, 2)


def BIT_CB53():
    """BIT 2,E"""
    BIT_U3R8(R.E, 2)


def BIT_CB54():
    """BIT 2,H"""
    BIT_U3R8(R.H, 2)


def BIT_CB55():
    """BIT 2,L"""
    BIT_U3R8(R.L, 2)


def BIT_CB56():
    """BIT 2,[HL]"""
    BIT_U3R8(mmu.get_memory(R.HL), 2)


def BIT_CB57():
    """BIT 2,A"""
    BIT_U3R8(R.A, 2)


def BIT_CB58():
    """BIT 3,B"""
    BIT_U3R8(R.B, 3)


def BIT_CB59():
    """BIT 3,C"""
    BIT_U3R8(R.C, 3)


def BIT_CB5A():
    """BIT 3,D"""
    BIT_U3R8(R.D, 3)


def BIT_CB5B():
    """BIT 3,E"""
    BIT_U3R8(R.E, 3)


def BIT_CB5C():
    """BIT 3,H"""
    BIT_U3R8(R.H, 3)


def BIT_CB5D():
    """BIT 3,L"""
    BIT_U3R8(R.L, 3)


def BIT_CB5E():
    """BIT 3,[HL]"""
    BIT_U3R8(mmu.get_memory(R.HL), 3)


def BIT_CB5F():
    """BIT 3,A"""
    BIT_U3R8(R.A, 3)


def BIT_CB60():
    """BIT 4,B"""
    BIT_U3R8(R.B, 4)


def BIT_CB61():
    """BIT 4,C"""
    BIT_U3R8(R.C, 4)


def BIT_CB62():
    """BIT 4,D"""
    BIT_U3R8(R.D, 4)


def BIT_CB63():
    """BIT 4,E"""
    BIT_U3R8(R.E, 4)


def BIT_CB64():
    """BIT 4,H"""
    BIT_U3R8(R.H, 4)


def BIT_CB65():
    """BIT 4,L"""
    BIT_U3R8(R.L, 4)


def BIT_CB66():
    """BIT 4,[HL]"""
    BIT_U3R8(mmu.get_memory(R.HL), 4)


def BIT_CB67():
    """BIT 4,A"""
    BIT_U3R8(R.A, 4)


def BIT_CB68():
    """BIT 5,B"""
    BIT_U3R8(R.B, 5)


def BIT_CB69():
    """BIT 5,C"""
    BIT_U3R8(R.C, 5)


def BIT_CB6A():
    """BIT 5,D"""
    BIT_U3R8(R.D, 5)


def BIT_CB6B():
    """BIT 5,E"""
    BIT_U3R8(R.E, 5)


def BIT_CB6C():
    """BIT 5,H"""
    BIT_U3R8(R.H, 5)


def BIT_CB6D():
    """BIT 5,L"""
    BIT_U3R8(R.L, 5)


def BIT_CB6E():
    """BIT 5,[HL]"""
    BIT_U3R8(mmu.get_memory(R.HL), 5)


def BIT_CB6F():
    """BIT 5,A"""
    BIT_U3R8(R.A, 5)


def BIT_CB70():
    """BIT 6,B"""
    BIT_U3R8(R.B, 6)


def BIT_CB71():
    """BIT 6,C"""
    BIT_U3R8(R.C, 6)


def BIT_CB72():
    """BIT 6,D"""
    BIT_U3R8(R.D, 6)


def BIT_CB73():
    """BIT 6,E"""
    BIT_U3R8(R.E, 6)


def BIT_CB74():
    """BIT 6,H"""
    BIT_U3R8(R.H, 6)


def BIT_CB75():
    """BIT 6,L"""
    BIT_U3R8(R.L, 6)


def BIT_CB76():
    """BIT 6,[HL]"""
    BIT_U3R8(mmu.get_memory(R.HL), 6)


def BIT_CB77():
    """BIT 6,A"""
    BIT_U3R8(R.A, 6)


def BIT_CB78():
    """BIT 7,B"""
    BIT_U3R8(R.B, 7)


def BIT_CB79():
    """BIT 7,C"""
    BIT_U3R8(R.C, 7)


def BIT_CB7A():
    """BIT 7,D"""
    BIT_U3R8(R.D, 7)


def BIT_CB7B():
    """BIT 7,E"""
    BIT_U3R8(R.E, 7)


def BIT_CB7C():
    """BIT 7,H"""
    BIT_U3R8(R.H, 7)


def BIT_CB7D():
    """BIT 7,L"""
    BIT_U3R8(R.L, 7)


def BIT_CB7E():
    """BIT 7,[HL]"""
    BIT_U3R8(mmu.get_memory(R.HL), 7)


def BIT_CB7F():
    """BIT 7,A"""
    BIT_U3R8(R.A, 7)


def RES_U3R8(register, value):
    initial = register
    higher = initial >> value + 1 << value + 1
    lower = ((initial << 8 - value) & 0xFF) >> 8 - value
    calc = higher | lower
    return calc


def RES_CB80():
    """RES 0,B"""
    R.B = RES_U3R8(R.B, 0)


def RES_CB81():
    """RES 0,C"""
    R.C = RES_U3R8(R.C, 0)


def RES_CB82():
    """RES 0,D"""
    R.D = RES_U3R8(R.D, 0)


def RES_CB83():
    """RES 0,E"""
    R.E = RES_U3R8(R.E, 0)


def RES_CB84():
    """RES 0,H"""
    R.H = RES_U3R8(R.H, 0)


def RES_CB85():
    """RES 0,L"""
    R.L = RES_U3R8(R.L, 0)


def RES_CB86():
    """RES 0,[HL]"""
    mmu.set_memory(R.HL, RES_U3R8(mmu.get_memory(R.HL), 0))


def RES_CB87():
    """RES 0,A"""
    R.A = RES_U3R8(R.A, 0)


def RES_CB88():
    """RES 1,B"""
    R.B = RES_U3R8(R.B, 1)


def RES_CB89():
    """RES 1,C"""
    R.C = RES_U3R8(R.C, 1)


def RES_CB8A():
    """RES 1,D"""
    R.D = RES_U3R8(R.D, 1)


def RES_CB8B():
    """RES 1,E"""
    R.E = RES_U3R8(R.E, 1)


def RES_CB8C():
    """RES 1,H"""
    R.H = RES_U3R8(R.H, 1)


def RES_CB8D():
    """RES 1,L"""
    R.L = RES_U3R8(R.L, 1)


def RES_CB8E():
    """RES 1,[HL]"""
    mmu.set_memory(R.HL, RES_U3R8(mmu.get_memory(R.HL), 1))


def RES_CB8F():
    """RES 1,A"""
    R.A = RES_U3R8(R.A, 1)


def RES_CB90():
    """RES 2,B"""
    R.B = RES_U3R8(R.B, 2)


def RES_CB91():
    """RES 2,C"""
    R.C = RES_U3R8(R.C, 2)


def RES_CB92():
    """RES 2,D"""
    R.D = RES_U3R8(R.D, 2)


def RES_CB93():
    """RES 2,E"""
    R.E = RES_U3R8(R.E, 2)


def RES_CB94():
    """RES 2,H"""
    R.H = RES_U3R8(R.H, 2)


def RES_CB95():
    """RES 2,L"""
    R.L = RES_U3R8(R.L, 2)


def RES_CB96():
    """RES 2,[HL]"""
    mmu.set_memory(R.HL, RES_U3R8(mmu.get_memory(R.HL), 2))


def RES_CB97():
    """RES 2,A"""
    R.A = RES_U3R8(R.A, 2)


def RES_CB98():
    """RES 3,B"""
    R.B = RES_U3R8(R.B, 3)


def RES_CB99():
    """RES 3,C"""
    R.C = RES_U3R8(R.C, 3)


def RES_CB9A():
    """RES 3,D"""
    R.D = RES_U3R8(R.D, 3)


def RES_CB9B():
    """RES 3,E"""
    R.E = RES_U3R8(R.E, 3)


def RES_CB9C():
    """RES 3,H"""
    R.H = RES_U3R8(R.H, 3)


def RES_CB9D():
    """RES 3,L"""
    R.L = RES_U3R8(R.L, 3)


def RES_CB9E():
    """RES 3,[HL]"""
    mmu.set_memory(R.HL, RES_U3R8(mmu.get_memory(R.HL), 3))


def RES_CB9F():
    """RES 3,A"""
    R.A = RES_U3R8(R.A, 3)


def RES_CBA0():
    """RES 4,B"""
    R.B = RES_U3R8(R.B, 4)


def RES_CBA1():
    """RES 4,C"""
    R.C = RES_U3R8(R.C, 4)


def RES_CBA2():
    """RES 4,D"""
    R.D = RES_U3R8(R.D, 4)


def RES_CBA3():
    """RES 4,E"""
    R.E = RES_U3R8(R.E, 4)


def RES_CBA4():
    """RES 4,H"""
    R.H = RES_U3R8(R.H, 4)


def RES_CBA5():
    """RES 4,L"""
    R.L = RES_U3R8(R.L, 4)


def RES_CBA6():
    """RES 4,[HL]"""
    mmu.set_memory(R.HL, RES_U3R8(mmu.get_memory(R.HL), 4))


def RES_CBA7():
    """RES 4,A"""
    R.A = RES_U3R8(R.A, 4)


def RES_CBA8():
    """RES 5,B"""
    R.B = RES_U3R8(R.B, 5)


def RES_CBA9():
    """RES 5,C"""
    R.C = RES_U3R8(R.C, 5)


def RES_CBAA():
    """RES 5,D"""
    R.D = RES_U3R8(R.D, 5)


def RES_CBAB():
    """RES 5,E"""
    R.E = RES_U3R8(R.E, 5)


def RES_CBAC():
    """RES 5,H"""
    R.H = RES_U3R8(R.H, 5)


def RES_CBAD():
    """RES 5,L"""
    R.L = RES_U3R8(R.L, 5)


def RES_CBAE():
    """RES 5,[HL]"""
    mmu.set_memory(R.HL, RES_U3R8(mmu.get_memory(R.HL), 5))


def RES_CBAF():
    """RES 5,A"""
    R.A = RES_U3R8(R.A, 5)


def RES_CBB0():
    """RES 6,B"""
    R.B = RES_U3R8(R.B, 6)


def RES_CBB1():
    """RES 6,C"""
    R.C = RES_U3R8(R.C, 6)


def RES_CBB2():
    """RES 6,D"""
    R.D = RES_U3R8(R.D, 6)


def RES_CBB3():
    """RES 6,E"""
    R.E = RES_U3R8(R.E, 6)


def RES_CBB4():
    """RES 6,H"""
    R.H = RES_U3R8(R.H, 6)


def RES_CBB5():
    """RES 6,L"""
    R.L = RES_U3R8(R.L, 6)


def RES_CBB6():
    """RES 6,[HL]"""
    mmu.set_memory(R.HL, RES_U3R8(mmu.get_memory(R.HL), 6))


def RES_CBB7():
    """RES 6,A"""
    R.A = RES_U3R8(R.A, 6)


def RES_CBB8():
    """RES 7,B"""
    R.B = RES_U3R8(R.B, 7)


def RES_CBB9():
    """RES 7,C"""
    R.C = RES_U3R8(R.C, 7)


def RES_CBBA():
    """RES 7,D"""
    R.D = RES_U3R8(R.D, 7)


def RES_CBBB():
    """RES 7,E"""
    R.E = RES_U3R8(R.E, 7)


def RES_CBBC():
    """RES 7,H"""
    R.H = RES_U3R8(R.H, 7)


def RES_CBBD():
    """RES 7,L"""
    R.L = RES_U3R8(R.L, 7)


def RES_CBBE():
    """RES 7,[HL]"""
    mmu.set_memory(R.HL, RES_U3R8(mmu.get_memory(R.HL), 7))


def RES_CBBF():
    """RES 7,A"""
    R.A = RES_U3R8(R.A, 7)


def SET_U3R8(register, value):
    initial = register
    higher = ((initial >> value) | 1) << value
    lower = ((initial << 8 - value) & 0xFF) >> 8 - value
    calc = higher | lower
    return calc


def SET_CBC0():
    """SET 0,B"""
    R.B = SET_U3R8(R.B, 0)


def SET_CBC1():
    """SET 0,C"""
    R.C = SET_U3R8(R.C, 0)


def SET_CBC2():
    """SET 0,D"""
    R.D = SET_U3R8(R.D, 0)


def SET_CBC3():
    """SET 0,E"""
    R.E = SET_U3R8(R.E, 0)


def SET_CBC4():
    """SET 0,H"""
    R.H = SET_U3R8(R.H, 0)


def SET_CBC5():
    """SET 0,L"""
    R.L = SET_U3R8(R.L, 0)


def SET_CBC6():
    """SET 0,[HL]"""
    mmu.set_memory(R.HL, SET_U3R8(mmu.get_memory(R.HL), 0))


def SET_CBC7():
    """SET 0,A"""
    R.A = SET_U3R8(R.A, 0)


def SET_CBC8():
    """SET 1,B"""
    R.B = SET_U3R8(R.B, 1)


def SET_CBC9():
    """SET 1,C"""
    R.C = SET_U3R8(R.C, 1)


def SET_CBCA():
    """SET 1,D"""
    R.D = SET_U3R8(R.D, 1)


def SET_CBCB():
    """SET 1,E"""
    R.E = SET_U3R8(R.E, 1)


def SET_CBCC():
    """SET 1,H"""
    R.H = SET_U3R8(R.H, 1)


def SET_CBCD():
    """SET 1,L"""
    R.L = SET_U3R8(R.L, 1)


def SET_CBCE():
    """SET 1,[HL]"""
    mmu.set_memory(R.HL, SET_U3R8(mmu.get_memory(R.HL), 1))


def SET_CBCF():
    """SET 1,A"""
    R.A = SET_U3R8(R.A, 1)


def SET_CBD0():
    """SET 2,B"""
    R.B = SET_U3R8(R.B, 2)


def SET_CBD1():
    """SET 2,C"""
    R.C = SET_U3R8(R.C, 2)


def SET_CBD2():
    """SET 2,D"""
    R.D = SET_U3R8(R.D, 2)


def SET_CBD3():
    """SET 2,E"""
    R.E = SET_U3R8(R.E, 2)


def SET_CBD4():
    """SET 2,H"""
    R.H = SET_U3R8(R.H, 2)


def SET_CBD5():
    """SET 2,L"""
    R.L = SET_U3R8(R.L, 2)


def SET_CBD6():
    """SET 2,[HL]"""
    mmu.set_memory(R.HL, SET_U3R8(mmu.get_memory(R.HL), 2))


def SET_CBD7():
    """SET 2,A"""
    R.A = SET_U3R8(R.A, 2)


def SET_CBD8():
    """SET 3,B"""
    R.B = SET_U3R8(R.B, 3)


def SET_CBD9():
    """SET 3,C"""
    R.C = SET_U3R8(R.C, 3)


def SET_CBDA():
    """SET 3,D"""
    R.D = SET_U3R8(R.D, 3)


def SET_CBDB():
    """SET 3,E"""
    R.E = SET_U3R8(R.E, 3)


def SET_CBDC():
    """SET 3,H"""
    R.H = SET_U3R8(R.H, 3)


def SET_CBDD():
    """SET 3,L"""
    R.L = SET_U3R8(R.L, 3)


def SET_CBDE():
    """SET 3,[HL]"""
    mmu.set_memory(R.HL, SET_U3R8(mmu.get_memory(R.HL), 3))


def SET_CBDF():
    """SET 3,A"""
    R.A = SET_U3R8(R.A, 3)


def SET_CBE0():
    """SET 4,B"""
    R.B = SET_U3R8(R.B, 4)


def SET_CBE1():
    """SET 4,C"""
    R.C = SET_U3R8(R.C, 4)


def SET_CBE2():
    """SET 4,D"""
    R.D = SET_U3R8(R.D, 4)


def SET_CBE3():
    """SET 4,E"""
    R.E = SET_U3R8(R.E, 4)


def SET_CBE4():
    """SET 4,H"""
    R.H = SET_U3R8(R.H, 4)


def SET_CBE5():
    """SET 4,L"""
    R.L = SET_U3R8(R.L, 4)


def SET_CBE6():
    """SET 4,[HL]"""
    mmu.set_memory(R.HL, SET_U3R8(mmu.get_memory(R.HL), 4))


def SET_CBE7():
    """SET 4,A"""
    R.A = SET_U3R8(R.A, 4)


def SET_CBE8():
    """SET 5,B"""
    R.B = SET_U3R8(R.B, 5)


def SET_CBE9():
    """SET 5,C"""
    R.C = SET_U3R8(R.C, 5)


def SET_CBEA():
    """SET 5,D"""
    R.D = SET_U3R8(R.D, 5)


def SET_CBEB():
    """SET 5,E"""
    R.E = SET_U3R8(R.E, 5)


def SET_CBEC():
    """SET 5,H"""
    R.H = SET_U3R8(R.H, 5)


def SET_CBED():
    """SET 5,L"""
    R.L = SET_U3R8(R.L, 5)


def SET_CBEE():
    """SET 5,[HL]"""
    mmu.set_memory(R.HL, SET_U3R8(mmu.get_memory(R.HL), 5))


def SET_CBEF():
    """SET 5,A"""
    R.A = SET_U3R8(R.A, 5)


def SET_CBF0():
    """SET 6,B"""
    R.B = SET_U3R8(R.B, 6)


def SET_CBF1():
    """SET 6,C"""
    R.C = SET_U3R8(R.C, 6)


def SET_CBF2():
    """SET 6,D"""
    R.D = SET_U3R8(R.D, 6)


def SET_CBF3():
    """SET 6,E"""
    R.E = SET_U3R8(R.E, 6)


def SET_CBF4():
    """SET 6,H"""
    R.H = SET_U3R8(R.H, 6)


def SET_CBF5():
    """SET 6,L"""
    R.L = SET_U3R8(R.L, 6)


def SET_CBF6():
    """SET 6,[HL]"""
    mmu.set_memory(R.HL, SET_U3R8(mmu.get_memory(R.HL), 6))


def SET_CBF7():
    """SET 6,A"""
    R.A = SET_U3R8(R.A, 6)


def SET_CBF8():
    """SET 7,B"""
    R.B = SET_U3R8(R.B, 7)


def SET_CBF9():
    """SET 7,C"""
    R.C = SET_U3R8(R.C, 7)


def SET_CBFA():
    """SET 7,D"""
    R.D = SET_U3R8(R.D, 7)


def SET_CBFB():
    """SET 7,E"""
    R.E = SET_U3R8(R.E, 7)


def SET_CBFC():
    """SET 7,H"""
    R.H = SET_U3R8(R.H, 7)


def SET_CBFD():
    """SET 7,L"""
    R.L = SET_U3R8(R.L, 7)


def SET_CBFE():
    """SET 7,[HL]"""
    mmu.set_memory(R.HL, SET_U3R8(mmu.get_memory(R.HL), 7))


def SET_CBFF():
    """SET 7,A"""
    R.A = SET_U3R8(R.A, 7)


def CALL_CC(value):
    """CALL Z,n16"""
    if R.ZERO == 1:
        R.PUSH(R.PC)
        JP_C3(value)


def CALL_CD(value):
    """CALL n16"""
    R.PUSH(R.PC)
    # NOTE: Must ensure PC is currently the address after CALL
    JP_C3(value)


def ADC_CE(value):
    """ADC A,n8"""
    ADC_A_N8(value)


def RET_D0():
    """RET NC"""
    if R.CARRY == 0:
        JP_C3(R.POP())


def POP_D1():
    """POP DE"""
    R.DE = R.POP()


def JP_D2(value):
    """JP NC,n16"""
    if R.CARRY == 0:
        R.PC = value


def CALL_D4(value):
    """CALL NC,n16"""
    if R.CARRY == 0:
        R.PUSH(R.PC)
        JP_C3(value)


def PUSH_D5():
    """PUSH DE"""
    R.PUSH(R.DE)


def SUB_D6(value):
    """SUB A,n8"""
    SUB_A_N8(value)


def RET_D8():
    """RET C"""
    if R.CARRY == 1:
        JP_C3(R.POP())


def JP_DA(value):
    """JP C,n16"""
    if R.CARRY == 1:
        R.PC = value


def CALL_DC(value):
    """CALL C,n16"""
    if R.CARRY == 1:
        R.PUSH(R.PC)
        JP_C3(value)


def SBC_DE(value):
    """SBC A,n8"""
    SBC_A_N8(value)


def LDH_E0(value):
    """LDH [n8],A"""
    mmu.set_memory(0xFF00 + value, R.A)


def POP_E1():
    """POP HL"""
    R.HL = R.POP()


def LDH_E2():
    """LDH [C],A"""
    mmu.set_memory(0xFF00 + R.C, R.A)


def PUSH_E5():
    """PUSH HL"""
    R.PUSH(R.HL)


def AND_E6(value):
    """AND A,n8"""
    AND_A_N8(value)


def JP_E9():
    """JP HL"""
    R.PC = R.HL


def LD_EA(value: int):
    """LD [n16],A"""
    mmu.set_memory(value, R.A)


def XOR_EE(value):
    """XOR A,n8"""
    XOR_A_N8(value)


def LDH_F0(value):
    """LDH A,[n8]"""
    R.A = mmu.get_memory(0xFF00 + value)


def POP_F1():
    """POP AF"""
    R.AF = R.POP()


def LDH_F2():
    """LDH A,[C]"""
    R.A = mmu.get_memory(0xFF00 + R.C)


def DI_F3():
    """DI"""
    global IME
    IME = False


def PUSH_F5():
    """PUSH AF"""
    R.PUSH(R.AF)


def OR_F6(value):
    """OR A,n8"""
    OR_A_N8(value)


def EI_FB():
    """EI"""
    global IME
    IME = True


def CP_FE(value):
    """CP A,n8"""
    CP_A_N8(value)


# endregion

# region DEBUG
opTimes = 0
ppuTimes = 0
allTimes = 0
# endregion

# region CPU Logic

clear_display()

try:
    while R.PC < len(mmu.RAM):
        # region DEBUG
        allTime = time.time() * 1000
        # endregion

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mmu.dump()
                pygame.quit()
                sys.exit()

        # region DEBUG
        opTime = time.time() * 1000
        # endregion

        if R.PC >= 0x104 and R.PC < 0x150:
            # TODO CARTRIDGE HEADER
            R.INCREMENT_PC(1)
            continue

        # region DEBUG
        R.debug()
        # endregion

        # region I hate all of this
        data = mmu.get_memory(R.PC)
        if data == 0xCB:
            data = mmu.get_memory(R.PC + 1)
            opcode = opcodes["cbprefixed"][helpers.int_to_hex(data)]
            R.INCREMENT_PC(opcode["bytes"])  # ??? don't add +1

            # region DEBUG
            print(
                helpers.int_to_hex(R.PC),
                helpers.int_to_hex(data),
                opcode["mnemonic"],
                [helpers.int_to_hex(c) for c in got_data],
            )
            # endregion

            match data:
                case 0x11:
                    RL_CB11()
                case 0x40:
                    BIT_CB40()
                case 0x41:
                    BIT_CB41()
                case 0x42:
                    BIT_CB42()
                case 0x43:
                    BIT_CB43()
                case 0x44:
                    BIT_CB44()
                case 0x45:
                    BIT_CB45()
                case 0x46:
                    BIT_CB46()
                case 0x47:
                    BIT_CB47()
                case 0x48:
                    BIT_CB48()
                case 0x49:
                    BIT_CB49()
                case 0x4A:
                    BIT_CB4A()
                case 0x4B:
                    BIT_CB4B()
                case 0x4C:
                    BIT_CB4C()
                case 0x4D:
                    BIT_CB4D()
                case 0x4E:
                    BIT_CB4E()
                case 0x4F:
                    BIT_CB4F()
                case 0x50:
                    BIT_CB50()
                case 0x51:
                    BIT_CB51()
                case 0x52:
                    BIT_CB52()
                case 0x53:
                    BIT_CB53()
                case 0x54:
                    BIT_CB54()
                case 0x55:
                    BIT_CB55()
                case 0x56:
                    BIT_CB56()
                case 0x57:
                    BIT_CB57()
                case 0x58:
                    BIT_CB58()
                case 0x59:
                    BIT_CB59()
                case 0x5A:
                    BIT_CB5A()
                case 0x5B:
                    BIT_CB5B()
                case 0x5C:
                    BIT_CB5C()
                case 0x5D:
                    BIT_CB5D()
                case 0x5E:
                    BIT_CB5E()
                case 0x5F:
                    BIT_CB5F()
                case 0x60:
                    BIT_CB60()
                case 0x61:
                    BIT_CB61()
                case 0x62:
                    BIT_CB62()
                case 0x63:
                    BIT_CB63()
                case 0x64:
                    BIT_CB64()
                case 0x65:
                    BIT_CB65()
                case 0x66:
                    BIT_CB66()
                case 0x67:
                    BIT_CB67()
                case 0x68:
                    BIT_CB68()
                case 0x69:
                    BIT_CB69()
                case 0x6A:
                    BIT_CB6A()
                case 0x6B:
                    BIT_CB6B()
                case 0x6C:
                    BIT_CB6C()
                case 0x6D:
                    BIT_CB6D()
                case 0x6E:
                    BIT_CB6E()
                case 0x6F:
                    BIT_CB6F()
                case 0x70:
                    BIT_CB70()
                case 0x71:
                    BIT_CB71()
                case 0x72:
                    BIT_CB72()
                case 0x73:
                    BIT_CB73()
                case 0x74:
                    BIT_CB74()
                case 0x75:
                    BIT_CB75()
                case 0x76:
                    BIT_CB76()
                case 0x77:
                    BIT_CB77()
                case 0x78:
                    BIT_CB78()
                case 0x79:
                    BIT_CB79()
                case 0x7A:
                    BIT_CB7A()
                case 0x7B:
                    BIT_CB7B()
                case 0x7C:
                    BIT_CB7C()
                case 0x7D:
                    BIT_CB7D()
                case 0x7E:
                    BIT_CB7E()
                case 0x7F:
                    BIT_CB7F()
                case _:
                    raise Exception(f"Unknown Instruction: {helpers.int_to_hex(data)}")

            mmu.IO.LCD.tick()

            continue

        opcode = opcodes["unprefixed"][helpers.int_to_hex(data)]
        # TODO what the fuck is this
        got_data = [
            int.from_bytes(
                bytes(mmu.RAM[R.PC + 1 : R.PC + 1 + int(operand["bytes"])]), "little"
            )
            for operand in opcode["operands"]
            if "bytes" in operand
        ]

        # region DEBUG
        print(
            helpers.int_to_hex(R.PC),
            helpers.int_to_hex(data),
            opcode["mnemonic"],
            [helpers.int_to_hex(c) for c in got_data],
        )
        # endregion

        R.INCREMENT_PC(opcode["bytes"])
        match data:
            case 0x00:
                NOP_00()
            case 0x01:
                LD_01(got_data[0])
            case 0x02:
                LD_02()
            case 0x03:
                INC_03()
            case 0x04:
                INC_04()
            case 0x05:
                DEC_05()
            case 0x06:
                LD_06(got_data[0])
            case 0x07:
                RLCA_07()
            case 0x0A:
                LD_0A()
            case 0x0B:
                DEC_0B()
            case 0x0C:
                INC_0C()
            case 0x0D:
                DEC_0D()
            case 0x0E:
                LD_0E(got_data[0])
            case 0x0F:
                RRCA_0F()
            case 0x11:
                LD_11(got_data[0])
            case 0x12:
                LD_12()
            case 0x13:
                INC_13()
            case 0x14:
                INC_14()
            case 0x15:
                DEC_15()
            case 0x16:
                LD_16(got_data[0])
            case 0x17:
                RLA_17()
            case 0x18:
                JR_18(got_data[0])
            case 0x19:
                ADD_19()
            case 0x1A:
                LD_1A()
            case 0x1B:
                DEC_1B()
            case 0x1C:
                INC_1C()
            case 0x1D:
                DEC_1D()
            case 0x1E:
                LD_1E(got_data[0])
            case 0x1F:
                RRA_1F(got_data[0])
            case 0x20:
                JR_20(got_data[0])
            case 0x21:
                LD_21(got_data[0])
            case 0x22:
                LD_22()
            case 0x23:
                INC_23()
            case 0x24:
                INC_24()
            case 0x25:
                DEC_25()
            case 0x26:
                LD_26(got_data[0])
            case 0x28:
                JR_28(got_data[0])
            case 0x29:
                ADD_29()
            case 0x2A:
                LD_2A()
            case 0x2B:
                DEC_2B()
            case 0x2C:
                INC_2C()
            case 0x2D:
                DEC_2D()
            case 0x2E:
                LD_2E(got_data[0])
            case 0x2F:
                CPL_2F()
            case 0x30:
                JR_30(got_data[0])
            case 0x31:
                LD_31(got_data[0])
            case 0x32:
                LD_32()
            case 0x33:
                INC_33()
            case 0x34:
                INC_34()
            case 0x35:
                DEC_35()
            case 0x36:
                LD_36(got_data[0])
            case 0x37:
                SCF_37()
            case 0x38:
                JR_38(got_data[0])
            case 0x39:
                ADD_39()
            case 0x3A:
                LD_3A()
            case 0x3B:
                DEC_3B()
            case 0x3C:
                INC_3C()
            case 0x3D:
                DEC_3D()
            case 0x3E:
                LD_3E(got_data[0])
            case 0x3F:
                CCF_3F()
            case 0x40:
                LD_40()
            case 0x41:
                LD_41()
            case 0x42:
                LD_42()
            case 0x43:
                LD_43()
            case 0x44:
                LD_44()
            case 0x45:
                LD_45()
            case 0x46:
                LD_46()
            case 0x47:
                LD_47()
            case 0x48:
                LD_48()
            case 0x49:
                LD_49()
            case 0x4A:
                LD_4A()
            case 0x4B:
                LD_4B()
            case 0x4C:
                LD_4C()
            case 0x4D:
                LD_4D()
            case 0x4E:
                LD_4E()
            case 0x4F:
                LD_4F()
            case 0x50:
                LD_50()
            case 0x51:
                LD_51()
            case 0x52:
                LD_52()
            case 0x53:
                LD_53()
            case 0x54:
                LD_54()
            case 0x55:
                LD_55()
            case 0x56:
                LD_56()
            case 0x57:
                LD_57()
            case 0x58:
                LD_58()
            case 0x59:
                LD_59()
            case 0x5A:
                LD_5A()
            case 0x5B:
                LD_5B()
            case 0x5C:
                LD_5C()
            case 0x5D:
                LD_5D()
            case 0x5E:
                LD_5E()
            case 0x5F:
                LD_5F()
            case 0x60:
                LD_60()
            case 0x61:
                LD_61()
            case 0x62:
                LD_62()
            case 0x63:
                LD_63()
            case 0x64:
                LD_64()
            case 0x65:
                LD_65()
            case 0x66:
                LD_66()
            case 0x67:
                LD_67()
            case 0x68:
                LD_68()
            case 0x69:
                LD_69()
            case 0x6A:
                LD_6A()
            case 0x6B:
                LD_6B()
            case 0x6C:
                LD_6C()
            case 0x6D:
                LD_6D()
            case 0x6E:
                LD_6E()
            case 0x6F:
                LD_6F()
            case 0x70:
                LD_70()
            case 0x71:
                LD_71()
            case 0x72:
                LD_72()
            case 0x73:
                LD_73()
            case 0x74:
                LD_74()
            case 0x75:
                LD_75()
            case 0x76:
                HALT_76()
            case 0x77:
                LD_77()
            case 0x78:
                LD_78()
            case 0x79:
                LD_79()
            case 0x7A:
                LD_7A()
            case 0x7B:
                LD_7B()
            case 0x7C:
                LD_7C()
            case 0x7D:
                LD_7D()
            case 0x7E:
                LD_7E()
            case 0x7F:
                LD_7F()
            case 0x80:
                ADD_80()
            case 0x81:
                ADD_81()
            case 0x82:
                ADD_82()
            case 0x83:
                ADD_83()
            case 0x84:
                ADD_84()
            case 0x85:
                ADD_85()
            case 0x86:
                ADD_86()
            case 0x87:
                ADD_87()
            case 0x88:
                ADC_88()
            case 0x89:
                ADC_89()
            case 0x8A:
                ADC_8A()
            case 0x8B:
                ADC_8B()
            case 0x8C:
                ADC_8C()
            case 0x8D:
                ADC_8D()
            case 0x8E:
                ADC_8E()
            case 0x8F:
                ADC_8F()
            case 0x90:
                SUB_90()
            case 0x91:
                SUB_91()
            case 0x92:
                SUB_92()
            case 0x93:
                SUB_93()
            case 0x94:
                SUB_94()
            case 0x95:
                SUB_95()
            case 0x96:
                SUB_96()
            case 0x97:
                SUB_97()
            case 0x98:
                SBC_98()
            case 0x99:
                SBC_99()
            case 0x9A:
                SBC_9A()
            case 0x9B:
                SBC_9B()
            case 0x9C:
                SBC_9C()
            case 0x9D:
                SBC_9D()
            case 0x9E:
                SBC_9E()
            case 0x9F:
                SBC_9F()
            case 0xA0:
                AND_A0()
            case 0xA1:
                AND_A1()
            case 0xA2:
                AND_A2()
            case 0xA3:
                AND_A3()
            case 0xA4:
                AND_A4()
            case 0xA5:
                AND_A5()
            case 0xA6:
                AND_A6()
            case 0xA7:
                AND_A7()
            case 0xA8:
                XOR_A8()
            case 0xA9:
                XOR_A9()
            case 0xAA:
                XOR_AA()
            case 0xAB:
                XOR_AB()
            case 0xAC:
                XOR_AC()
            case 0xAD:
                XOR_AD()
            case 0xAE:
                XOR_AE()
            case 0xAF:
                XOR_AF()
            case 0xB0:
                OR_B0()
            case 0xB1:
                OR_B1()
            case 0xB2:
                OR_B2()
            case 0xB3:
                OR_B3()
            case 0xB4:
                OR_B4()
            case 0xB5:
                OR_B5()
            case 0xB6:
                OR_B6()
            case 0xB7:
                OR_B7()
            case 0xB8:
                CP_B8()
            case 0xB9:
                CP_B9()
            case 0xBA:
                CP_BA()
            case 0xBB:
                CP_BB()
            case 0xBC:
                CP_BC()
            case 0xBD:
                CP_BD()
            case 0xBE:
                CP_BE()
            case 0xBF:
                CP_BF()
            case 0xC0:
                RET_C0()
            case 0xC1:
                POP_C1()
            case 0xC2:
                JP_C2(got_data[0])
            case 0xC3:
                JP_C3(got_data[0])
            case 0xC4:
                CALL_C4(got_data[0])
            case 0xC5:
                PUSH_C5()
            case 0xC8:
                RET_C8()
            case 0xC9:
                RET_C9()
            case 0xCA:
                JP_CA(got_data[0])
            case 0xCC:
                CALL_CC(got_data[0])
            case 0xCD:
                CALL_CD(got_data[0])
            case 0xD0:
                RET_D0()
            case 0xD1:
                POP_D1()
            case 0xD4:
                CALL_D4(got_data[0])
            case 0xD5:
                PUSH_D5()
            case 0xD8:
                RET_D8()
            case 0xDC:
                CALL_DC(got_data[0])
            case 0xE0:
                LDH_E0(got_data[0])
            case 0xE1:
                POP_E1()
            case 0xE2:
                LDH_E2()
            case 0xE5:
                PUSH_E5()
            case 0xEA:
                LD_EA(got_data[0])
            case 0xF0:
                LDH_F0(got_data[0])
            case 0xF1:
                POP_F1()
            case 0xF2:
                LDH_F2()
            case 0xF3:
                DI_F3()
            case 0xF5:
                PUSH_F5()
            case 0xF6:
                OR_F6(got_data[0])
            case 0xFB:
                EI_FB()
            case 0xFE:
                CP_FE(got_data[0])
            case _:
                raise Exception(f"Unknown Instruction: {helpers.int_to_hex(data)}")

        # endregion

        # region DEBUG
        opTime = (time.time() * 1000) - opTime
        opTimes += opTime

        ppuTime = time.time() * 1000
        # endregion

        mmu.IO.LCD.tick()

        # region DEBUG
        ppuTime = (time.time() * 1000) - ppuTime
        ppuTimes += ppuTime

        allTime = (time.time() * 1000) - allTime
        allTimes += allTime
        print({"op": opTimes, "ppu": ppuTimes, "all": allTimes})
        # endregion

except Exception as e:
    traceback.print_exception(e)
    print("Exiting...")
    mmu.dump()

# endregion
