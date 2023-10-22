# txt2hash.py

`txt2hash.py` is a simple command-line utility that takes text and returns its hash using various hash algorithms. You can specify the text to hash and the hash algorithm to use as command-line arguments.

## Features

- Supports multiple hash algorithms: md5, sha1, sha224, sha256, sha384, and sha512.
- Provides clear error messages if an unsupported hash type is chosen.

## Prerequisites

- Python 3.x
- [colorama](https://pypi.org/project/colorama/) library
  - You can install it using `pip install colorama`

## Usage

```bash
python txt2hash.py -t "Your text here" -T sha256

#or
chmod +x txt2hash.py
./txt2hash.py -t "Your text here" -T sha256
```
Replace "Your text here" with the text you want to hash, and "sha256" with your desired hash algorithm.

## Command-line Arguments

-t, --text: The text to hash (required).
-T, --type: The hash algorithm to use. Choose from 'md5', 'sha1', 'sha224', 'sha256', 'sha384', or 'sha512' (required).

## Example

```bash
python txt2hash.py -t "Hello, World!" -T sha256
```
