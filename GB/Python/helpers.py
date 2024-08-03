def formatted_hex(value, no_prefix=False, use_16_bit=False):
    result = hex(value)[2:].zfill(4 if use_16_bit else 2).upper()
    if no_prefix:
        return result
    return "0x" + result
