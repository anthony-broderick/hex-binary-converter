"""
Parse the input

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


def main():
    parser = argparse.ArgumentParser(description="Convert between decimal, binary, hex, and ASCII")
    parser.add_argument("number", help="The number or string to convert")
    args = parser.parse_args()

    input_str = args.number

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
            print("ASCII:", input_str)
            print("Hex:", " ".join(hex(ord(c))[2:] for c in input_str))
            print("Binary:", " ".join(bin(ord(c))[2:].zfill(8) for c in input_str))
            return
    except ValueError:
        print("Invalid input format.")
        return
    
    print("Decimal:", number)
    print("Hex:", to_hex(number))
    print("Binary:", to_binary(number))
    print("ASCII:", to_ascii(number))

if __name__ == "__main__":
    main()