class Movie:
    class_counter = 1
    def __init__(self, title, rating, genre,watched):
        self.title = title
        self.rating = rating
        self.genre = genre
        self.watched = watched
        self.id = Movie.class_counter
        Movie.class_counter +=1

    def __repr__(self):
        return f'__id: {self.id}, Title: {self.title}, Rating: {self.rating}, Genre: {self.genre}'

    def __str__(self):
        return f'ID :{self.id}, title: {self.title}, rating: {self.rating}, genre: {self.genre}'
