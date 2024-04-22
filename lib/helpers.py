# lib/helpers.py
from models.artist import Artist, GENRES
from models.song import Song
from models.user import User
from models.playlist import Playlist
from models.palylist_enrollment import Playlist_enrollment


def exit_program():
    print("Goodbye!")
    exit()

def login():
    User.create_table()
    print("\nGood to see you again!\n")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    user = User.find_by_name(name)
    if user:
        if user.password == password:
            print("\nYou are successfuly logged in")
            return user
        else: 
            print("The password is wrong")
            return None
    else: 
        print("The user name does not exist")
        return None

def signup():
    User.create_table()
    print("\nCrate your account.\n")
    name = input("Enter your name: ")
    name_verify = User.find_by_name(name)
    if name_verify:
        print(f"User name {name} exists already. Please try the other name.")
    else: 
        birth_year = input("Enter your birth year: ")
        print(f"Gender list: {User.GENDERS}")
        gender = input("Enter your gender (Select a number from above): ")
        email = input("Enter your email address: ")
        email_verify = User.find_by_email(email)
        if email_verify:
            print(f"{email} exists already. Please login with your account.")  
        else:          
            password = input("Create password (minimum 8 charactors): ")
            try: 
                user = User.create(name, int(birth_year), int(gender), email, password)
                print(f"{user.name} account is successfully created.")
                return True
            except Exception as exc:
                print("Error creating a user account", exc)

def list_artists():
    Artist.create_table()
    print("Artist list\n")
    artists = Artist.get_all()
    for artist in artists:
        print(artist)

def find_artist_by_name():
    Artist.create_table()
    print("Find artist\n")
    name = input("Enter the artist name: ")
    artists = Artist.find_by_name_partial_match(name)
    if not artists:
        print (f'Artist name "{name}" not found')
    else:
        for artist in artists:
            print(f"\n{artist}")
            Song.create_table()         
            songs = Song.get_all_for_artist(artist.id)
            if songs: 
                for song in songs:
                    print(f"  - {song.name} (Year: {song.year})")
            else: 
                print("  No songs registered for this artist")


def add_artist():
    print("Add artist\n")
    Artist.create_table()
    name = input("Enter artist name: ")
    name_verify = Artist.find_by_name(name)
    if name_verify:
        print(f"\nError adding the artist: {name} already exists.")
    else:
        country = input("Enter what country the artist is from: ")
        print(f"Genre list: {GENRES}")
        genre_id =input ("Enter genre number from the list above: ")
        try:
            artist = Artist.create(name, country, int(genre_id))
            print(f"{artist.name} is successfly added to the artist list")
            print(artist)
        except Exception as exc:
            print("\nError creating an artist", exc)

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
    name_verify = Song.find_by_name(name)
    year = input("Enter the release year: ")
    artist_name = input("Enter the artist name: ")
    artist = Artist.find_by_name(artist_name)
    if name_verify and artist:
        print(f"\nError adding a song: {name} ({artist_name}) already exists.")
    else:
        try:
            song = Song.create(name, int(year), int(artist.id))
            print(f"\n{song.name} is successfly added")
            print(song)
        except Exception as exc:
            print("Error adding a song", exc)

def list_playlists(user):
    Playlist.create_table()
    print(f"{user.name}'s Playlist list\n")    
    playlists = Playlist.get_all_by_user(user.id)
    if playlists:
        for playlist in playlists:
            print(f" - {playlist.name}")
    else:
        print("Playlist does not exist")
    
def open_playlist_by_name(user):
    Playlist.create_table()
    print("Open Playlist\n")
    name = input("Enter the playlist name: ")
    playlist = Playlist.get_all_by_user_n_name(user.id, name)
    if playlist:
        print(f"\n<Playlist: {playlist.name}>") 
        enrollments = Playlist_enrollment.get_all_songs_for_playlist(playlist.id)
        if enrollments: 
            for enrollment in enrollments:
                song_info = Song.find_by_id(enrollment.song_id)
                print(enrollment)
                # print(f"  - {song_info.name} (Year: {song_info.year})")
        else: 
            print("  No songs registered for this playlist")
    else:
        print (f'Playlist {name} not found')

def create_playlist(user):
    print("Create Playlist\n")
    Playlist.create_table()
    name = input("Enter playlist name: ")
    name_verify = Playlist.get_all_by_user_n_name(user.id, name)
    if name_verify:
        print(f"Error creating playlist: Playlist {name} already exists")
    else:
        try:
            playlist = Playlist.create(name, int(user.id))
            print(f"Playlist {playlist.name} is successfly created")
            print(playlist)
        except Exception as exc:
            print("Error creating a playlist", exc)

def add_song_to_playlist(user):
    print("Add song to playlist\n")
    Playlist_enrollment.create_table()
    playlist_name = input("Enter the playlist name: ")
    playlist = Playlist.get_all_by_user_n_name(int(user.id), playlist_name)
    if playlist:
        song_name = input(f"Enter the song name to add to {playlist_name} :")
        song = Song.find_by_name(song_name)
        if song: 
            try:
                enrollment = Playlist_enrollment.create(int(playlist.id), int(song.id))
                print(f"{song.name} is successfly added to playlist {playlist.name}")
            except Exception as exc:
                print("Error creating an artist", exc)            
        else: 
            print(f"{song_name} not found")
    else: 
        print(f"{playlist_name} not found")



