from models.__init__ import CURSOR, CONN

class User:

    all = {}

    GENDERS = {
        1: "Male",
        2: "Female",
        3: "Non-Binary",
        4: "Prefer not to say"
    }

    def __init__(self, name, birth_year, gender, email, password, id=None):
        self.id = id
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.email = email
        self.password = password

    def __repr__(self):
        return (
            f"<User {self.name} (Gender: {self.gender}, Birth year: {self.birth_year}, Email address: {self.email})"
        )

    @classmethod
    def exists_in_all(cls, name):
        for user in cls.all.values():
            if user.name == name:
                return True
        return False

    @property 
    def name(self):
        return self._name 

    @name.setter 
    def name(self, name):
        if isinstance(name, str) and len(name):
            if not self.exists_in_all(name):
                self._name = name
            else:
                raise TypeError(f"{name} already exists. Name must be unique.")
        else:
            raise TypeError ("Name mst be a non-empty string.")


    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, birth_year):
        if isinstance(birth_year, int) and 1930<= birth_year <= 2024:
            self._birth_year = birth_year
        else:
            raise TypeError ("Birth year must be a number and between 1930 and 2024")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender): 
        if isinstance(gender, int) and 1 <= gender <= 4 :
            self._gender = gender
        else:
            raise TypeError ("Select your gender from the options")

    @property 
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and "@" in email:
            self._email = email
        else:
            raise TypeError("Please type email address")

    @property 
    def password(self):
        return self._password 

    @password.setter
    def password(self, password):
        if isinstance(password, str) and len(password)>= 8:
            self._password = password
        else:
            raise TypeError("Password must be longer than 8 charactors")


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                birth_year INTEGER,
                gender INTEGER,
                email TEXT,
                password TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS users;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO users (name, birth_year, gender, email,password)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.birth_year, self.gender, self.email, self.password))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE users
            SET name = ?, birth_year = ?, gender = ?, email = ?, password = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.birth_year, self.gender, self.email, self.password))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM users
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id, ))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, birth_year, gender, email, password):
        user = cls(name, birth_year, gender, email, password)
        user.save()
        return user
    
    @classmethod
    def instance_from_db(cls, row):
        user = cls.all.get(row[0])
        if user: 
            user.name = row[1]
            user.birth_year = row[2]
            user.gender = row[3]
            user.email = row[4]
            user.password = row[5]
        else:
            user = cls(row[1], row[2], row[3], row[4], row[5])
            user.id = row[0]
            cls.all[user.id] = user
        return user

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM users
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT  * FROM users
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id, )).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT  * FROM users
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name, )).fetchone()
        return cls.instance_from_db(row) if row else None
