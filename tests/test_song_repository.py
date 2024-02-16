from lib.song_repository import *
from lib.song import *
from lib.database_connection import *

"""
When I call #all on SongRepository
I get all the songs back in a list 
"""

def test_lists_all_songs(db_connection):
    db_connection.seed("seeds/joy_challenge_tables.sql")
    repository = SongRepository(db_connection)
    result = repository.all()
    assert result == [
        Song('Belfast', 'something classic', 'https://www.youtube.com/watch?v=d5vGjCoQM1s', 'reflective'),
        Song('Why', 'something banging', 'https://www.youtube.com/watch?v=BmTj8zkDBbM', 'bitter'),
        Song('Alien Observer', 'something from space', 'https://www.youtube.com/watch?v=eVqFnuaW4JQ', 'reflective'),
    ]


def test_select_by_mood(db_connection):
    db_connection.seed("seeds/joy_challenge_tables.sql")
    repository = SongRepository(db_connection)
    result = repository.select_mood('reflective')
    assert result == [
        Song('Belfast', 'something classic', 'https://www.youtube.com/watch?v=d5vGjCoQM1s', 'reflective'),
        Song('Alien Observer', 'something from space', 'https://www.youtube.com/watch?v=eVqFnuaW4JQ', 'reflective'),
    ]
    
