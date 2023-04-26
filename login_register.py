import base64 


def register(username, password):
    # Encode username and password to Base64
    encoded_username = base64.b64encode(username.encode('utf-8')).decode('utf-8')
    encoded_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')

    # Write the encoded username and password to a File 

    with open('users.txt', 'r') as f:
        users = [line.strip() for line in f]

    for user in users:
        if user.split(',')[0] == encoded_username:
            print('Username already exists')
            return
    
    with open('users.txt', 'a') as f:
        f.write(f'{encoded_username},{encoded_password}')
    print('Registration successful.')


def login(username, password):
    # Read the encoded username and password from File

    with open("users.txt", "r") as f:
        for line in f:
            encoded_username, encoded_password = line.strip().split(',')
            if encoded_username == base64.b64encode(username.encode('utf-8')).decode('utf-8') and encoded_password == base64.b64encode(password.encode('utf-8')).decode('utf-8'):
                print("Login successful")
                return
    print("Invalid username or password")

def main():
    while True:
        option = input("Enter an option  (login or register): ").lower()
        if option == 'register':
            username = input('Enter a username: ')
            password = input('Enter a password: ')
            re_password = input('Enter password again: ')
            if password == re_password:
                register(username, password)
            else:
                print("Passwords did't match ")
        elif option == 'login':
            username = input("Enter your username: ")
            password = input("Enter you password: ")
            login(username, password)
        else:
            print("Invalid option")

if __name__ == '__main__':
    main()
