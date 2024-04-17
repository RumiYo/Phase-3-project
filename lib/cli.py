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
    add_song

)


def main():
    logged_in = False

    while True:
        if not logged_in:
            login_page()
        choice = input("> ")
        if choice == "0":   # 0. Exit the program
            exit_program()
        elif choice == "1":   # 1. Login
            if login():
                logged_in = True 
                
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
                        pass
                    elif choice == "00":  # 00. Sign Out0
                        logged_in = False
                        break 
                    else:
                        print("Invalid choice")

        elif choice == "2":  # 2. Sign in
            if signup():
                logged_in = True 
                menu2()
        else:
            print("Invalid choice")


def login_page():
    print("Welcome to Music player!")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Login")
    print("2. Create your account")

def main_page():
    print("What do you want to listen to?")
    print("1. Artists")
    print("2. Songs")
    print("3. Playlists")
    print("00. Sign Out")
    print("0. Exit the program")

def menu_artists():
    print("Artists")
    print("1. Open the list of artists")
    print("2. Find artist by name")
    print("3. Add artist")
    print("4. Return to Main page")
    print("0. Exit the program")
    return True

def menu_songs():
    print("Songs")
    print("1. Open the list of songs")
    print("2. Find song by name")
    print("3. Add song")
    print("4. Return to Main page")
    print("0. Exit the program")
    return True

    

if __name__ == "__main__":
    main()
