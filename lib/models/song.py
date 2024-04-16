from models.__init__ import CURSOR, CONN

class Song:

    all = {}

    def __init__(self, name, year, id=None):
        self.id = id 
        self.name = name
        self.year = year