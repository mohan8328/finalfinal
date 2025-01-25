import os

class Config:
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt2")  # Default to GPT-2
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))
