from lib.quote import Quote

class QuoteRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM quotes')

        quotes_list = []

        for row in rows:
            quote = Quote(row['id'], row['content'], row['author'], row['mood'])
            quotes_list.append(quote)

        return quotes_list
    
    def select_mood(self,select_mood):
        rows = self._connection.execute("SELECT * FROM quotes WHERE mood = %s", [select_mood])

        quotes_mood_list = []

        for row in rows:
            quote = Quote(row['id'], row['content'], row['author'], row['mood'])
            quotes_mood_list.append(quote)

        return quotes_mood_list