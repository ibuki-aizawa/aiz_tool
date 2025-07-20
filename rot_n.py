#!/usr/bin/env python3

import sys

def rot_n(text: str, n = 13):
    """
    Rotate characters in the text by n positions.
    """
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            offset = ord('a')
            result.append(chr((ord(char) - offset + n) % 26 + offset))
        elif 'A' <= char <= 'Z':
            offset = ord('A')
            result.append(chr((ord(char) - offset + n) % 26 + offset))
        else:
            result.append(char)
    return ''.join(result)

def usage() -> None:
    print("Usage: rot_n.py [options] [<text>]")
    print("Options:")
    print("  -n, --n <number>: Rotate characters by <number> positions (default is 13)")
    print("  -h, --help: Show this help message")

if __name__ == "__main__":
    n = 13
    args = sys.argv[1:]
    input_text = ""

    while args:
        arg = args.pop(0)
        if arg in ('--help', '-h'):
            usage()
            sys.exit(0)
        elif arg in ('--n', '-n'):
            if not args or not args[0].isdigit():
                print("Error: -n option requires a numeric argument.")
                sys.exit(1)
            n = int(args.pop(0))
        else:
            input_text += arg + " "

    if input_text == "":
        input_text = input().strip()

    output_text = rot_n(input_text, n)
    print(output_text)
