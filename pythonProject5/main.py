from fastapi import FastAPI
from app.services.recommender import generate_recommendations

app = FastAPI()

@app.post("/recommend")
async def get_recommendations(user_movies: list):
    recommendations = generate_recommendations(user_movies)
    return {"recommendations": recommendations}
