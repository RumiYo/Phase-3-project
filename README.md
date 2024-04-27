# Music App
Flatiron School Software Engineer course Phase 3 project

## Table of Contents
* [Phase 3 project requirement](#phase-3-project-requirements)
* [My Python CLI application](#my-python-cli-application)
* [Technologies](#my-technologies)
* [Resources](#resources)


## Phase 3 project requirements

[Project guidelines are here. ](https://github.com/learn-co-curriculum/python-p3-v2-final-project)

Implement a Python CLI Application that meets the following requirements

### ORM Requirements
The application must include a database created and modified with Python ORM methods that you write.

 * The data model must include at least 2 model classes.
 * The data model must include at least 1 one-to-many relationship.
 * Property methods should be defined to add appropriate constraints to each model class.
 * Each model class should include ORM methods (create, delete, get all, and find by id at minimum).

### CLI Requirements
 * The CLI must display menus with which a user may interact.
 * The CLI should use loops as needed to keep the user in the application until they choose to exit.
 * For EACH class in the data model, the CLI must include options: to create an object, delete an object, display all objects, view related objects, and find an object by attribute.
 * The CLI should validate user input and object creations/deletions, providing informative errors to the user.
 * The project code should follow OOP best practices.
 * Pipfile contains all needed dependencies and no unneeded dependencies.
 * Imports are used in files only where necessary.
 * Project folders, files, and modules should be organized and follow appropriate naming conventions.
 * The project should include a README.md that describes the application.

## My Python CLI Application
The music app where you can find various kinds of music and also give your flavor by adding your favorite musicians and songs.

[![Music App](http://img.youtube.com/vi/oqulOwIfZXw/0.jpg)](http://www.youtube.com/watch?v=oqulOwIfZXw)

## My Technologies
### Directory Structure

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── artist.py
    │   └── playlist_enrollment.py
    │   └── playlist.py
    │   └── song.py  
    │   └── user.py  
    ├── cli.py
    ├── debug.py
    └── helpers.py
    └── company.db    
```

### `while True` loop for CLI
`while True` creates a loop and continues running until `break` gets executed.
`while True` is used to show all menus (login_page, main_page, menu_artists, menu_songs, and menu_playlists)
```
elif choice == "1":  #1. Artists   
                            while True: 
                                if menu_artists():
                                    choice = input("> ")
                                    if choice == "1":   # 1. Open the list of artist
                                        list_artists()
                                    elif choice == "2":  # 2. Find artists by name
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
```

### Adding layered menu
The app page was structured like below.
```
Login menu
└── Main menu
    ├── Artist menu
    ├── Song menu
    └──  Playlist menu
```
Since `while True` was set for login page, the loop continued running.  In order to stop the loop and move users from the login page, I created "logged_in" and used it as a condition of the loop. With this, users successfully move to the main page after logging in or signing in. 
```
def main():
    logged_in = False

    while True:    
        while not logged_in:  # Add a loop to continue until a valid login is performed
            login_page()
            choice = input("> ")
            if choice == "0":   # 0. Exit the program
                exit_program()
            elif choice in ("1", "2"):   # 1. Login
                user = login()  if choice == "1" else signup()
                if user:
                    logged_in = True
                    logged_in_user = user  # Store the logged-in user globally
            
                    while True: 
                        main_page()
                        choice = input("> ")

```

### Additional method on the Model classes
Some methods were added in each model class.  Below is the method from the Playlist class.
This method was added to pull the data with multiple conditions. Also, by using "like" and "%", we can fetch all data which includes the input value.
```
    @classmethod 
        def get_all_by_user_n_name_partial_match(cls, user_id, name):
            sql = """
                SELECT * FROM playlists
                WHERE user_id = ? AND LOWER(name) like LOWER(?)
            """ 
            search_term =  '%' + name + '%'
            rows = CURSOR.execute(sql, (user_id, search_term)).fetchall()
            return [cls.instance_from_db(row) for row in rows]if rows else None
```


## Resources

- [Build a CLI Application in Python [Book Store Application]](https://youtu.be/kTaqR1WyT8A?si=34tY6hPUR5JVX0En)
- [Sample of CLI menus in action](https://youtu.be/4UIYd00J0ok?si=jYeLHOA7QVFcLgsT)
- [SQL: Using like match patterns](https://learnsql.com/blog/using-like-match-patterns-sql/)
- [README Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)