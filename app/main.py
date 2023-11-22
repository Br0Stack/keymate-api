from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from .routers import search
import os

app = FastAPI()

api_key_header = APIKeyHeader(name='X-API-KEY')

# Get the API key from the .env file
api_key = os.environ["OPENAI_API_KEY"]

def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != "expected_api_key":  # Replace with your actual API key
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )

app.include_router(search.router, dependencies=[Depends(get_api_key)])
