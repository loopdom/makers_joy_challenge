from lib.song import Song

def test_song_constructs():
    song = Song(1,'Dogs','utube.com/dogs','VvSad')
    assert song.id == 1
    assert song.name == 'Dogs'
    assert song.link == 'utube.com/dogs'
    assert song.mood == 'VvSad'

def test_song_equals():
    song1 = Song(1,'Dogs','utube.com/dogs','VvSad')
    song2 = Song(1,'Dogs','utube.com/dogs','VvSad')
    assert song1 == song2

def test_song_repr():
    song = Song(1,'Dogs','utube.com/dogs','VvSad')
    assert str(song) == 'Song(1, Dogs, utube.com/dogs, VvSad)'