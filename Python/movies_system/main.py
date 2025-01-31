from display_recommendation import *
from filter_movies import *
from movies import *
from user_input import *



#Initialize movie data
movies = initialize_movies()

#Get user preferences               
preferences = get_user_input()  

#Filter movies     
filtered_movies = filter_movies(movies, preferences)

#Display recommendations
display_recommendations(filtered_movies)
