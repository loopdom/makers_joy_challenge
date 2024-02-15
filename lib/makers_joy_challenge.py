import random

class JoyRandomiser():

    def __init__(self, quotation_list, song_list):
        self.quotation_list = quotation_list
        self.song_list = song_list
        self.random_result = ''
  
    def randomise(self):
        self.random_result = f'''
        Thanks for using the randomiser!
        Here\'s your random quotation from Octavia Butler's Parables:

        {random.choice(self.quotation_list)}
        
        and for your random song, you got...

        {random.choice(self.song_list)}!
        '''
        return self.random_result

my_quotation_list = [
        '''All that you touch You Change.
        All that you Change Changes you.
        The only lasting truth Is Change.''',
        '''The child in each of us
        Knows paradise.
        Paradise is home.
        Home as it was
        Or home as it should have been.

        Paradise is one's own place,
        One's own people,
        One's own world,
        Knowing and known,
        Perhaps even
        Loving and loved.

        Yet every child
        Is cast from paradise-
        Into growth and new community,
        Into vast, ongoing
        Change.''',
        '''Kindness eases change.
        Love quiets fear.
        And a sweet and powerful
        Positive obsession
        Blunts pain,
        Diverts rage,
        And engages each of us
        In the greatest,
        The most intense
        Of our chosen struggles.'''
]

my_song_list = [
        '''something classic:
        https://www.youtube.com/watch?v=d5vGjCoQM1s''',
        '''something classical:
        https://www.youtube.com/watch?v=0U6sWqfrnTs''',
        '''something banging:
        https://www.youtube.com/watch?v=BmTj8zkDBbM''',
        '''something wistful:
        https://www.youtube.com/watch?v=-LgQhfusf_E''',
        '''something about being a lovely horse!
        https://www.youtube.com/watch?v=dYFrpG9VqU8''',
        '''something with a nice beat:
        https://www.youtube.com/watch?v=Rfhx7ZdmUpk&pp=ygUKdGlyemFoIGYyMg%3D%3D''',
        '''something from space:
        https://www.youtube.com/watch?v=eVqFnuaW4JQ''',
        '''something funky:
        https://www.youtube.com/watch?v=GRdYqxakKIE''',
        '''something to cure your headache (or give you a new one...):
        https://www.youtube.com/watch?v=VpoOjoiYcWY''',
        '''something to get you in the code zone:
        https://www.youtube.com/watch?v=GGi6CygbpNQ'''
]

joy_randomiser = JoyRandomiser(my_quotation_list, my_song_list)
joy_randomiser.randomise()
print(joy_randomiser.random_result)