from models.__init__ import CURSOR, CONN
from models.artist import Artist

class Song:

    all = {}

    def __init__(self, name, year, artist_id, id=None):
        self._id = id 
        self._name = name
        self._year = year
        self._artist_id = artist_id

    def __str__(self):
        artist = Artist.find_by_id(self.artist_id)
        return (
            f" - {self.name} ({artist.name}, {self.year})"
        )

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise TypeError ("Song name must be a non-empty string")

    @property
    def year(self):
        return self._year 

    @year.setter
    def year(self, year):
        if isinstance(year, int) and 1800 <= year <= 2024:
            self._year = year
        else: 
            raise TypeError ("Release year must be between 1800 and 2024")
    
    @property
    def artist_id (self):
        return self._artist_id 

    @artist_id.setter
    def artist_id(self, artist_id):
        if type(artist_id) is int and Artist.find_by_id(artist_id):
            self._artist_id = artist_id
        else:
            raise ValueError("Artist_id must reference a artist in the database")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                year INTEGER, 
                artist_id INTEGER,
                FOREIGN KEY (artist_id) REFERENCES artists(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS songs;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO songs (name, year, artist_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.year, self.artist_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE songs 
            SET name = ?, year = ?, artist_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.year, self.artist_id, self.id))
        CONN.commit()
        
        type(self).all[self.id] = self  

    def delete(self):
        sql = """
            DELETE FROM songs
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
        
    @classmethod
    def create(cls, name, year, artist_id):
        song = cls(name, year, artist_id)
        song.save()
        return song

    @classmethod
    def instance_from_db(cls, row):
        song = cls.all.get(row[0])
        if song:
            song.name = row[1]
            song.year = row[2]
            song.artist_id = row[3] 
        else:
            song = cls(row[1], row[2], row[3])
            song.id = row[0]
            cls.all[song.id] = song
        return song
    
    @classmethod 
    def get_all(cls):
        sql = """
            SELECT * FROM songs
        """ 
        rows =CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod 
    def get_all_for_artist(cls, artist_id):
        sql = """
            SELECT * FROM songs
            WHERE artist_id = ?
        """ 
        rows =CURSOR.execute(sql, (artist_id, )).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM songs 
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name_full_match(cls,name):
        sql = """
            SELECT * FROM songs 
            WHERE LOWER(name) = LOWER(?)
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    
    @classmethod
    def find_by_name_partial_match(cls, name):
        sql = """
            SELECT * FROM songs
            WHERE LOWER(name) like LOWER(?)
        """
        search_term = '%' + name + '%'
        rows = CURSOR.execute(sql,(search_term,)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else None
