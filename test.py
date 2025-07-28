import requests
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = "http://127.0.0.1:8000/generate"
headers = {
    "x-api-key": os.getenv("API_KEY"),
    "Content-Type": "application/json"
}
params = {"query": "Tell me about FastAPI"}

response = requests.post(endpoint, headers=headers, params=params)
print(response.json())
