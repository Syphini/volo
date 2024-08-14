import argparse
import cProfile
import pstats
import traceback
import sys
import os
import typing
import pygame
from pyvologb.helpers import formatted_hex
from pyvologb.cartridge import Cartridge
from pyvologb.mmu import MMU
from pyvologb.registers import Registers
from pyvologb.opcodes import Opcodes


def main() -> None:
    print()

    def parse_args(args: typing.List[str]) -> argparse.Namespace:
        parser = argparse.ArgumentParser()
        parser.add_argument("rom")
        parser.add_argument("-s", "--skip-boot", action="store_true", default=False)
        parser.add_argument("-m", "--mem-dump", action="store_true", default=False)
        parser.add_argument("-d", "--debug", action="store_true", default=False)
        return parser.parse_args(args)

    args = parse_args(sys.argv[1:])

    ROM_PATH = os.path.abspath(args.rom)
    if not os.path.exists(ROM_PATH):
        print(f'ROM does not exist at "{ROM_PATH}"')
        sys.exit()

    OP_DEBUG = False

    if args.debug:
        profiler = cProfile.Profile()
        profiler.enable()

    # region Registers

    cartridge = Cartridge(ROM_PATH)
    mmu = MMU(cartridge, use_boot_rom=(not args.skip_boot))
    R = Registers(mmu)
    opcodes = Opcodes(mmu, R)

    # endregion

    def debug(exception: Exception | None = None) -> None:
        if args.debug:
            print("------")
            R.debug()
            print("------")

            if not exception:
                profiler.disable()
                stats = pstats.Stats(profiler).sort_stats("ncalls")
                stats.print_stats()

        if exception:
            traceback.print_exception(exception)

    def dump() -> None:
        if args.mem_dump:
            mmu.dump()

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
                    debug()
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

            if PC_DATA == 0xCB:
                PC_DATA = mmu.get_memory(R.PC + 1) + 0x100
                R.PC += 1

            # region DEBUG
            if OP_DEBUG:
                print(
                    formatted_hex(R.PC),
                    formatted_hex(PC_DATA),
                )
                R.debug()
            # endregion

            cycles = opcodes.execute(PC_DATA)
            mmu.IO.tick(cycles)
            mmu.IO.LCD.CYCLE_COUNTER += 1

    # endregion

    except Exception as e:
        debug(e)
        dump()
        print("Exiting...")


if __name__ == "__main__":
    main()
