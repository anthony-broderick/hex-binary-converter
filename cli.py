import argparse
from converter import convert

def main():
    parser = argparse.ArgumentParser(description="Convert between decimal, binary, hex, and ASCII")
    parser.add_argument("values", nargs="+", help="One or more numbers or strings to convert")
    args = parser.parse_args()

    for val in args.values:
        result = convert(val)
        print(result)
        print()

    
if __name__ == "__main__":
    main()