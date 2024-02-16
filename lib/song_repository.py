from lib.song import *

class SongRepository:
    def __init__(self, connection):
        self._connection = connection



    def all(self):
        rows = self._connection.execute("SELECT * FROM songs")
        songs = []
        for row in rows:
            song = Song(row['name'], row['description'], row['link'], row['mood'])
            songs.append(song)
        return songs
    
    def select_mood(self, mood):
        rows = self._connection.execute("SELECT * FROM songs WHERE mood = %s", [mood])
        songs = []
        for row in rows:
            song = Song(row['name'], row['description'], row['link'], row['mood'])
            songs.append(song)
        return songs

