data = {
    "forecast": [
        {"day": "Monday",   "temp": 14.0, "condition": "Sunny"},
        {"day": "Tuesday",  "temp": 11.5, "condition": "Rainy"},
        {"day": "Wednesday","temp": 13.0, "condition": "Cloudy"},
        {"day": "Thursday", "temp": 16.2, "condition": "Sunny"},
        {"day": "Friday",   "temp": 9.8,  "condition": "Stormy"},
    ]
}

forecast = data["forecast"]

warm_days = []
for entry in forecast:
    if entry["temp"] > 13.0:
        warm_days.append(entry)

print("Warm days (>13°C):")
for day in warm_days:
    print(f"  {day['day']}: {day['temp']}°C")

sunny_days = [e for e in forecast if e["condition"] == "Sunny"]

print("\nSunny days:")
for day in sunny_days:
    print(f"  {day['day']}")

nice_days = [e for e in forecast if e["temp"] > 12 and e["condition"] != "Rainy"]

print("\nNice days (warm + not rainy):")
for day in nice_days:
    print(f"  {day['day']}: {day['temp']}°C, {day['condition']}")