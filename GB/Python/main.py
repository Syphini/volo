import traceback
import helpers
from mmu import MMU
from registers import Registers
from opcodes import Opcodes

print()

DEBUG = False

ROM_FILE = "GB/ROM/DMG_ROM.bin"

# region Registers

mmu = MMU()
R = Registers(mmu)
opcodes = Opcodes(mmu, R)

# endregion

with open(ROM_FILE, "rb") as f:
    for cycle_count, b in enumerate(f.read()):
        mmu.set_memory(cycle_count, b)

# region CPU Logic
try:
    while True:
        if R.PC >= 0x104 and R.PC < 0x150:
            # TODO CARTRIDGE HEADER
            R.INCREMENT_PC(1)
            continue

        PC_DATA = mmu.get_memory(R.PC)

        CB_FLAG = False
        if PC_DATA == 0xCB:
            CB_FLAG = True
            PC_DATA = mmu.get_memory(R.PC + 1)
            R.INCREMENT_PC(1)

        # region DEBUG
        if DEBUG:
            print(
                helpers.formatted_hex(R.PC),
                helpers.formatted_hex(PC_DATA + 0xCB00 if CB_FLAG else PC_DATA),
            )
            R.debug()
        # endregion

        cycles = opcodes.execute(PC_DATA, CB_FLAG)
        mmu.IO.LCD.tick(cycles)

# endregion

except Exception as e:
    print("------")
    R.debug()
    print("------")
    traceback.print_exception(e)
    mmu.dump()
    print("Exiting...")
