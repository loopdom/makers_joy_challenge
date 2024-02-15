class Quote():

    def __init__(self, id, content, author, mood):
        self.id = id
        self.content = content
        self.author = author
        self.mood = mood
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Quote({self.id}, {self.content}, {self.author}, {self.mood})'