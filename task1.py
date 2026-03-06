import requests

API_KEY = "your_api_key_here"
CITY = "Warsaw"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

response.raise_for_status()

data = response.json()

print("Status code:", response.status_code)
print("Raw response:", data)