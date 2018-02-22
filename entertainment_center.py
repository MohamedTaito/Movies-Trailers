# get fresh_tomato file and class file
from json import loads
import movies_trailers
import media


# get the movies  from the file
with open('movies.json', 'r') as json_data:
    movies = loads(json_data.read())


# creat array to get al movies
all_movies = []
for current_movie in movies:
    all_movies.append(media.Movie(json_movie=current_movie))

# call the function in fresh_tomatoes file
movies_trailers.open_movies_page(all_movies)
