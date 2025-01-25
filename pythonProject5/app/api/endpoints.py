from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Data model for request validation
class UserMovies(BaseModel):
    user_movies: List[str]

# Endpoint to receive the movie list
@app.post("/recommend")
async def recommend_movies(data: UserMovies):
    user_movies = data.user_movies  # The movies the user has inputted
    # Here you would call your recommendation logic
    recommendations = generate_recommendations(user_movies)
    return {"recommendations": recommendations}

# Mock recommendation function
def generate_recommendations(user_movies):
    # For simplicity, this mock function just returns some static movies
    return ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"]
