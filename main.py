from fastapi import FastAPI, Header, HTTPException, Depends
import ollama
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

USER_CREDITS = {os.getenv("API_KEY"): 5}

def validate_key(api_key: str = Header(..., alias="x-api-key")):
    if api_key not in USER_CREDITS:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")
    if USER_CREDITS[api_key] <= 0:
        raise HTTPException(status_code=403, detail="Access Denied: No remaining credits")
    return api_key

@app.post("/generate")
def process_prompt(query: str, user_key: str = Depends(validate_key)):
    USER_CREDITS[user_key] -= 1
    try:
        reply = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": query}]
        )
        return {
            "reply": reply["message"]["content"],
            "credits_remaining": USER_CREDITS[user_key]
        }
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
