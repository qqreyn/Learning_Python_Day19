import json

data = {
    "city": "Warsaw",
    "main": {"temp": 15.2, "humidity": 82},
    "forecast": [
        {"day": "Monday", "temp": 14.0, "condition": "Sunny"},
        {"day": "Tuesday", "temp": 11.5, "condition": "Rainy"},
    ]
}

compact = json.dumps(data)
print("Compact:")
print(compact)

pretty = json.dumps(data, indent=2)
print("\nPretty-printed:")
print(pretty)

sorted_output = json.dumps(data, indent=2, sort_keys=True)
print("\nSorted keys:")
print(sorted_output)

with open("weather_output.json", "w") as f:
    json.dump(data, f, indent=2)

print("\nSaved to weather_output.json")