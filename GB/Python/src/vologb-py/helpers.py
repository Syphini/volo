def formatted_hex(value: int, no_prefix: bool = False, use_16_bit: bool = False) -> str:
    result = hex(value)[2:].zfill(4 if use_16_bit else 2).upper()
    if no_prefix:
        return result
    return "0x" + result
