# Forecast-Risky

Weather software for [2025 NASA Space Apps Challenge](https://www.spaceappschallenge.org/): [Will It Rain On My Parade?](https://www.spaceappschallenge.org/2025/challenges/will-it-rain-on-my-parade/)

## Repository Structure
Forecast-Risky/\
│\
├── backend/\
│   ├── src/\
│   │   ├── __init__.py\
│   │   └── utils.py\
│   ├── config.env          # API key\
│   └── main.py             # entry point\
│   └── requirements.txt    # python packages\
│\
├── frontend/\
│   ├── src/\
│   │   ├── components/\
│   │   │   └── WeatherCard.jsx\
│   │   └── App.jsx\
│   ├── index.html          # API key\
│   └── package.json             # entry point\
│   └── vite.config.js   # python dependencies\
│\
├── .gitignore\
├── LICENSE\
└── README.md

## Useage
- Backend: `uvicorn main:app --reload`
  - Install virtual environment: `python3 -m venv .venv`
  - Load dependencies: `pip install -r requirements.txt`
  - Grab API Key (free) from [OpenWeather](https://openweathermap.org/price)
    ```bash
    # config.env
    OPENWEATHER_API_KEY=YOUR_API_KEY_HERE
    ```