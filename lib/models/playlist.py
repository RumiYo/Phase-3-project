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
