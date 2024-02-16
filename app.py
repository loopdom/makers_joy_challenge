from lib.quote_repository import QuoteRepository
from lib.song_repository import SongRepository
from lib.quote import Quote
import random
from lib.database_connection import DatabaseConnection

class JoyRandomiser():

    def __init__(self, connection):
        self.connection = connection
        self.quotation_list = []
        self.songs_list = []
        # self.song_list = song_list
        self.random_result = ''

    def randomise(self, mood):
        quote_repository = QuoteRepository(self.connection)
        song_repository = SongRepository(self.connection)

        self.quotation_list = quote_repository.select_mood(mood)
        self.songs_list = song_repository.select_mood(mood)

        quote = random.choice(self.quotation_list)
        song = random.choice(self.songs_list)

        self.random_result = f'''
        Thanks for using the randomiser!
        Here\'s your random {quote.mood} quotation by {quote.author}:

        {quote.content}
        
        and for your random {song.mood} song, you got...

        {random.choice(self.songs_list)}

        {song.name}
        #
        #
        # WHEN SONG.NAME ABOVE IS CALLED THE DESCRIPTION SHOWS UP INSTEAD ON THE TERMINAL.
        # WHEN WE CALL SONG.DESCRIPTION WE GOT AN ERROR OF 'Song' object has no attribute 'description'
        #
        #
        {song.link}
        '''
        return self.random_result

database_connection = DatabaseConnection()
database_connection.connect()
joy_randomiser = JoyRandomiser(database_connection)
joy_randomiser.randomise('reflective')
print(joy_randomiser.random_result)