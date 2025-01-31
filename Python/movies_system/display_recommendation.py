from termcolor import colored
def display_recommendations(filtered_movies):
    if filtered_movies:
        print("\nRecommended Movies: \n")
        for movie in filtered_movies:
            print(f"{colored(movie['name'],"red")}:- "
                f"{colored('Genre','cyan')}: {movie['genre']}, " +
                f"{colored('Language','cyan')}: {movie['Language']}, " +
                f"{colored('Rating','cyan')}: {movie['rating']}, " +
                f"{colored('Year','cyan')}: {movie['year']}, " +
                f"{colored('Duration','cyan')}: {movie['duration']}\n")
    else:
        print("\nNo movies match your preferences.\n")