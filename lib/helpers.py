# lib/helpers.py
from models.artist import Artist, GENRES
from models.user import User


def exit_program():
    print("Goodbye!")
    exit()

def login():
    print("Performing useful function#1.")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    user = User.find_by_name(name)
    if user:
        if user.password == password:
            return True
        else: 
            print("The password is wrong")
    else: 
        print("The user name does not exist")

def signup():
    User.create_table()
    print("Performing useful function#2.")
    name = input("Enter your name: ")
    birth_year = input("Enter your birth year: ")
    print(f"Gener list: {User.GENDERS}")
    gender = input("Enter your gender (Select a number from above): ")
    email = input("Enter your email address: ")
    password = input("Create password (minimum 8 charactors): ")
    try: 
        user = User.create(name, int(birth_year), int(gender), email, password)
        print(f"{user.name} account is successfully created.")
        return True
    except Exception as exc:
        print("Error creating a user account", exc)

def list_artists():
    print("Artist list")

def find_artist_by_name():
    print("Find artist")

def add_artist():
    print("Add artist")


def list_songs():
    print("Song list")

def find_song_by_name():
    print("Find song")

def add_song():
    print("Add song")




