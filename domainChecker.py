import requests
import sys
import os.path

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
        print(f"{domain} -- Status code : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{domain} -- Error: {e}")
        print("Please check the domain name and try again.")


def check_multiple_domains(file_path):
    try:
        with open(file_path, 'r') as f:
            domains = f.read().splitlines()
    except FileNotFoundError:
            print(f"Error: Could not find the file '{file_path}'")
            return
    
    for domain in domains:
        check_status_code(domain)

    sys.exit()

def main():
    print("*** Welcome to the Domain Status Checker ***\n")

    while True:
        print("Please choose one of the following options:")
        print("1. Check status code for a single domain")
        print("2. Check status code for multiple domains in a file")
        print("3. Exit")

        choice = input("\nEnter your choice (1, 2, 3): ")

        if choice == "1":
            while True:
                domain = input("\nEnter the domain name: ")
                if validate_domain_name(domain):
                    break
                else:
                    print("Invalid domain name. Please try again.")

            check_status_code(domain)
            sys.exit()
        elif choice == "2":
            while True:
                file_path = input("\nEnter the file path: ")
                if os.path.isfile(file_path):
                    break
                else:
                    print("Invalid file path. Please try again.")

            check_multiple_domains(file_path)
        elif choice == "3":
            print("\nThank you for using the Domain Status Checker By:Anubis!")
            sys.exit()
        else:
            print("\nInvalid choice. Please choose a valid option.\n")
            continue

if __name__ == '__main__':
    main()
