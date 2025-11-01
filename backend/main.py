import os
import requests

from dotenv import load_dotenv
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.utils import print_message

app = FastAPI()

# allow frontend requests (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # for dev, loosened
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/weather")
def get_weather(city:str=Query(..., description="City name")):

    load_dotenv("config.env")
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise EnvironmentError(print_message("fail", "No valid API key"))

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        print_message("fail", f"Could not fetch weather for {city}")
        if response.status_code == 401:
            print_message("fail", "Invalid API key")
            raise HTTPException(status_code=401, detail="Invalid API key")
        elif response.status_code == 404:
            print_message("fail", f"City '{city}' not found")
            raise HTTPException(status_code=404, detail=f"City '{city}' not found")
        else:
            print_message("fail", "Unexpected error from weather service")
            raise HTTPException(status_code=500, detail="Unexpected error from weather service")
    
    print_message("pass", f"Successfully fetched weather for {city}")
    return response.json()