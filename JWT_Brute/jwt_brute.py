#!/bin/python3
import jwt
import sys
from colorama import Fore
import time
from concurrent.futures import ThreadPoolExecutor

def brute_force_jwt(encoded, secret):
    try:
        payload = jwt.decode(encoded, secret, algorithms=['HS256'])
        return secret
    except jwt.InvalidKeyError:
        return None
    except jwt.ExpiredSignatureError:
        return None
    except Exception as e:
        return None

def main():
    print(Fore.RED+"\nScript for brute force jwt token by: Asbawy")
    encoded = input(Fore.BLUE+"Enter JWT token: ")
    password_list = input(Fore.BLUE+"Enter the passwords list: ")

    try:
        with open(password_list) as secrets_file:
            secrets = [line.strip() for line in secrets_file]
        print(Fore.BLUE+f"[INFO] Starting brute force with {len(secrets)} passwords....")
        start_time = time.time()
        success = None
        passwords_tested = 0

        with ThreadPoolExecutor(max_workers=4) as executor:
            for secret in secrets:
                result = executor.submit(brute_force_jwt, encoded, secret)
                passwords_tested += 1
                if result.result():
                    success = result.result()
                    break
                    
                sys.stdout.write(Fore.BLUE+f"\r[INFO] Passwords tested: {passwords_tested}")
                sys.stdout.flush()
        
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