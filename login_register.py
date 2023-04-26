import base64 
import json
import os 


def register(username, password):
    # Encode username and password to Base64
    encoded_username = base64.b64encode(username.encode('utf-8')).decode('utf-8')
    encoded_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')

    # Check if the users.json exist
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            users = json.load(f)
    else:
        users = {}

    # Check if the username already Exist
    for user_id, user in users.items():
        if user['username'] == encoded_username:
            print("Username already exists.")
            return
        
    # Generate new user ID
    user_id = str(len(users) + 1)

    # Add new user to the dictionary of Users
    users[user_id] = {'username': encoded_username, 'password': encoded_password}

    # Write the updated users dictionary to the JSON File
    with open('users.json', 'w') as f:
        json.dump(users, f)

    print(f'Registration successful. Your user ID is {user_id}.')


def login(username, password):
    # Check if the users.json exist
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            users = json.load(f)
    else:
        print('No users found')
        return
    
    # Check if the username and password match any User
    for user_id, user in users.items():
        if user['username'] == base64.b64encode(username.encode('utf-8')).decode('utf-8') and user['password'] == base64.b64encode(password.encode('utf-8')).decode('utf-8'):
            print(f'Login successful. Welcome, user {user_id}')
            return
    
    print('Invalid username or password.')


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