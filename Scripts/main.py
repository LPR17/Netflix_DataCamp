#Importing NumPy, Matplotlib & Pandas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Function to calculate the amount of action movies in the 90s
def ActionMovieCount (DF):
    DF_count = 0
    for movie in DF.iterrows():
        DF_count += 1
    return DF_count


#Function to caclulate the most frequent movie duration in the 90s
def ModeDurationMoves (DF):
    most_frequent = DF['duration'].mode()[0] #Used the 
    return most_frequent


#Ejecutamos desde el directorio de Scripts
netflix_df = pd.read_csv("../Data/netflix_data.csv")

#Defined the dataframe containing all the movies from the 90s
nineties_movies = netflix_df[(netflix_df["release_year"].between(1990, 1999))]

#Defined the dataframe cointaining all the action movies from the 90s that are less than 90 minutes
short_action_movies = nineties_movies[(nineties_movies["genre"] == "Action") & (nineties_movies["duration"] < 90)]


short_movie_count = ActionMovieCount(short_action_movies)
duration = ModeDurationMoves(nineties_movies)



#Print the results
print(f"The most frequent duration of 90s movies is {duration}")
print(f"The amount of action movies in the 90s is : {short_movie_count}")