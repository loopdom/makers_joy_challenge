class Song():

    def __init__(self, id, name, link, mood):
        self.id = id
        self.name = name
        self.link = link
        self.mood = mood
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Song({self.id}, {self.name}, {self.link}, {self.mood})'