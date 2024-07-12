import sys
import pygame
import time
import traceback
import helpers
from mmu import MMU
from registers import Registers
from opcodes import Opcodes

print()

ROM_FILE = "GB/ROM/DMG_ROM.bin"

# region Registers

mmu = MMU()
R = Registers(mmu)
opcodes = Opcodes(mmu, R)

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
        PC_DATA = mmu.get_memory(R.PC)
        if PC_DATA == 0xCB:
            PC_DATA = mmu.get_memory(R.PC + 1)
            opinfo = opcodes.opinfo["cbprefixed"][helpers.int_to_hex(PC_DATA)]
            R.INCREMENT_PC(opinfo["bytes"])  # ??? don't add +1

            # region DEBUG
            print(
                helpers.int_to_hex(R.PC),
                helpers.int_to_hex(PC_DATA),
                opinfo["mnemonic"],
                [helpers.int_to_hex(c) for c in got_data],
            )
            # endregion

            opcodes.execute_cb(PC_DATA, got_data[0] if len(got_data) > 0 else None)

            mmu.IO.LCD.tick()

            continue

        opinfo = opcodes.opinfo["unprefixed"][helpers.int_to_hex(PC_DATA)]
        # TODO what the fuck is this
        got_data = [
            int.from_bytes(
                bytes(mmu.RAM[R.PC + 1 : R.PC + 1 + int(operand["bytes"])]), "little"
            )
            for operand in opinfo["operands"]
            if "bytes" in operand
        ]

        # region DEBUG
        print(
            helpers.int_to_hex(R.PC),
            helpers.int_to_hex(PC_DATA),
            opinfo["mnemonic"],
            [helpers.int_to_hex(c) for c in got_data],
        )
        # endregion

        R.INCREMENT_PC(opinfo["bytes"])
        opcodes.execute(PC_DATA, got_data[0] if len(got_data) > 0 else None)
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
