# Hex-Binary-Decimal-ASCII Converter

A minimal Python CLI tool to convert between decimal, binary, hex, and ASCII.

## Behind the Scenes

Parse the input (can be multiple args separated by spaces).

    If it starts with 0x, treat it as hex.

    If it starts with 0b, treat it as binary.

    If it’s only digits, treat it as decimal.

    Otherwise, treat it as text.

Convert to other formats

    Decimal → Hex → Binary → ASCII (single characters only).

    Or if it’s text, convert each character into binary + hex.

Print results
    
    Everything is displayed in a neat format.

## Usage

python converter.py 42 28 Hello
python converter.py 0x2A (or python converter.py 0x2a)
python converter.py 0b101010
python converter.py "Hello" (or python converter.py Hello)