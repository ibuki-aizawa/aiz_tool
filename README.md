# aiz_tool

## Password Generator

```bash
Usage: ./password_generator.py [options]
Options:
  -n, --number <number>: Generate <number> passwords (default is 10)
  -l, --length <length>: Specify the length of the password (default is 16)
  -s, --with-symbols: Include symbols in the password (default is False)
  -x, --xkcd: Generate a password using the XKCD method (word-based)
  -h, --help: Show this help message
  -v, --version: Show the version of the script
```

## Rot-N

```bash
Usage: rot_n.py [options] [<text>]
Options:
  -n, --n <number>: Rotate characters by <number> positions (default is 13)
  -h, --help: Show this help message
```

### Example Usage:
```bash
./rot_n.py -n 5 "Hello, World!"
```

```bash
cat file.txt | ./rot_n.py -n 5
```
