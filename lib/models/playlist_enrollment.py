from models.__init__ import CURSOR, CONN

class Playlist_enrollment:

    all = {}

    def __init__(self, playlist_id, song_id, id=None):
        self.id = id
        self.playlist_id = playlist_id
        self.song_id = song_id
    
    def __str__(self):
        from models.playlist import Playlist
        from models.song import Song
        from models.artist import Artist
        song = Song.find_by_id(self.song_id)
        artist = Artist.find_by_id(song.artist_id)
        playlist = Playlist.find_by_id(self.playlist_id)
        return (f" - {song.name} ({artist.name}, {song.year})")

    @property
    def playlist_id(self):
        return self._playlist_id 
    
    @playlist_id.setter
    def playlist_id(self, playlist_id):
        if isinstance(playlist_id, int) and playlist_id:
            self._playlist_id = playlist_id

    @property
    def song_id(self):
        return self._song_id 
    
    @song_id.setter
    def song_id(self, song_id):
        if isinstance(song_id, int) and song_id:
            self._song_id = song_id

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS playlist_enrollments (
                id INTEGER PRIMARY KEY,
                playlist_id INTEGER,
                song_id INTEGER,
                FOREIGN KEY (playlist_id) REFERENCES playlists(id),
                FOREIGN KEY (song_id) REFERENCES songs(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS playlist_enrollments;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO playlist_enrollments (playlist_id, song_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.playlist_id, self.song_id))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        sql = """
            UPDATE playlist_enrollments
            SET playlist_id = ?, song_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.playlist_id, self.song_id, self.id))
        CONN.commit()
        
        type(self).all[self.id] = self  

    def delete(self):
        sql = """
            DELETE FROM playlist_enrollments
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, playlist_id, song_id):
        enrollment = cls(playlist_id, song_id)
        enrollment.save()
        return enrollment
    
    @classmethod
    def instance_from_db(cls, row):
        enrollment = cls.all.get(row[0])
        if enrollment:
            enrollment.playlist_id = row[1]
            enrollment.song_id = row[2]
        else:
            enrollment = cls(row[1], row[2])
            enrollment.id = row[0]
            cls.all[enrollment.id] = enrollment
        return enrollment

    @classmethod 
    def get_all(cls):
        sql = """
            SELECT * FROM playlist_enrollments
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM playlist_enrollments
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id, )).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_registry(cls, playlist_id, song_id):
        sql = """
            SELECT * FROM playlist_enrollments
            WHERE playlist_id = ? and song_id = ?
        """
        row = CURSOR.execute(sql, (playlist_id, song_id )).fetchone()
        return cls.instance_from_db(row) if row else None

