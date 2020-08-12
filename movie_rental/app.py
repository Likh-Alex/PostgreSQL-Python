from user import User
import json
import os

def file_exists(filename):
    return os.path.isfile(filename)

def menu():
    username = input("Please enter your name: ")
    filename = f'{username}.txt'
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user=User(username)

    selection = input("Enter 'a' to add a movie, "
          "'s' to see the list of movies, "
          "'w' to set a movie as watched, "
          "'d' to delete a movie,"
          "'l' to see the list of watched movies, "
          "'q' to save and quit.")
    while selection != 'q':
        if selection == 'a':
            movie_name = input("Enter movie name")
            movie_rating = input("Enter movie rating")
            movie_genre = input("Enter movie genre")
            movie_watched = input("Enter if movie watched")
            user.add_movie(movie_name, movie_rating, movie_genre, movie_watched)

        elif selection == 's':
            for movie in user.movies:
                print(f"{movie.title}, {movie.rating}, {movie.genre}, {movie.watched}")
        elif selection == 'w':
            movie_watched = input("Enter a movie watched: ")
            if movie_watched in user.movies:
                print(f"Watched {movie_watched}")
                user.set_watched(movie_watched)
        elif selection == 'd':
            movie_to_delete = input("Enter a movie to delete: ")
            user.delete_movie(movie_to_delete)
            print(f"{movie_to_delete} deleted")
        elif selection == 'l':
            user.watched_movies()

        selection = input("Enter 'a' to add a movie, "
                          "'s' to see the list of movies, "
                          "'w' to set a movie as watched, "
                          "'d' to delete a movie,"
                          "'l' to see the list of watched movies, "
                          "'q' to save and quit.")

    with open(filename, 'w') as f:
        json.dump(user.json(), f)
        print("saved your files")



menu()