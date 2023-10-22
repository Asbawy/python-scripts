import hashlib

def hash_generator(input_string):
    hash_dict = {
        'MD5': hashlib.md5(input_string.encode()).hexdigest(),
        'SHA-1': hashlib.sha1(input_string.encode()).hexdigest(),
        'SHA-256': hashlib.sha256(input_string.encode()).hexdigest(),
        'SHA-512': hashlib.sha512(input_string.encode()).hexdigest(),
        'BLAKE2b': hashlib.blake2b(input_string.encode()).hexdigest(),
        'BLAKE2s': hashlib.blake2s(input_string.encode()).hexdigest(),
        'SHA3-256': hashlib.sha3_256(input_string.encode()).hexdigest(),
        'SHA3-512': hashlib.sha3_512(input_string.encode()).hexdigest(),
        'SHAKE128': hashlib.shake_128(input_string.encode()).hexdigest(16),
        'SHAKE256': hashlib.shake_256(input_string.encode()).hexdigest(32)
    }

    for algo, hash_val in hash_dict.items():
        print(f'{algo} hash : {hash_val}')

input_string = input("Enter a string to hash: ")
hash_generator(input_string)