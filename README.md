# LLMConnectAPI 

LLMConnectAPI is a FastAPI-based project that provides a secure API interface to interact with a local LLM (such as Mistral via Ollama). It uses API key authentication and manages per-key credit limits for controlled access.

## Features

- API key authentication
- Credit tracking per key
- Generate responses via local LLM (Mistral)
- Test client included

## Project Structure

LLMConnectAPI/
├── main.py             # FastAPI server with credit-based key authentication
├── text.py             # Client script to test API interaction
├── .env                # Environment file with your API key
├── requirements.txt    # Dependency list

## Setup Instructions

1. Clone the repository
```
git clone https://github.com/your-username/LLMConnectAPI.git
cd LLMConnectAPI
```

2. Create a `.env` file
```
API_KEY=your_secret_key
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Start the FastAPI server
```
uvicorn main:app --reload
```

5. Run the test script
```
python text.py
```

## API Endpoint

### POST /generate

**Query parameter:**
- `prompt` – The prompt to send to the LLM

**Headers:**
- `x-api-key` – Your API key from `.env`

**Example:**
```
curl -X POST "http://127.0.0.1:8000/generate?prompt=Tell me about Python"      -H "x-api-key: your_secret_key"
```

## API Credit Logic

- Each API key starts with 5 credits (modifiable in `main.py`)
- Each request reduces 1 credit
- If credits are exhausted, a 403 error is returned

## Tech Stack Used

- FastAPI
- Ollama
- Python
- Mistral
