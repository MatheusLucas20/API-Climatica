import requests

def get_weather_API(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    API_Key = "API_AQUI"
    complete_url = f"{base_url}q={city}&appid={API_Key}"
    
    # O timeout=5 impede que a segunda chamada trave o seu terminal
    response = requests.get(complete_url, timeout=5)
    return response.json()

def get_weather_City(city):  # Garanta que este nome bate com o seu main.py
    response = get_weather_API(city)
    temp = response['main']['temp']
    return round((temp - 273.15), 2)

def get_weather_main(city):
    response = get_weather_API(city)
    main = response['weather'][0]['main']
    return main
