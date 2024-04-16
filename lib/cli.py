# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        elif choice == "2":
            pass
        else:
            print("Invalid choice")


def menu():
    print("Welcome to Music player!")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Login")
    print("2. Create your account")


if __name__ == "__main__":
    main()
