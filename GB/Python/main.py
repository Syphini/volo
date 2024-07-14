import time
import traceback
import helpers
from mmu import MMU
from registers import Registers
from opcodes import Opcodes

print()

DEBUG = False
SIMPLE_DEBUG = False

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

# region CPU Logic

try:
    while R.PC < len(mmu.RAM):
        # region DEBUG
        if DEBUG:
            allTime = time.time() * 1000
        # endregion

        # region DEBUG
        if DEBUG:
            opTime = time.time() * 1000
        # endregion

        if R.PC >= 0x104 and R.PC < 0x150:
            # TODO CARTRIDGE HEADER
            R.INCREMENT_PC(1)
            continue

        # region DEBUG
        if DEBUG:
            R.debug()
        # endregion

        # region I hate all of this
        PC_DATA = mmu.get_memory(R.PC)
        if PC_DATA == 0xCB:
            PC_DATA = mmu.get_memory(R.PC + 1)
            opinfo = opcodes.opinfo["cbprefixed"][helpers.int_to_hex(PC_DATA)]
            R.INCREMENT_PC(opinfo["bytes"])  # ??? don't add +1

            # region DEBUG
            if SIMPLE_DEBUG:
                print(
                    helpers.int_to_hex(R.PC),
                    helpers.int_to_hex(PC_DATA),
                    opinfo["mnemonic"],
                    [helpers.int_to_hex(c) for c in got_data],
                )
            # endregion

            opcodes.execute_cb(PC_DATA)

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
        if SIMPLE_DEBUG:
            print(
                helpers.int_to_hex(R.PC),
                helpers.int_to_hex(PC_DATA),
                opinfo["mnemonic"],
                [c["name"] for c in opinfo["operands"]],
                [helpers.int_to_hex(c) for c in got_data],
            )
        # endregion

        R.INCREMENT_PC(opinfo["bytes"])
        opcodes.execute(PC_DATA, got_data[0] if len(got_data) > 0 else None)
        # endregion

        mmu.IO.LCD.tick()

except Exception as e:
    traceback.print_exception(e)
    mmu.dump()
    print("Exiting...")

# endregion
