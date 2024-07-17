def formatted_hex(value):
    return "0x" + hex(value)[2:].zfill(2).upper()


def wrap_16bit(value):
    return value & 0xFFFF


def wrap_8bit(value):
    return value & 0xFF


def signed_value(value):
    if (value & (1 << 7)) != 0:
        return -(128 - (value - (1 << 7)))
    return value
