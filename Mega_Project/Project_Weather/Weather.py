import requests
import datetime

def get_weather(city):
    # Use Open-Meteo's Geocoding API to get latitude and longitude for the city
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geocoding_response = requests.get(geocoding_url)
    
    if geocoding_response.status_code == 200:
        geocoding_data = geocoding_response.json()
        if not geocoding_data.get("results"):
            print(f"Error: City '{city}' not found.")
            return None
        
        # Extract latitude and longitude
        latitude = geocoding_data["results"][0]["latitude"]
        longitude = geocoding_data["results"][0]["longitude"]
        city_name = geocoding_data["results"][0]["name"]
        country = geocoding_data["results"][0]["country"]
        
        # Use Open-Meteo's Weather API to get weather data
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        weather_response = requests.get(weather_url)
        
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            return {
                "city": city_name,
                "country": country,
                "temperature": weather_data["current_weather"]["temperature"],
                "windspeed": weather_data["current_weather"]["windspeed"],
                "weathercode": weather_data["current_weather"]["weathercode"]
            }
        else:
            print(f"Error: Unable to fetch weather data (HTTP {weather_response.status_code})")
            return None
    else:
        print(f"Error: Unable to fetch location data (HTTP {geocoding_response.status_code})")
        return None

def display_weather(data):
    if data is None:
        return
    
    # Map weather codes to human-readable descriptions
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snow fall",
        73: "Moderate snow fall",
        75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }
    
    weather_description = weather_codes.get(data["weathercode"], "Unknown")
    
    print(f"Weather in {data['city']}, {data['country']}:")
    print(f"Temperature: {data['temperature']}°C")
    print(f"Weather: {weather_description}")
    print(f"Wind Speed: {data['windspeed']} km/h")

def main():
    city = input("Enter the city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()