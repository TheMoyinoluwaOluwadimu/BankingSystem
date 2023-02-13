import random

# Store all the users and their information
users = {}


def generate_account_number():
    account_number = ''
    for i in range(10):
        account_number += str(random.randint(0, 9))
    return account_number


def register():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Generate a random account number
    account_number = generate_account_number()
    while account_number in users:
        account_number = generate_account_number()

    # Save the user information
    users[account_number] = {
        'name': name,
        'email': email,
        'password': password,
        'balance': 0.0
    }
    print("Registration successful! Your account number is: ", account_number)


def login():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")

    if account_number in users:
        user = users[account_number]
        if user['password'] == password:
            return account_number

    return None


def deposit(account_number):
    amount = float(input("Enter the amount to deposit: "))
    users[account_number]['balance'] += amount
    print("Deposit successful! Your current balance is: ", users[account_number]['balance'])


def withdraw(account_number):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > users[account_number]['balance']:
        print("Insufficient balance!")
    else:
        users[account_number]['balance'] -= amount
        print("Withdrawal successful! Your current balance is: ", users[account_number]['balance'])


def main():
    while True:
        print("\nWelcome to the banking system")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            register()
        elif choice == 2:
            account_number = login()
            if account_number:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Logout")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        deposit(account_number)
                    elif choice == 2:
                        withdraw(account_number)
                    elif choice == 3:
                        break
            else:
                print("Incorrect account number or password!")
        elif choice == 3:
            break


if __name__ == '__main__':
    main()
