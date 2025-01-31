# Step 1: Initialize movie data
def initialize_movies():
    movies = [
    {"name": "Inception", "genre": "Sci-fi", "rating": 8.8, "year": 2010, "Language": "English", "duration": "2.28 hrs"},  
    {"name": "The Dark Knight", "genre": "Action", "rating": 9.0, "year": 2008, "Language": "English", "duration": "2.32 hrs"},  
    {"name": "Interstellar", "genre": "Sci-fi", "rating": 8.6, "year": 2014, "Language": "English", "duration": "2.49 hrs"},  
    {"name": "Parasite", "genre": "Thriller", "rating": 8.6, "year": 2019, "Language": "Korean", "duration": "2.12 hrs"},  
    {"name": "Avengers: Endgame", "genre": "Action", "rating": 8.4, "year": 2019, "Language": "English", "duration": "3.1 hrs"},  
    {"name": "Joker", "genre": "Drama", "rating": 8.5, "year": 2019, "Language": "English", "duration": "2.02 hrs"},  
    {"name": "Toy Story 4", "genre": "Animation", "rating": 7.8, "year": 2019, "Language": "English", "duration": "1.40 hrs"},  
    {"name": "The Matrix", "genre": "Sci-fi", "rating": 8.7, "year": 1999, "Language": "English", "duration": "2.16 hrs"},  
    {"name": "Gladiator", "genre": "Action", "rating": 8.5, "year": 2000, "Language": "English", "duration": "2.35 hrs"},  
    {"name": "Forrest Gump", "genre": "Drama", "rating": 8.8, "year": 1994, "Language": "English", "duration": "2.22 hrs"},  
    {"name": "Dangal", "genre": "Drama", "rating": 8.4, "year": 2016, "Language": "Hindi", "duration": "2.41 hrs"},  
    {"name": "Lagaan", "genre": "Drama", "rating": 8.1, "year": 2001, "Language": "Hindi", "duration": "3.44 hrs"},  
    {"name": "The Host", "genre": "Horror", "rating": 7.1, "year": 2006, "Language": "Korean", "duration": "2.00 hrs"},  
    {"name": "Infernal Affairs", "genre": "Thriller", "rating": 8.0, "year": 2002, "Language": "Chinese", "duration": "1.58 hrs"},  
    {"name": "Marathi Tiger", "genre": "Action", "rating": 7.5, "year": 2015, "Language": "Marathi", "duration": "2.10 hrs"},  
    {"name": "Court", "genre": "Drama", "rating": 7.7, "year": 2014, "Language": "Marathi", "duration": "1.50 hrs"},  
    {"name": "Pain and Glory", "genre": "Drama", "rating": 7.6, "year": 2019, "Language": "Spanish", "duration": "1.52 hrs"},  
    {"name": "The Platform", "genre": "Horror", "rating": 7.0, "year": 2019, "Language": "Spanish", "duration": "1.52 hrs"},  
    {"name": "Raise the Red Lantern", "genre": "Drama", "rating": 8.1, "year": 1991, "Language": "Chinese", "duration": "2.17 hrs"},  
    {"name": "Train to Busan", "genre": "Action", "rating": 7.6, "year": 2016, "Language": "Korean", "duration": "1.58 hrs"},  
    {"name": "Zindagi Na Milegi Dobara", "genre": "Drama", "rating": 8.2, "year": 2011, "Language": "Hindi", "duration": "2.35 hrs"},  
    {"name": "Drishyam", "genre": "Thriller", "rating": 8.2, "year": 2015, "Language": "Hindi", "duration": "2.43 hrs"},  
    {"name": "Baahubali: The Beginning", "genre": "Action", "rating": 8.0, "year": 2015, "Language": "Hindi", "duration": "2.39 hrs"},  
    {"name": "Three Idiots", "genre": "Comedy", "rating": 8.4, "year": 2009, "Language": "Hindi", "duration": "2.51 hrs"},  
    {"name": "Yeh Ballet", "genre": "Drama", "rating": 7.6, "year": 2020, "Language": "Hindi", "duration": "1.57 hrs"},  
    {"name": "Roma", "genre": "Drama", "rating": 7.7, "year": 2018, "Language": "Spanish", "duration": "2.15 hrs"},  
    {"name": "Y Tu Mamá También", "genre": "Drama", "rating": 7.7, "year": 2001, "Language": "Spanish", "duration": "1.46 hrs"},  
    {"name": "House of Flying Daggers", "genre": "Action", "rating": 7.5, "year": 2004, "Language": "Chinese", "duration": "1.59 hrs"},  
    {"name": "Farewell My Concubine", "genre": "Drama", "rating": 8.1, "year": 1993, "Language": "Chinese", "duration": "2.31 hrs"},  
    {"name": "Oldboy", "genre": "Thriller", "rating": 8.4, "year": 2003, "Language": "Korean", "duration": "2.00 hrs"},  
    {"name": "Burning", "genre": "Drama", "rating": 7.5, "year": 2018, "Language": "Korean", "duration": "2.28 hrs"},  
    {"name": "Sairat", "genre": "Romance", "rating": 8.3, "year": 2016, "Language": "Marathi", "duration": "2.54 hrs"},  
    {"name": "Natsamrat", "genre": "Drama", "rating": 8.9, "year": 2016, "Language": "Marathi", "duration": "2.46 hrs"},  
    {"name": "Fandry", "genre": "Drama", "rating": 8.3, "year": 2013, "Language": "Marathi", "duration": "1.45 hrs"}  
]

    return movies


# Step 2: Get user preferences
def get_user_preferences():
    genre = input("Enter preferred genre (e.g., Action, Sci-Fi, Drama, etc.): ")
    language = input("Enter preferred Language: ")
    min_rating = float(input("Enter minimum rating (0-10): "))
    year = int(input("Enter minimum release year: "))
    return {"genre": genre, "min_rating": min_rating, "year": year, "Language":language}

# Step 3: Filter movies based on preferences
def filter_movies(movies, preferences):
    filtered_movies = []
    for movie in movies:
        if (movie["genre"].lower()== preferences["genre"].lower() and
            movie["Language"].lower()== preferences["Language"].lower() and
            movie["rating"] >= preferences["min_rating"] and
            movie["year"] >= preferences["year"]):
            filtered_movies.append(movie)
    return filtered_movies

# Step 4: Display recommended movies
def display_recommendations(filtered_movies):
    if filtered_movies:
        print("\nRecommended Movies:")
        for movie in filtered_movies:
            print(f"{movie['name']} - Genre: {movie['genre']}, Language: {movie['Language']}, Rating: {movie['rating']}, Year: {movie['year']}, Duration: {movie['duration']}")
    else:
        print("\nNo movies match your preferences.")

# Main function to orchestrate the program
def main():
    movies = initialize_movies()                # Step 1: Initialize movie data
    preferences = get_user_preferences()        # Step 2: Get user preferences
    filtered_movies = filter_movies(movies, preferences)  # Step 3: Filter movies
    display_recommendations(filtered_movies)    # Step 4: Display recommendations

# Run the program
if __name__ == "__main__":
    main()
