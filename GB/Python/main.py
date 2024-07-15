import time
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
                )
            # endregion

            opcodes.execute_cb(PC_DATA)

            mmu.IO.LCD.tick()

            continue

        opinfo = opcodes.opinfo["unprefixed"][helpers.int_to_hex(PC_DATA)]
        # TODO what the fuck is this
        opBytes = [
            c
            for c in [operand.get("bytes", None) for operand in opinfo["operands"]]
            if c is not None
        ]
        opData = (
            int.from_bytes(
                bytes([mmu.get_memory(R.PC + i) for i in range(1, opBytes[0] + 1)]),
                "little",
            )
            if len(opBytes) > 0
            else None
        )

        # region DEBUG
        if SIMPLE_DEBUG:
            print(
                helpers.int_to_hex(R.PC),
                helpers.int_to_hex(PC_DATA),
                opinfo["mnemonic"],
                [
                    helpers.int_to_hex(opData) if c.get("bytes") else c["name"]
                    for c in opinfo["operands"]
                ],
            )
        # endregion

        R.INCREMENT_PC(opinfo["bytes"])
        opcodes.execute(PC_DATA, opData)
        # endregion

        mmu.IO.LCD.tick()

except Exception as e:
    traceback.print_exception(e)
    mmu.dump()
    print("Exiting...")

# endregion
