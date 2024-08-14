from collections import namedtuple
import struct


class Cartridge:
    def __init__(self, rom_path: str) -> None:

        self.MEMORY_BANKS = []

        with open(rom_path, "rb") as f:
            while data := f.read(0x4000):
                self.MEMORY_BANKS.append(bytearray(data))

        self.MBC_COUNT = len(self.MEMORY_BANKS)

        self.RAM_ENABLE = False
        # self.RAM_BANKS = []

        # Read Cartridge Header
        header_raw = self.MEMORY_BANKS[0][0x100:0x150]
        header_unpacked = struct.unpack("=xxxx48x15sBHBBBBBBBBH", header_raw)

        # FIXME this won't compile properly
        CartridgeHeader = namedtuple(
            "CartridgeHeader",
            "title cgb new_licensee_code sgb cartridge_type rom_size ram_size destination_code old_licensee_code mask_rom_version header_checksum global_checksum",
        )
        self.HEADER = CartridgeHeader(*header_unpacked)

    def toggle_ram_enable(self, value: int) -> None:
        if (value & 0xF) == 0xA:
            self.RAM_ENABLE = True
        else:
            self.RAM_ENABLE = False
