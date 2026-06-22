"""
Weather Checker (Web)
------------------------
A Flask web app that lets the user check the current weather
for any city by name. Uses the free Open-Meteo API for both
geocoding and weather data. Web version of the console-based
weather_app project.
"""

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

WEATHER_ICONS = {
    0: "☀️", 1: "🌤️", 2: "⛅", 3: "☁️",
    51: "🌦️", 61: "🌧️", 71: "🌨️", 80: "🌦️",
    95: "⛈️"
}


def get_weather_icon(code):
    """Returns an emoji icon for a given weather code.

    Args:
        code (int): weather code returned by the API.

    Returns:
        str: emoji representing the weather, or a generic thermometer
        if the code isn't mapped.
    """
    return WEATHER_ICONS.get(code, "🌡️")


def get_coordinates(city):
    """Looks up a city's coordinates, name, region, and country.

    Args:
        city (str): name of the city to search for.

    Returns:
        tuple: (latitude, longitude, name, country, region), or all
        None values if the city wasn't found.
    """
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)
    data = response.json()
    if "results" in data:
        result = data["results"][0]
        admin1 = result.get("admin1", "")  # region/state
        return result["latitude"], result["longitude"], result["name"], result["country"], admin1
    return None, None, None, None, None


def get_weather(lat, lon):
    """Fetches the current weather for a given coordinate pair.

    Args:
        lat (float): latitude.
        lon (float): longitude.

    Returns:
        dict: current weather data (temperature, wind, humidity, code).
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,windspeed_10m,weathercode,relativehumidity_2m&timezone=auto"
    response = requests.get(url)
    return response.json()["current"]


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    city_name = None
    error = None
    icon = None

    if request.method == "POST":
        city = request.form["city"]
        lat, lon, city_name, country, admin1 = get_coordinates(city)
        if lat:
            weather = get_weather(lat, lon)
            city_name = f"{city_name}, {admin1}, {country}"
            icon = get_weather_icon(weather["weathercode"])
        else:
            error = f"City '{city}' not found"

    return render_template("index.html", weather=weather, city=city_name, error=error, icon=icon)


if __name__ == "__main__":
    app.run(debug=True)