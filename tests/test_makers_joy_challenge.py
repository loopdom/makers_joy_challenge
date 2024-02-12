from lib.makers_joy_challenge import JoyRandomiser

# Test that the joy randomiser spits out a random quotation
# and a random song with description
def test_joy_randomiser():
    quotation_list = ['quote1', 'quote2']
    song_list = ['song1', 'song2']
    joy_randomiser = JoyRandomiser(quotation_list, song_list)
    result = joy_randomiser.randomise()
    assert result == f'Here\'s your random quotation: {any(quotation_list)} and for your random song, you got... {any(song_list)}'