import json

raw_json = """
{
  "city": "Warsaw",
  "weather": [{"main": "Clouds", "description": "overcast clouds"}],
  "main": {"temp": 15.2, "humidity": 82},
  "wind": {"speed": 5.1}
}
"""

data = json.loads(raw_json)

print(type(data))
print("City:", data["city"])
print("Temperature:", data["main"]["temp"])