import random

class JoyRandomiser():

    def __init__(self, quotation_list, song_list):
        self.quotation_list = quotation_list
        self.song_list = song_list
        self.random_result = ''

    def randomise(self):
        self.random_result = f'Here\'s your random quotation: {random.choice(self.quotation_list)} and for your random song, you got... {random.choice(self.song_list)}'
        return self.random_result
    

my_quotation_list = [
'quote1',
'quote2',
'quote3'
]

my_song_list = [
'song1',
'song2',
'song3'
]

joy_randomiser = JoyRandomiser(my_quotation_list, my_song_list)
joy_randomiser.randomise()
print(joy_randomiser.random_result)



