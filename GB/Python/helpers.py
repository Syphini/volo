def getLowerNibble(value: int):
    return value & 0b1111


def int_to_hex(value):
    return "0x" + hex(value)[2:].zfill(2).upper()


def hexstring_to_bytearray(hex_data: str):
    data = bytearray()
    for c in bytes.fromhex(hex_data):
        data.append(c)
    return data


def wrap_16(value):
    return value % 0x10000


def wrap_8(value):
    return value % 256


def signed_value(value):
    if (value & (1 << 7)) != 0:
        return -(128 - (value - (1 << 7)))
    return value
