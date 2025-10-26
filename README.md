# Forecast-Risky

Weather software for [2025 NASA Space Apps Challenge](https://www.spaceappschallenge.org/): [Will It Rain On My Parade?](https://www.spaceappschallenge.org/2025/challenges/will-it-rain-on-my-parade/)

## Repository Structure
Forecast-Risky/\
│\
├── src/\
│   ├── __init__.py\
│   ├── api.py          # get weather data\
│   ├── location.py     # location detection (IP lookup)\
│   └── utils.py        # helper functions\
│\
└── main.py             # entry point

cli: streamlit run main.py