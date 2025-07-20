#! /usr/bin/env python3

import sys
import string
import secrets

version = '1.0.0'

def password(length: int, withSymbols: bool) -> str:
    alphabet = string.ascii_letters + string.digits

    if withSymbols:
        alphabet += string.punctuation

    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def xkcd(numberOfWords: int) -> str:
    with open('/usr/share/dict/words') as f:
        words = [word.strip() for word in f]
        password = ' '.join(secrets.choice(words) for _ in range(numberOfWords))
        return password

def usage() -> None:
    print('Usage: ./password_generator.py [options]')
    print('Options:')
    print('  -n, --number <number>: Generate <number> passwords (default is 10)')
    print('  -l, --length <length>: Specify the length of the password (default is 16)')
    print('  -s, --with-symbols: Include symbols in the password (default is False)')
    print('  -x, --xkcd: Generate a password using the XKCD method (word-based)')
    print('  -h, --help: Show this help message')
    print('  -v, --version: Show the version of the script')

if __name__ == '__main__':
    numberOfGenerations = 10
    length = 16
    withSymbols = False
    useXkcd = False
    args = sys.argv[1:]

    while args:
        arg = args.pop(0)
        if arg == '--help' or arg == '-h':
            usage()
            sys.exit(0)
        elif arg == '--version' or arg == '-v':
            print(f'version {version}')
            sys.exit(0)
        elif arg == '--xkcd' or arg == '-x':
            useXkcd = True
        elif (arg == '-l' or arg == '--length') and (not args or not args[0].isdigit()):
            print('Error: -l option requires a numeric argument.')
            sys.exit(1)
        elif arg == '-l' or arg == '--length':
            length = int(args.pop(0))
        elif arg == '--with-symbols' or arg == '-s':
            withSymbols = True
        elif (arg == '-n' or arg == '--number') and (not args or not args[0].isdigit()):
            print('Error: -n option requires a numeric argument.')
            sys.exit(1)
        elif arg == '-n' or arg == '--number':
            numberOfGenerations = int(args.pop(0))
        else:
            print(f'Error: Unknown option {arg}')
            usage()
            sys.exit(1)

    for i in range(numberOfGenerations):
        if useXkcd:
            print(xkcd(length))
        else:
            print(password(length, withSymbols))

