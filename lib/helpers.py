# lib/helpers.py
from models.artist import Artist, GENRES
from models.user import User


def exit_program():
    print("Goodbye!")
    exit()

def login():
    print("Performing useful function#1.")
    name = input("Enter your name: ")
    return True



def signup():
    print("Performing useful function#2.")
    name = input("Enter your name: ")
    birth_year = input("Enter your birth year: ")
    print(f"Gener list: {User.GENDERS}")
    gender = input("Enter your gender (Select a number from above): ")
    email = input("Enter your email address: ")
    print(name, birth_year, gender, email)


