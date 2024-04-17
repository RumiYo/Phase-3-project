from models.__init__ import CURSOR, CONN

class Playlist:

    all = {}

    def __init__(self, name, song_id, user_id):
        self.id = id
        self.name = name
        self.song_id = song_id
        self.user_id = user_id

    def __repr__(self):
        return(
            f"<Playlist {self.name} (song_id: {self.song_id}, user_id: {self.user_id}>"
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
    def song_id (self):
        return self._song_id

    @song_id.setter
    def song_id(self, song_id):
        if isinstance(song_id, int) and 0 < song_id:
            self._song_id = song.id
        else:
            raise TypeError("Song ID must be a string")

    @property
    def user_id (self):
        return self._user_id

    @user_id_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int) and 0 < user_id:
            self._user_id = user.id
        else:
            raise TypeError("User ID must be a string")

    @classmethod 
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXIST playlists (
                id INTEGER PRIMARY KEY,
                name TEXT, 
                FOREIGN KEY (song_id) REFERENCES songs(id), 
                FOREIGN KEY (user_id) EREFERENCES users(id)
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
            INSERT INTO playlists (name, song_id, user_id)
        """
        CURSOR.execute(sql, (self.name, self.song_id, self.user_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """ 
            UPDATE playlists
            SET name = ? song_id = ?, user_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.song_id, self.user_id, self.id))
        CONN.commit()

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
    def create(cls, name, song_id, user_id):
        playlist = cls(name, song_id, user_id)
        playlist.save()
        return playlist

    @classmethod
    def instance_from_db(cls, row):
        playlist = cls.all.get(row[0])
        if playlist: 
            playlist.name = row[1]
            playlist.song_id = row[2]
            playlist.user_id = row[3]
        else: 
            playlist = cls(row[1], row[2], row[3])
            playlist.id = row[0]
            cls.all[playlist.id] = playlist
        return playlist

    @classmethod 
    def get_all(cls):
        sql = """
            SELECT * FROM playlists
        """ 
        row =CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

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
            SELECT * FROM playlist 
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    
