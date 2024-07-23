def formatted_hex(value, no_prefix=False, use_16_bit=False):
    result = hex(value)[2:].zfill(4 if use_16_bit else 2).upper()
    if no_prefix:
        return result
    return "0x" + result


def wrap_16bit(value):
    return value & 0xFFFF


def wrap_8bit(value):
    return value & 0xFF


def signed_value(value):
    if (value & (1 << 7)) != 0:
        return -(128 - (value - (1 << 7)))
    return value
