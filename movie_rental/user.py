from movie_class import Movie

class User:
    class_counter = 1
    def __init__(self, name):
        self.name = name
        self.id = User.class_counter
        self.movies = []
        User.class_counter+=1

    def __repr__(self):
        return f"Name {self.name}, id{self.id}"

    def add_movie(self, name, rating, genre, watched):
        movie = Movie(name, rating, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.title != name, self.movies))

    def watched_movies(self):
        movies_watched = list(filter(lambda movie: movie.watched, self.movies))
        return movies_watched

    def set_watched(self, name):
        for movie in self.movies:
            if movie.title == name:
                movie.watched == True



    def json(self):
        return {
            'name':self.name,
            'movies':[movie.json() for movie in self.movies]
        }

    @classmethod
    def from_json(cls, data):
        user = cls(data['name'])
        for movie in data['movies']:
            user.movies.append(Movie.from_json(movie))
        return user