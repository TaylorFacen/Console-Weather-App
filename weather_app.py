import requests

from config import DARK_SKY_API_KEY

def get_weather(latitude, longitude):
    url = "https://api.darksky.net/forecast/{}/{},{}".format(DARK_SKY_API_KEY, latitude, longitude)

    response = requests.get(url)
    data = response.json()

    current_weather = data['currently']
    summary = current_weather['summary'].lower()
    temperature = current_weather['temperature']

    message = "Currently, it's {} degrees outside. There's also {}.".format(temperature, summary)
    print(message)


if __name__ == "__main__":
    get_weather(latitude = 37.8267, longitude = -122.4233)