# lib/cli.py
from models.artist import GENRES
from helpers import (
    exit_program,
    login,
    signup,
    change_password,
    list_artists,
    find_artist_by_name,
    add_artist,
    list_songs_of_artist,
    add_song_for_selected_artist,
    remove_song_for_selected_artist,
    list_songs,
    find_song_by_name,
    add_song,
    remove_song,
    list_playlists,
    open_playlist_by_name,
    create_playlist,
    add_song_to_playlist,
    remove_song_from_playlist
)


def main():

    global logged_in_user 
    logged_in_user = None
    
    while not logged_in_user:  # Add a loop to continue until a valid login is performed
        login_page()
        choice = input("> ")
        if choice == "0":   # 0. Exit the program
            exit_program()
        elif choice in ("1", "2"):   # 1. Login
            user = login()  if choice == "1" else signup()
            if user:
                logged_in_user = user  # Store the logged-in user globally
        elif choice == "3": 
            change_password()
        else:
            print("Invalid choice")
            
    while logged_in_user: 
        main_page()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":  #1. Artists  
            artist_loop()
        elif choice == "2": # 2. Songs
            song_loop()
        elif choice == "3":  # 3. Playlists 
            playlist_loop()   
        else:
            print("Invalid choice")

def artist_loop():
    selected_artist = None

    while not selected_artist:  
        menu_artists()
        choice = input("> ")
        if choice == "1":   # 1. Open the list of artist
            list_artists()
        elif choice == "2":  # 2. Find artist by name
            artist = find_artist_by_name()
            if artist: 
                selected_artist = artist
                
        elif choice == "3":  # 3. Add artist"
            add_artist()
        elif choice == "4":  # 4. Return to Main page
            break
        elif choice == "0":  # 0. Exit the program
            exit_program()
        else: 
            print("Invalid choice")
    
    while selected_artist: 
        chosen_artist_menu(artist) 
        choice = input("> ")

        if choice == "0":
            exit_program()
        elif choice == "1": 
            list_songs_of_artist(selected_artist)
        elif choice == "2": 
            add_song_for_selected_artist(selected_artist)
        elif choice == "3": 
            remove_song_for_selected_artist(selected_artist)
        elif choice == "4": 
            break
        else: 
            print("Invalid choice")

def chosen_artist_menu(artist):
    print("\n=======================================")
    print(f"{artist.name} ({GENRES.get(artist.genre_id)}, {artist.country})\n")
    print(f"  1. Open the list of {artist.name} songs")
    print(f"  2. Add {artist.name} song")
    print(f"  3. Remove {artist.name} song")
    print("  4. Return to Artist page")
    print("  0. Exit the program")
    print("\n")

def song_loop():
    while True: 
        if menu_songs():
            choice = input("> ")
            if choice == "1":   # 1. Open the list of songs
                list_songs()
            elif choice == "2":  # 2. Find song by name
                find_song_by_name()
            elif choice == "3":  # 3. Add a song"
                add_song()
            elif choice == "4":  # 4. Remove a song"
                remove_song()
            elif choice == "5":  # 5. Return to Main page
                break
            elif choice == "0":  # 0. Exit the program
                exit_program()
            else: 
                print("Invalid choice") 

def playlist_loop():
    while True: 
        if menu_playlists():
            choice = input("> ")
            if choice == "1":   # 1. Open the list of playlists (logged-in users' playlists only)
                list_playlists(logged_in_user)
            elif choice == "2":  # 2. Open a playlist
                open_playlist_by_name(logged_in_user)
            elif choice == "3":  # 3. Create playlist
                create_playlist(logged_in_user)
            elif choice == "4":  # 4. Add song to a playlist
                add_song_to_playlist(logged_in_user)
            elif choice == "5":  # 5. Add song to a playlist
                remove_song_from_playlist(logged_in_user)
            elif choice == "6":  # 6. Return to Main page
                break
            elif choice == "0":  # 0. Exit the program
                exit_program()
            else: 
                print("Invalid choice") 


def login_page():
    print("\n****************************")
    print("* Welcome to Music player! *")
    print("****************************\n")
    print("Please select an option:\n")
    print("  1. Login")
    print("  2. Create your account")
    print("  3. Change password")
    print("  0. Exit the program")
    print("\n")

def main_page():
    print("\n=======================================")
    print("What do you want to listen to?\n")
    print("  1. Artists")
    print("  2. Songs")
    print("  3. Playlists")
    print("  0. Exit the program")
    print("\n")

def menu_artists():
    print("\n=======================================")
    print("Artists\n")
    print("  1. Open the list of artists")
    print("  2. Find artists by name")
    print("  3. Add artist")
    print("  4. Return to Main page")
    print("  0. Exit the program")
    print("\n")
    return True

def menu_songs():
    print("\n=======================================")
    print("Songs\n")
    print("  1. Open the whole list of songs")
    print("  2. Find song by name")
    print("  3. Add song")
    print("  4. Remove song")    
    print("  5. Return to Main page")
    print("  0. Exit the program")
    print("\n")
    return True

def menu_playlists():
    print("\n=======================================")
    print("Playlist\n")
    print("  1. Open the list of playlist")
    print("  2. Open playlist by name")
    print("  3. Create playlist")
    print("  4. Add song to playlist")
    print("  5. Remove song from playlist")
    print("  6. Return to Main page")
    print("  0. Exit the program")
    print("\n")
    return True    

if __name__ == "__main__":
    main()
