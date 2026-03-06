import requests
import json

API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city: str) -> dict:
    """Fetch weather data for a given city from OpenWeatherMap."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params, timeout=10)

    if response.status_code == 404:
        raise ValueError(f"City '{city}' not found. Please check the name and try again.")
    if response.status_code == 401:
        raise PermissionError("Invalid API key. Get a free key at https://openweathermap.org/api")
    if response.status_code != 200:
        raise ConnectionError(f"Unexpected error: HTTP {response.status_code}")

    return response.json()


def parse_weather(data: dict) -> dict:
    """Extract the important fields from the raw API response."""
    return {
        "city":        data["name"],
        "country":     data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like":  data["main"]["feels_like"],
        "temp_min":    data["main"]["temp_min"],
        "temp_max":    data["main"]["temp_max"],
        "humidity":    data["main"]["humidity"],
        "condition":   data["weather"][0]["main"],
        "description": data["weather"][0]["description"].capitalize(),
        "wind_speed":  data["wind"]["speed"],
        "visibility":  data.get("visibility", "N/A"),
    }


def display_weather(info: dict) -> None:
    """Print the weather data in a clean, formatted layout."""
    visibility = (
        f"{info['visibility'] / 1000:.1f} km"
        if isinstance(info["visibility"], int)
        else info["visibility"]
    )

    print()
    print("=" * 45)
    print(f"  Weather Report — {info['city']}, {info['country']}")
    print("=" * 45)
    print(f"  Condition    : {info['description']}")
    print(f"  Temperature  : {info['temperature']}°C  (feels like {info['feels_like']}°C)")
    print(f"  Range        : {info['temp_min']}°C – {info['temp_max']}°C")
    print(f"  Humidity     : {info['humidity']}%")
    print(f"  Wind Speed   : {info['wind_speed']} m/s")
    print(f"  Visibility   : {visibility}")
    print("=" * 45)
    print()


def main():
    print("\n🌤  Weather Data Analyzer")
    print("-" * 45)

    city = input("Enter a city name: ").strip()

    if not city:
        print("Error: City name cannot be empty.")
        return

    print(f"\nFetching weather for '{city}'...")

    try:
        raw_data = fetch_weather(city)
        weather  = parse_weather(raw_data)
        display_weather(weather)

        show_raw = input("Show raw JSON response? (y/n): ").strip().lower()
        if show_raw == "y":
            print()
            print(json.dumps(raw_data, indent=2))

    except ValueError as e:
        print(f"\n City error: {e}")
    except PermissionError as e:
        print(f"\n Auth error: {e}")
    except ConnectionError as e:
        print(f"\n Connection error: {e}")
    except requests.exceptions.ConnectionError:
        print("\n Network error: Could not reach the API. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("\n Timeout: The request took too long. Try again.")


if __name__ == "__main__":
    main()