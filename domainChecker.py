import requests
import sys

def check_status_code(domain):
    try:
        response = requests.get(f"https://{domain}")
        print(f"{domain} -- Status code : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{domain} -- Error: {e}")


def check_multiple_domains(file_path):
    with open(file_path, 'r') as f:
        domains = f.read().splitlines()
        for domain in domains:
            check_status_code(domain)
    sys.exit()

def main():
    print("\n*** Welcome to the Domain Status Checker ***\n")
    while True:
        print("Please choose one of the following options:")
        print("1. Check status code for a singe domain")
        print("2. Check status code for multiple domains in a file")
        print("3. Exit")
        choice = input("\nEnter your choice (1, 2, 3): ")

        if choice == "1":
            domain = input("\nEnter the domain name: ")
            check_status_code(domain)
            sys.exit()
        elif choice == "2":
            file_path = input("Enter the file path: ")
            check_multiple_domains(file_path)
        elif choice == "3":
            print("\nThanks you fo using the Domain Status Checker By:Anubis!")
            sys.exit()
        else:
            print("\nInvalid choice, Please choose a valid option")
            continue
if __name__ == '__main__':
    main()
