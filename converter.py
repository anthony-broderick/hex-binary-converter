"""
Parse the input (can be multiple args separated by spaces).

    If it starts with 0x, treat it as hex.

    If it starts with 0b, treat it as binary.

    If it’s only digits, treat it as decimal.

    Otherwise, treat it as text.
"""

import argparse

# [2:] strips '0x' or '0b' prefix
def to_hex(number: int) -> str:
    return hex(number)[2:]
def to_binary(number: int) -> str:
    return bin(number)[2:]
def to_ascii(number: int) -> str:
    try:
        return chr(number)
    except ValueError:
        return "?"

def convert(input_str: str) -> str:

    # int(input_str, base)
    try:
        if input_str.startswith("0x"):
            # hexadecimal
            number = int(input_str, 16)
        elif input_str.startswith("0b"):
            # binary
            number = int(input_str, 2)
        elif input_str.isdigit():
            # decimal
            number = int(input_str)
        else:
            # assume ASCII
            return (
                f"ASCII: {input_str}\n"
                f"Hex: {' '.join(hex(ord(c))[2:] for c in input_str)}\n"
                f"Binary: {' '.join(bin(ord(c))[2:].zfill(8) for c in input_str)}"
            )
    except ValueError:
        return "Invalid input format.\n"
    
    return (
        f"Decimal: {number}\n"
        f"Hex: {to_hex(number)}\n"
        f"Binary: {to_binary(number)}\n"
        f"ASCII: {to_ascii(number)}"
    )