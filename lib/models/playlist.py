from models.__init__ import CURSOR, CONN
from models.user import User

class Playlist:

    all = {}

    def __init__(self, name, user_id, id=None):
        self._id = id
        self._name = name
        self._user_id = user_id

    def __repr__(self):
        user = User.find_by_id(self.user_id)
        return(
            f"<Playlist {self.name} (user_id: {user.name}) >>"
        )

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise TypeError("Playlist name must be a non-empty string")

    @property
    def user_id (self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int) and 1 <= user_id:
            self._user_id = user_id
        else:
            raise TypeError("User ID must be a string")

    @classmethod 
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS playlists (
                id INTEGER PRIMARY KEY,
                name TEXT, 
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS playlists
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO playlists (name, user_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.user_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """ 
            UPDATE playlists
            SET name = ?, user_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.user_id, self.id))
        CONN.commit()

        type(self).all[self.id] = self  

    def delete(self):
        sql = """
            DELETE FROM playlists
            WHERE id = ?
        """
        CURSOR.execute(sql,(self.id, ))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, user_id):
        playlist = cls(name, user_id)
        playlist.save()
        return playlist

    @classmethod
    def instance_from_db(cls, row):
        playlist = cls.all.get(row[0])
        if playlist: 
            playlist.name = row[1]
            playlist.user_id = row[2]
        else: 
            playlist = cls(row[1], row[2])
            playlist.id = row[0]
            cls.all[playlist.id] = playlist
        return playlist

    @classmethod 
    def get_all(cls):
        sql = """
            SELECT * FROM playlists
        """ 
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod 
    def get_all_by_user(cls, user_id):
        sql = """
            SELECT * FROM playlists
            WHERE user_id = ?
        """ 
        rows = CURSOR.execute(sql, (user_id, )).fetchall()
        return [cls.instance_from_db(row) for row in rows]if rows else None

    @classmethod 
    def get_all_by_user_n_name_partial_match(cls, user_id, name):
        sql = """
            SELECT * FROM playlists
            WHERE user_id = ? AND LOWER(name) like LOWER(?)
        """ 
        search_term =  '%' + name + '%'
        rows = CURSOR.execute(sql, (user_id, search_term)).fetchall()
        return [cls.instance_from_db(row) for row in rows]if rows else None

    @classmethod 
    def get_all_by_user_n_name(cls, user_id, name):
        sql = """
            SELECT * FROM playlists
            WHERE user_id = ? AND LOWER(name) == LOWER(?)
        """ 
        row = CURSOR.execute(sql, (user_id, name)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM playlists 
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls,name):
        sql = """
            SELECT * FROM playlists 
            WHERE LOWER(name) = LOWER(?)
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    