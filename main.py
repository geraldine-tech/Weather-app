import requests


def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]

        temp = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']

        forecast = (f"Temperature: {temp}°C\n"
                    f"Pressure: {pressure} hPa\n"
                    f"Humidity: {humidity}%\n"
                    f"Weather: {description.capitalize()}")

        return forecast
    else:
        return "City not found or API request failed."


# Example usage
city_name = "London"
api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
print(get_weather(city_name, api_key))
