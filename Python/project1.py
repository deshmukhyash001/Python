# Step 1: Initialize movie data
def initialize_movies():
    movies = [
        {"name": "Inception", "genre": "sci-fi", "rating": 8.8, "year": 2010},
        {"name": "The Dark Knight", "genre": "action", "rating": 9.0, "year": 2008},
        {"name": "Interstellar", "genre": "sci-fi", "rating": 8.6, "year": 2014},
        {"name": "Parasite", "genre": "thriller", "rating": 8.6, "year": 2019},
        {"name": "Avengers: Endgame", "genre": "action", "rating": 8.4, "year": 2019},
        {"name": "Joker", "genre": "drama", "rating": 8.5, "year": 2019},
        {"name": "Toy Story 4", "genre": "animation", "rating": 7.8, "year": 2019},
        {"name": "The Matrix", "genre": "sci-fi", "rating": 8.7, "year": 1999},
        {"name": "Gladiator", "genre": "action", "rating": 8.5, "year": 2000},
        {"name": "Forrest Gump", "genre": "drama", "rating": 8.8, "year": 1994}
    ]
    return movies


# Step 2: Get user preferences
def get_user_preferences():
    genre = input("Enter preferred genre (e.g., Action, Sci-Fi, Drama, etc.): ")
    genre.lower() 
    min_rating = float(input("Enter minimum rating (0-10): "))
    year = int(input("Enter minimum release year: "))
    return {"genre": genre, "min_rating": min_rating, "year": year}

# Step 3: Filter movies based on preferences
def filter_movies(movies, preferences):
    filtered_movies = []
    for movie in movies:
        if (movie["genre"]== preferences["genre"] and
            movie["rating"] >= preferences["min_rating"] and
            movie["year"] >= preferences["year"]):
            filtered_movies.append(movie)
    return filtered_movies

# Step 4: Display recommended movies
def display_recommendations(filtered_movies):
    if filtered_movies:
        print("\nRecommended Movies:")
        for movie in filtered_movies:
            print(f"{movie['name']} - Genre: {movie['genre']}, Rating: {movie['rating']}, Year: {movie['year']}")
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
