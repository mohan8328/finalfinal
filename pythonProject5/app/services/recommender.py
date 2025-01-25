from app.utils.llm_helper import fetch_llm_recommendations

def generate_recommendations(user_movies: list):
    # This function gets recommendations based on the user-provided movie list
    try:
        recommendations = fetch_llm_recommendations(user_movies)
        return recommendations
    except Exception as e:
        return {"error": str(e)}
