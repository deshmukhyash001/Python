def get_user_input():
    genre = input("Enter preferred genre (e.g., Action, Sci-Fi, Drama, etc.): ")
    genre = genre.lower()
    language = input("Enter preferred Language: ")
    min_rating = float(input("Enter minimum rating (0-10): "))
    year = int(input("Enter minimum release year: "))
    return {"genre": genre, "min_rating": min_rating, "year": year, "Language":language}
