import time
import requests
import math
 
api_key="3169cffb730904d9515ecfad89c0e55e"
# city="Dhaka, Bangladesh"
city=input("Enter city or country name: ")

def kelvin_to_cel_fer(kelvin):
    celcious=math.floor(kelvin-273.15)
    fahrenhite=math.floor(celcious * (9/5) +32)
    return celcious,fahrenhite
 
def weather_data(api_key,city):
    while True:
        try:
            url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            response=requests.get(url).json()
            temp_kelvin=response['main']['temp']
            temp_celcius,temp_fharenhite=kelvin_to_cel_fer(temp_kelvin)
            print(f"City {city}\ntemparature: {temp_celcius}°C and {temp_fharenhite}°F\nPressure is {response['main']['pressure']}\nhumidity is {response['main']['humidity']}")
            time.sleep(1800)
        except(KeyError):
            print(KeyError)
            break

weather_data(api_key,city)

