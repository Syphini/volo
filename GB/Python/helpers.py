def getLowerNibble(value: int):
    return value & 0b1111


def int_to_hex(value):
    return "0x" + hex(value)[2:].zfill(2).upper()


def hexstring_to_bytearray(hex_data: str):
    data = bytearray()
    for c in bytes.fromhex(hex_data):
        data.append(c)
    return data
