from movie_class import Movie
from user import User

first_movie = Movie('Rambo',4,'Action',False)
second_movie = Movie('Matrix',5,'Sci-fi',True)
# print(first_movie)
# print(second_movie)

first_user = User('Alex')
print(first_user)

first_user.movies.append(first_movie)
first_user.movies.append(second_movie)

print(first_user.movies)

print(first_user.watched_movies())

first_user.add_movie('Batman',4,'Action',False)
print(first_user.movies)

first_user.delete_movie("Batman")
print(first_user.movies)