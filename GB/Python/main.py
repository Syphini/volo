import cProfile
import pstats
import traceback
import sys
import pygame
import helpers
from cartridge import Cartridge
from mmu import MMU
from registers import Registers
from opcodes import Opcodes

print()

OP_DEBUG = False
PROFILE_DEBUG = True

if PROFILE_DEBUG:
    profiler = cProfile.Profile()
    profiler.enable()

ROM_FILE = "GB/ROM/cpu_instrs.gb"

# region Registers

cartridge = Cartridge(ROM_FILE)
mmu = MMU(cartridge, use_boot_rom=True)
R = Registers(mmu)
opcodes = Opcodes(mmu, R)

# endregion


def dump(exception=None):
    print("------")
    R.debug()
    print("------")
    if exception:
        traceback.print_exception(exception)
    mmu.dump()

    if PROFILE_DEBUG:
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats("ncalls")
        stats.print_stats()


lastTime = 0

# region CPU Logic
try:
    while True:
        if pygame.time.get_ticks() - lastTime >= 1000:
            print(f"CYCLES: {mmu.IO.LCD.CYCLE_COUNTER}")
            lastTime = pygame.time.get_ticks()
            mmu.IO.LCD.CYCLE_COUNTER = 0

        # region Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dump()
                pygame.quit()
                print("Closed App")
                sys.exit()
            mmu.IO.JOYP.handle_event(event)
        # endregion

        # region Interrupts

        if mmu.IME:
            if mmu.IO.IF.VBLANK == 1 and mmu.IO.IE.VBLANK == 1:
                mmu.IME = False
                mmu.IO.IF.VBLANK = 0
                opcodes.CALL_CD(0x40)
                mmu.IO._TIMER.tick(20)
                mmu.IO.LCD.tick(20)
                mmu.HALT = False
            elif mmu.IO.IF.LCD == 1 and mmu.IO.IE.LCD == 1:
                mmu.IME = False
                mmu.IO.IF.LCD = 0
                opcodes.CALL_CD(0x48)
                mmu.IO._TIMER.tick(20)
                mmu.IO.LCD.tick(20)
                mmu.HALT = False
            elif mmu.IO.IF.TIMER == 1 and mmu.IO.IE.TIMER == 1:
                mmu.IME = False
                mmu.IO.IF.TIMER = 0
                opcodes.CALL_CD(0x50)
                mmu.IO._TIMER.tick(20)
                mmu.IO.LCD.tick(20)
                mmu.HALT = False
            elif mmu.IO.IF.SERIAL == 1 and mmu.IO.IE.SERIAL == 1:
                mmu.IME = False
                mmu.IO.IF.SERIAL = 0
                opcodes.CALL_CD(0x58)
                mmu.IO._TIMER.tick(20)
                mmu.IO.LCD.tick(20)
                mmu.HALT = False
            elif mmu.IO.IF.JOYPAD == 1 and mmu.IO.IE.JOYPAD == 1:
                mmu.IME = False
                mmu.IO.IF.JOYPAD = 0
                opcodes.CALL_CD(0x60)
                mmu.IO._TIMER.tick(20)
                mmu.IO.LCD.tick(20)
                mmu.HALT = False

        # endregion

        if mmu.HALT:
            if mmu.IO.IF.get() & mmu.IO.IE.get() == 0:
                mmu.IO._TIMER.tick(4)
                mmu.IO.LCD.tick(4)
                continue
            else:
                mmu.HALT = False

        PC_DATA = mmu.get_memory(R.PC)

        CB_FLAG = False
        if PC_DATA == 0xCB:
            CB_FLAG = True
            PC_DATA = mmu.get_memory(R.PC + 1)
            R.PC += 1

        # region DEBUG
        if OP_DEBUG:
            print(
                helpers.formatted_hex(R.PC),
                helpers.formatted_hex(PC_DATA + 0xCB00 if CB_FLAG else PC_DATA),
            )
            R.debug()
        # endregion

        cycles = opcodes.execute(PC_DATA, CB_FLAG)
        mmu.IO.tick(cycles)
        mmu.IO.LCD.CYCLE_COUNTER += 1


# endregion

except Exception as e:
    dump(e)
    print("Exiting...")
