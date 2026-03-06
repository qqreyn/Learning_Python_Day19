data = {
    "city": "Warsaw",
    "forecast": [
        {"day": "Monday",  "temp": 14.0, "condition": "Sunny"},
        {"day": "Tuesday", "temp": 11.5, "condition": "Rainy"},
        {"day": "Wednesday","temp": 13.0, "condition": "Cloudy"},
        {"day": "Thursday","temp": 16.2, "condition": "Sunny"},
        {"day": "Friday",  "temp": 9.8,  "condition": "Stormy"},
    ]
}

print("5-Day Forecast for", data["city"])
print("-" * 35)
for entry in data["forecast"]:
    print(f"{entry['day']:<12} {entry['temp']}°C  {entry['condition']}")
    
print()
for i, entry in enumerate(data["forecast"], start=1):
    print(f"Day {i}: {entry['day']} — {entry['condition']}")