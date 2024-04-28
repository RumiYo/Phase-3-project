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
    print("\n----------------------------------")
    print("Good to see you again!\n")
    name = input("  Enter your name: ")
    password = input("  Enter your password: ")
    user = User.find_by_name(name)
    if user:
        if user.password == password:
            print("\nYou are successfuly logged in")
            return user
        else: 
            print("\nThe password is wrong")
            return None
    else: 
        print("\nThe user name does not exist")
        return None

def signup():
    User.create_table()
    print("\nCrate your account.\n")
    name = input("Enter your name: ")
    name_verify = User.find_by_name(name)
    if name_verify:
        print(f"User name {name} exists already. Please try the other name.")
        return None
    else: 
        birth_year = input("Enter your birth year: ")
        print(f"Gender list: {User.GENDERS}")
        gender = input("Enter your gender (Select a number from above): ")
        email = input("Enter your email address: ")
        email_verify = User.find_by_email(email)
        if email_verify:
            print(f"{email} exists already. Please login with your account.")
            return None
        else:          
            password = input("Create password (minimum 8 charactors): ")
            try: 
                user = User.create(name, int(birth_year), int(gender), email, password)
                print(f"{user.name} account is successfully created.")
                return user
            except Exception as exc:
                print("Error creating a user account", exc)
                return None

def change_password():
    name = input("  Enter your name: ")
    user = User.find_by_name(name)
    if user:
        password = input("  Enter your current password: ")
        if user.password == password:
            new_password = input("  Enter new password: ")
            user.password = new_password
            try: 
                user_updated = User.update(user)
                print(f"{user_updated.name}'s password is updated")
            except Exception as exc:
                print("Error changing password", exc)
                return None

        else: 
            print("\nThe password is wrong")
            return None
    else: 
        print("\nThe user name does not exist")
        return None    

    

def list_artists():
    Artist.create_table()
    print("Artist list\n")
    artists = Artist.get_all()
    artists.sort(key=lambda x: x.name) 
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
        artists.sort(key=lambda x: x.name) 
        for artist in artists:
            print(f"\n{artist}")
            Song.create_table()         
            songs = Song.get_all_for_artist(artist.id)
            if songs: 
                for song in songs:
                    print(f"    - {song.name} ({song.year})")
            else: 
                print("  No songs registered for this artist")


def add_artist():
    print("Add artist\n")
    Artist.create_table()
    name = input("Enter artist name: ")
    name_verify = Artist.find_by_name_full_match(name)
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
    songs.sort(key=lambda x: x.name) 
    for song in songs:
        print(song)

def find_song_by_name():
    print("Find song\n")
    name = input("Enter the song name: ")
    songs = Song.find_by_name_partial_match(name)
    if not songs:
        print (f'Song name "{name}" not found')
    else:
        songs.sort(key=lambda x: x.name) 
        for song in songs:
            print(song)      


def add_song():
    print("Add song\n")
    Song.create_table()
    name = input("Enter song name: ")
    name_verify = Song.find_by_name_full_match(name)
    year = input("Enter the release year: ")
    artist_name = input("Enter the artist name: ")
    artist_verify = Artist.find_by_name_full_match(artist_name)
    if artist_verify:
        if name_verify:
            print(f"\nError adding a song: {name} ({artist_name}) already exists.")
        else:
            try:
                song = Song.create(name, int(year), int(artist_verify.id))
                print(f"\n{song.name} is successfly added")
                print(song)
            except Exception as exc:
                print("Error adding a song", exc)
    else:
        print(f'Artist name "{artist_name}" not found')

def remove_song():
    print("Remove song\n")
    Song.create_table()
    name = input("Enter song name: ")
    song_verify = Song.find_by_name_full_match(name)
    if song_verify:
        Song.delete(song_verify)
        print(f"\n{name} is successfly added")
    else:
        print (f'Song name "{name}" not found')


def list_playlists(user):
    Playlist.create_table()
    print(f"{user.name}'s Playlist list\n")    
    playlists = Playlist.get_all_by_user(user.id)
    if playlists:
        for playlist in playlists:
            print(f" - {playlist.name}")
    else:
        playlists.sort(key=lambda x: x.name) 
        print("Playlist does not exist")
    
def open_playlist_by_name(user):
    Playlist.create_table()
    print("Open Playlist\n")
    name = input("Enter the playlist name: ")
    playlists = Playlist.get_all_by_user_n_name_partial_match(user.id, name)
    if playlists:
        playlists.sort(key=lambda x: x.name) 
        for playlist in playlists:
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
        song_name = input(f"Enter the song name to add to {playlist_name}:")
        song = Song.find_by_name_full_match(song_name)
        if song:
            if Playlist_enrollment.find_registry(playlist.id, song.id):
                print(f'{song_name} is already in playlist {playlist.name}')
            else:
                try:
                    enrollment = Playlist_enrollment.create(int(playlist.id), int(song.id))
                    print(f"{song.name} is successfly added to playlist {playlist.name}")
                except Exception as exc:
                    print("Error creating an artist", exc)            
        else: 
            print(f'"{song_name}" not found')
    else: 
        print(f"{playlist_name} not found")


def Remove_song_from_playlist(user):
    print("Remove song from playlist\n")
    Playlist_enrollment.create_table()
    playlist_name = input("Enter the playlist name: ")
    playlist = Playlist.get_all_by_user_n_name(int(user.id), playlist_name)
    if playlist:
        song_name = input(f"Enter the song name to remove from {playlist_name}:")
        song = Song.find_by_name_full_match(song_name)
        emrollment_verify = Playlist_enrollment.find_registry(playlist.id, song.id)
        if emrollment_verify: 
            try:
                Playlist_enrollment.delete(emrollment_verify)
                print(f"{song.name} is successfly deleted to playlist {playlist.name}")
            except Exception as exc:
                print("Error creating an artist", exc)            
        else: 
            print(f'"{song_name}" not found')
    else: 
        print(f"{playlist_name} not found")



