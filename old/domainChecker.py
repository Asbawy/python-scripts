import requests
import sys
import os.path
from termcolor import colored


def validate_domain_name(domain_name):
    if ' ' in domain_name:
        return False
    elif not domain_name:
        return False
    else: 
        return True
    

def check_status_code(domain):
    try:
        response = requests.get(f"https://{domain}")
        print(colored(f"{domain} -- Status code : {response.status_code}", "green"))
    except requests.exceptions.RequestException as e:
        print(colored(f"{domain} -- Error: {e}", "red"))
        print(colored("Please check the domain name and try again.", "red"))


def check_multiple_domains(file_path):
    try:
        with open(file_path, 'r') as f:
            domains = f.read().splitlines()
    except FileNotFoundError:
            print(colored(f"Error: Could not find the file '{file_path}'", "red"))
            return
    
    for domain in domains:
        check_status_code(domain)

    sys.exit()


def main():
    print(colored("*** Welcome to the Domain Status Checker ***\n", "cyan"))

    while True:
        print("Please choose one of the following options:")
        print(colored("1. Check status code for a single domain", "yellow"))
        print(colored("2. Check status code for multiple domains in a file", "yellow"))
        print(colored("3. Exit", "yellow"))

        choice = input("\nEnter your choice (1, 2, 3): ")

        if choice == "1":
            while True:
                domain = input("\nEnter the domain name: ")
                if validate_domain_name(domain):
                    break
                else:
                    print(colored("Invalid domain name. Please try again.", "red"))

            check_status_code(domain)
            sys.exit()
        elif choice == "2":
            while True:
                file_path = input("\nEnter the file path: ")
                if os.path.isfile(file_path):
                    break
                else:
                    print(colored("Invalid file path. Please try again.", "red"))

            check_multiple_domains(file_path)
        elif choice == "3":
            print(colored("\nThank you for using the Domain Status Checker By:Anubis!", "cyan"))
            sys.exit()
        else:
            print(colored("\nInvalid choice. Please choose a valid option.\n", "red"))
            continue


if __name__ == '__main__':
    main()
