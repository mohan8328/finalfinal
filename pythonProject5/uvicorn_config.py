from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(
    title="Movie Recommendation Chat",
    description="A chat-like movie recommendation system.",
    version="1.0.0",
)

# Include the API endpoints
app.include_router(endpoints.router)
