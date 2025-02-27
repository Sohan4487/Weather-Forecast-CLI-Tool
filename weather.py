import requests
import sys

def get_weather(city):
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        temp_min = main['temp_min']
        temp_max = main['temp_max']
        humidity = main['humidity']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C (Min: {temp_min}°C, Max: {temp_max}°C)")
        print(f"Weather: {weather_desc}")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found, please check the name and try again.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python weather.py <city_name>")
        sys.exit(1)
    
    city = sys.argv[1]
    get_weather(city)
