from lib.makers_joy_challenge import JoyList
from lib.makers_joy_challenge import JoyRandomiser

# Test that the joy randomiser spits out a random quotation
# and a random song with description
def test_joy_randomiser():
    joy_randomiser = JoyRandomiser()
    result = joy_randomiser.randomise()
    assert result == any(JoyList.quotation_list) + any(JoyList.song_list)