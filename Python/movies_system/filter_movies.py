def filter_movies(movies, preferences):
    filtered_movies = []
    for movie in movies:
        if (movie["genre"].lower()== preferences["genre"].lower() and
            movie["Language"].lower()== preferences["Language"].lower() and
            movie["rating"] >= preferences["min_rating"] and
            movie["year"] >= preferences["year"]):
            filtered_movies.append(movie)
    return filtered_movies