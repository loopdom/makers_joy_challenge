from lib.quote_repository import QuoteRepository
from lib.quote import Quote

def test_quote_all(db_connection):
    db_connection.seed('seeds/joy_challenge_tables.sql')

    quote_repository = QuoteRepository(db_connection)

    result = quote_repository.all()

    assert result == [
        Quote(1, 'All that you touch You Change. All that you Change Changes you. The only lasting truth Is Change.', 'Octavia Butler', 'reflective'),
        Quote(2, 'The child in each of us Knows paradise.Paradise is home. Home as it was Or home as it should have been. Paradise is one`s own place, One`s own people, One`s own world, Knowing and known, Perhaps even Loving and loved. Yet every child Is cast from paradise- Into growth and new community, Into vast, ongoing Change.', 'Octavia Butler' , 'reflective'),
        Quote(3, 'Kindness eases change. Love quiets fear. And a sweet and powerful Positive obsession Blunts pain, Diverts rage, And engages each of us In the greatest, The most intense Of our chosen struggles', 'Octavia Butler', 'reflective'),
        Quote(4, 'Hell is other people', 'J Paul Sarte','bitter'),
        Quote(5, 'So it`s true when all is said and done, grief is the price we pay for love ', 'E.A Bucchianeri','sad')
    ]

def test_select_by_mood(db_connection):
    db_connection.seed('seeds/joy_challenge_tables.sql')

    quote_repository = QuoteRepository(db_connection)

    result = quote_repository.select_mood('reflective')
    assert result == [
        Quote(1, 'All that you touch You Change. All that you Change Changes you. The only lasting truth Is Change.', 'Octavia Butler', 'reflective'),
        Quote(2, 'The child in each of us Knows paradise.Paradise is home. Home as it was Or home as it should have been. Paradise is one`s own place, One`s own people, One`s own world, Knowing and known, Perhaps even Loving and loved. Yet every child Is cast from paradise- Into growth and new community, Into vast, ongoing Change.', 'Octavia Butler' , 'reflective'),
        Quote(3, 'Kindness eases change. Love quiets fear. And a sweet and powerful Positive obsession Blunts pain, Diverts rage, And engages each of us In the greatest, The most intense Of our chosen struggles', 'Octavia Butler', 'reflective')
    ]