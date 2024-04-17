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
            if login():
                menu2()
        elif choice == "2":
            if signup():
                menu2()
        else:
            print("Invalid choice")


def menu1():
    print("Welcome to Music player!")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Login")
    print("2. Create your account")

def menu2():
    print("What do you want to listen to?")
    print("Select Playlists")
    print("Select Artists")
    print("Select Songs")
    input("Press Enter to return to the main menu")


if __name__ == "__main__":
    main()
