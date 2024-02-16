from lib.quote_repository import QuoteRepository
from lib.quote import Quote
import random
from lib.database_connection import DatabaseConnection

class JoyRandomiser():

    def __init__(self, connection):
        self.connection = connection
        self.quotation_list = []
        # self.song_list = song_list
        self.random_result = ''

    def randomise(self, mood):
        quote_repository = QuoteRepository(self.connection)
        self.quotation_list = quote_repository.select_mood(mood)

        self.random_result = f'''
        Thanks for using the randomiser!
        Here\'s your random quotation from Octavia Butler's Parables:

        {random.choice(self.quotation_list)}
        
        and for your random song, you got...

        No songs right now!
        '''
        return self.random_result

database_connection = DatabaseConnection()
database_connection.connect()
joy_randomiser = JoyRandomiser(database_connection)
joy_randomiser.randomise('reflective')
print(joy_randomiser.random_result)