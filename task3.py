data = {
    "city": "Warsaw",
    "main": {
        "temp": 15.2,
        "feels_like": 13.8,
        "humidity": 82
    },
    "wind": {
        "speed": 5.1,
        "deg": 270
    },
    "weather": [
        {"main": "Clouds", "description": "overcast clouds"}
    ]
}

temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]

print(f"Temperature: {temp}°C")
print(f"Humidity: {humidity}%")
print(f"Wind speed: {wind_speed} m/s")

feels_like = data["main"].get("feels_like", "N/A")
visibility = data.get("visibility", "N/A") 

print(f"Feels like: {feels_like}°C")
print(f"Visibility: {visibility}")