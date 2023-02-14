import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "813d8873885b254e6f67753bb793a6bd"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)
def get_gmail() -> Dict:
    response = requests.get('https://gmail.googleapis.com/$discovery/rest?version=v1')
    return response.json()
# https://www.askpython.com/python/examples/connect-and-call-apis
def main():
    temp = get_weather("London")
    print(temp)

    print (get_gmail())

if __name__ == "__main__":
    main()