from lib.quote import Quote

def test_quote_constructs():
    quote = Quote(1,'Happy birthday','BirthdayMaria','VvHappy')
    assert quote.id == 1
    assert quote.content == 'Happy birthday'
    assert quote.author == 'BirthdayMaria'
    assert quote.mood == 'VvHappy'

def test_quote_equals():
    quote1 = Quote(1,'Happy birthday','BirthdayMaria','VvHappy')
    quote2 = Quote(1,'Happy birthday','BirthdayMaria','VvHappy')
    assert quote1 == quote2

def test_quote_repr():
    quote = Quote(1,'Happy birthday','BirthdayMaria','VvHappy')
    assert str(quote) == 'Quote(1, Happy birthday, BirthdayMaria, VvHappy)'