# lib/helpers.py
from models.artist import Artist, GENRES
from models.song import Song
from models.user import User


def exit_program():
    print("Goodbye!")
    exit()

def login():
    print("\nGood to see you again!\n")
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
    print("\nCrate your account.\n")
    name = input("Enter your name: ")
    birth_year = input("Enter your birth year: ")
    print(f"Gender list: {User.GENDERS}")
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
    print("Artist list\n")
    artists = Artist.get_all()
    for artist in artists:
        print(artist)

def find_artist_by_name():
    print("Find artist\n")
    name = input("Enter the artist name: ")
    artist = Artist.find_by_name(name)
    print(artist) if artist else print (f'{name} not found')


def add_artist():
    print("Add artist\n")
    Artist.create_table()
    name = input("Enter artist name: ")
    country = input("Enter what country the artist is from: ")
    print(f"Genre list: {GENRES}")
    genre_id =input ("Enter genre number from the list above: ")
    try:
        artist = Artist.create(name, country, int(genre_id))
        print(f"{artist.name} is successfly added to the artist list")
    except Exception as exc:
        print("Error creating an artist", exc)

def list_songs():
    print("Song list\n")
    songs = Song.get_all()
    for song in songs:
        print(song)

def find_song_by_name():
    print("Find song\n")
    name = input("Enter the song name: ")
    song = Song.find_by_name(name)
    print(song) if song else print (f'{name} not found')

def add_song():
    print("Add song\n")
    Song.create_table()
    name = input("Enter song name: ")
    year = input("Enter the release year: ")
    artist_name = input("Enter the artist name: ")
    artist = Artist.find_by_name(artist_name)
    try:
        song = Song.create(name, int(year), int(artist.id))
        print(f"{song.name} is successfly added to the song list")
    except Exception as exc:
        print("Error creating a song", exc)

def list_playlists():
    print("Playlist list\n")    
    
def open_playlist():
    print("Open Playlist\n")

def create_playlist():
    print("Create Playlist\n")





