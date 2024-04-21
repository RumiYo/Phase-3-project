# lib/cli.py

from helpers import (
    exit_program,
    login,
    signup,
    list_artists,
    find_artist_by_name,
    add_artist,
    list_songs,
    find_song_by_name,
    add_song,
    list_playlists,
    open_playlist_by_name,
    create_playlist

)

logged_in_user = None

def main():
    logged_in = False

    while True:    
        while not logged_in:  # Add a loop to continue until a valid login is performed
            login_page()
            choice = input("> ")
            if choice == "0":   # 0. Exit the program
                exit_program()
            elif choice == "1":   # 1. Login
                user = login()  # Call login() only when choice is "1"
                if user:
                    logged_in = True
                    logged_in_user = user  # Store the logged-in user globally
            
                    while True: 
                        main_page()
                        choice = input("> ")
                        if choice == "0":
                            exit_program()
                        elif choice == "1":  #1. Artists   

                            while True: 
                                if menu_artists():
                                    choice = input("> ")
                                    if choice == "1":   # 1. Open the list of artist
                                        list_artists()
                                    elif choice == "2":  # 2. Find artist by name
                                        find_artist_by_name()
                                    elif choice == "3":  # 3. Add artist"
                                        add_artist()
                                    elif choice == "4":  # 4. Return to Main page
                                        break
                                    elif choice == "0":  # 0. Exit the program
                                        exit_program()
                                        break
                                    else: 
                                        print("Invalid choice")

                        elif choice == "2": # 2. Songs
                            
                            while True: 
                                if menu_songs():
                                    choice = input("> ")
                                    if choice == "1":   # 1. Open the list of songs
                                        list_songs()
                                    elif choice == "2":  # 2. Find song by name
                                        find_song_by_name()
                                    elif choice == "3":  # 3. Add a song"
                                        add_song()
                                    elif choice == "4":  # 4. Return to Main page
                                        break
                                    elif choice == "0":  # 0. Exit the program
                                        exit_program()
                                        break
                                    else: 
                                        print("Invalid choice") 

                        elif choice == "3":  # 3. Playlists
                                    
                            while True: 
                                if menu_playllists():
                                    choice = input("> ")
                                    if choice == "1":   # 1. Open the list of playlists
                                        list_playlists()
                                    elif choice == "2":  # 2. Open a playlist
                                        open_playlist_by_name()
                                    elif choice == "3":  # 3. Create playlist
                                        create_playlist(logged_in_user)
                                    elif choice == "4":  # 4. Return to Main page
                                        break
                                    elif choice == "0":  # 0. Exit the program
                                        exit_program()
                                        break
                                    else: 
                                        print("Invalid choice") 

                        elif choice == "00":  # 00. Sign Out
                            logged_in = False
                            break 
                        else:
                            print("Invalid choice")

            elif choice == "2":  # 2. Signin
                if signup():
                    logged_in = True 
                    main_page()
            else:
                print("Invalid choice")


def login_page():
    print("\nWelcome to Music player!\n")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Login")
    print("2. Create your account")
    print("\n")

def main_page():
    print("\nWhat do you want to listen to?\n")
    print("1. Artists")
    print("2. Songs")
    print("3. Playlists")
    print("00. Sign Out")
    print("0. Exit the program")
    print("\n")

def menu_artists():
    print("\nArtists\n")
    print("1. Open the list of artists")
    print("2. Find artist by name")
    print("3. Add artist")
    print("4. Return to Main page")
    print("0. Exit the program")
    print("\n")
    return True

def menu_songs():
    print("\nSongs\n")
    print("1. Open the list of songs")
    print("2. Find song by name")
    print("3. Add song")
    print("4. Return to Main page")
    print("0. Exit the program")
    print("\n")
    return True

def menu_playllists():
    print("\Playlist\n")
    print("1. Open the list of playlist")
    print("2. Open playlist by name")
    print("3. Create playlist")
    print("4. Return to Main page")
    print("0. Exit the program")
    print("\n")
    return True    

if __name__ == "__main__":
    main()
