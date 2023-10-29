#!/bin/python3
import jwt
import sys
from colorama import Fore
import time
from concurrent.futures import ThreadPoolExecutor
import re
from tqdm import tqdm

def brute_force_jwt(encoded, secrets):
    success = None
    for secret in secrets:
        try:
            payload = jwt.decode(encoded, secret, algorithms=['HS256'])
            return secret
            break
        except jwt.InvalidKeyError:
            pass
        except jwt.ExpiredSignatureError:
            pass
        except Exception as e:
            pass
    return success

def main():
    banner = """
    ╔╦╗╔═╗╔╦╗ ╦╦ ╦╔╦╗
     ║║║╣  ║║ ║║║║ ║
    ═╩╝╚═╝═╩╝╚╝╚╩╝ ╩ v1.0
    JWT Bruter by Asbawy
    """
    print(Fore.RED+banner)
    encoded = input(Fore.BLUE+"Enter JWT token: ")
    password_list = input(Fore.BLUE+"Enter the passwords list: ")

    try:
        with open(password_list) as secrets_file:
            secrets = [line.strip() for line in secrets_file]
        
        num_threads = 4  # Adjust this number based on your system's capabilities
        batch_size = len(secrets) // num_threads

        print(Fore.BLUE+f"[INFO] Starting brute force with {len(secrets)} passwords....")
        start_time = time.time()
        success = None
        passwords_tested = 0

        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            batches = [secrets[i:i + batch_size] for i in range(0, len(secrets), batch_size)]
            for batch in tqdm(batches, unit=' batch', ncols=100, ascii=True):
                result = executor.submit(brute_force_jwt, encoded, batch)
                if result.result():
                    success = result.result()
                    break

        if success:
            print(Fore.GREEN+f"\n[+] Token decoded with the following password: [{success}]")
        else:
            print(Fore.RED+"\n[-] Failed to decode token.")
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(Fore.CYAN+f"[INFO] Elapsed time: {elapsed_time:.2f} seconds")
    except FileNotFoundError:
        print(Fore.RED+f"\n[ERR] File: {password_list} not found!")
    except KeyboardInterrupt:
        print(Fore.RED+f"\n[ERR] Brute force interrupted by user!")

if __name__ == "__main__":
    main()