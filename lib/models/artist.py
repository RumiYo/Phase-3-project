from models.__init__ import CURSOR, CONN

GENRES = {
    1: "Rock",
    2: "Pop",
    3: "Hip hop",
    4: "R&B",
    5: "Latin",
    6: "Reggae",
    7: "Country & Fork",
    8: "Techno & EDM",
    9: "Jazz",
    10: "Classical"
}

class Artist:

    all = {}

    def __init__(self, name, country, genre_id, id=None):
        self.id = id
        self.name = name 
        self.country = country
        self.genre_id = genre_id

    def __repr__(self):
        return f"<Artist{self.id} {self.name} (country: {self.country}, genre: {GENRES.get(self.genre_id)})>"

    @property 
    def name(self):
        return self._name  
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else: 
            raise ValueError("Name must be a string.")
    
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        if isinstance(country, str) and len(country):
            self._country = country
        else:
            raise ValueError("Country is a string")
    
    @property
    def genre_id(self):
        return self._genre_id 

    @genre_id.setter
    def genre_id(self, genre_id):
        if isinstance(genre_id, int) and 1 <= genre_id <= 10:
            self._genre_id = genre_id
        else:
            raise ValueError("Genre is a number")

    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS artists (
                id INTEGER PRIMARY KEY,
                name TEXT,
                country TEXT,
                genre_id INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS artists;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO artists (name, country, genre_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.country, self.genre_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, country, genre_id):
        artist = cls(name, country, genre_id)
        artist.save()
        return artist

    def update(self):
        sql = """
            UPDATE artists
            SET name = ?, country = ?, genre_id = ? 
            WHERE id = ?
        """
        COURSOR.execute(sql, (self.name, self.country, self.genre_id, self.id))
        CON.commit()
    
    def delete(self):
        sql = """
            DELETE FROM artist
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        artist = cls.all.get(row[0])
        if artist:
            artist.name = row[1]
            artist.country = row[2]
            artist.genre_id = row[3]
        else:
            artist = cls(row[1], row[2], row[3])
            artist.id = row[0]
            cls.all[artist.id] = artist
        return artist

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM artists  
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM artists
            WHERE id = ?
        """
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM artists
            WHERE LOWER(name) = LOWER(?)
        """
        row = CURSOR.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row) if row else None
