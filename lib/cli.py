# lib/cli.py

from helpers import (
    exit_program,
    login,
    signup
)


def main():
    while True:
        menu1()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            login()
        elif choice == "2":
            signup()
        else:
            print("Invalid choice")


def menu1():
    print("Welcome to Music player!")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Login")
    print("2. Create your account")


if __name__ == "__main__":
    main()
