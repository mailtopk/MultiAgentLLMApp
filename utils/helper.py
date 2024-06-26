import os
from dotenv import load_dotenv, find_dotenv

def load_env():
    _ = load_dotenv(find_dotenv())

def get_open_ai_model_and_key():   
    load_env()
    key = os.getenv("OPEN_API_KEY")
    model = os.getenv("MODEL")
    return key, model

def get_tavily_api_key():
    key = os.getenv("TAVILY_API_KEY")
    return key

if __name__ == "__main__":
    print(get_open_ai_model_and_key())