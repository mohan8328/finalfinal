from transformers import pipeline

def initialize_llm():
    """
    Initialize the Hugging Face pipeline for text generation.
    """
    return pipeline("text-generation", model="gpt2")

llm = initialize_llm()

async def fetch_llm_recommendations(movie_list):
    """
    Use the LLM to generate movie recommendations based on input.
    """
    prompt = f"Based on the following movies: {', '.join(movie_list)}, recommend 5 other movies with explanations."
    response = llm(prompt, max_length=150, num_return_sequences=1)
    generated_text = response[0]["generated_text"]

    # Extract recommendations (simple parsing)
    return generated_text.split("\n")[:5]  # First 5 lines as recommendations
