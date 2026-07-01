from functions import *

if __name__ == '__main__':
    city = input("Nome da cidade: ")
    print(f"Temperatura da cidade: {get_weather_City(city)}ºC")
    print(f"Clima da cidade: {get_weather_main(city)}")
