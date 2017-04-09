import json
import urllib

import fresh_tomatoes
import movie_template

API_KEY = "insert API_KEY here"


# Establishing connection to API to retrieve trending movies using json module


def fetch_popular_api():
    connection = urllib.urlopen(
        "https://api.themoviedb.org/3/movie/popular?api_key=" + API_KEY + "&language=en-US&page=1")  # NOQA
    json_data = json.load(connection)
    return json_data["results"]


# Retrieving youtube URL from a second API call


def fetch_video_api(id):
    connection = urllib.urlopen(
        "https://api.themoviedb.org/3/movie/" + id + "/videos?api_key=" + API_KEY + "&language=en-US")  # NOQA
    json_data = json.load(connection)
    return "https://www.youtube.com/watch?v=" + json_data["results"][0]["key"]


# Initialising Movie objects and adding them to the list to be sent


movie_data = fetch_popular_api()
movie_list = []
for movie in movie_data:
    obj = movie_template.Movie(movie["title"], "https://image.tmdb.org/t/p/w500/" + movie["poster_path"],
                               fetch_video_api(str(movie["id"])))  # NOQA
    movie_list.append(obj)

# calling function from fresh_tomatoes script to build and launch website

fresh_tomatoes.open_movies_page(movie_list)
