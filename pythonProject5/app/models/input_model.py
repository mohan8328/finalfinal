from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    user_movies: list[str]
