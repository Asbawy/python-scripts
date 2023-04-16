import requests

def check_single_domain(domain):
    response = requests.get(domain)
    status_code = response.status_code
    print(f"{domain} - Status Code: {status_code}")

def check_domains_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            domain = line.strip()
            check_single_domain(domain)

# Menu
print("\n1. Check status code for a single domain")
print("2. Check status code for multiple domains in a file")
choice = input("\nEnter your choice (1 or 2): ")

if choice == '1':
    domain = input("Enter the domain name: ")
    check_single_domain(domain)
elif choice == '2':
    filename = input("Enter the name of the file containing the domains: ")
    check_domains_file(filename)
else:
    print("Invalid choice. Please enter 1 or 2 .")
