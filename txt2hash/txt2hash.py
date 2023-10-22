#!/usr/bin/python3
from colorama import Fore
import hashlib
import argparse


def main(text, hashType):
    supported_hash_types = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

    if hashType.lower() not in supported_hash_types:
    	print(Fore.RED + f"[!] the script does not support the hash type: {hashType}")
    	return

    encoder = text.encode('utf-8')
    myHash = hashlib.new(hashType, encoder).hexdigest()
    print(Fore.RED + f"[+] Hash ({hashType}): {myHash}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='txt2hash.py',
        description='This script takes text and returns its hash using various hash algorithms',
        epilog='Script by [Asbawy]')

    parser.add_argument('-t', '--text', dest='text', required=True, help='The text to hash.')
    parser.add_argument('-T', '--type', dest='type', required=True, choices=['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'], help='The hash algorithm to use.')

    args = parser.parse_args()
    main(args.text, args.type)
