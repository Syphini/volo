from collections import namedtuple
import struct


class Cartridge:
    def __init__(self, rom_path):

        self.MEMORY_BANKS = []

        with open(rom_path, "rb") as f:
            while data := f.read(0x4000):
                self.MEMORY_BANKS.append(bytearray(data))

        # Read Cartridge Header
        header_raw = self.MEMORY_BANKS[0][0x100:0x150]
        header_unpacked = struct.unpack("=xxxx48x15sBHBBBBBBBBH", header_raw)
        self.HEADER = namedtuple(
            "CartridgeHeader",
            "title cgb new_licensee_code sgb cartridge_type rom_size ram_size destination_code old_licensee_code mask_rom_version header_checksum global_checksum",
        )._make(header_unpacked)
