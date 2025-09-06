# Hex-Binary-Decimal-ASCII Converter

A minimal Python CLI and GUI tool to convert between decimal, binary, hex, and ASCII.

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

python gui.py (for gui)
python cli.py [input] [optional_input] ... (for terminal print)