import requests
def Weather(city_name):
    url='http://api.openweathermap.org/data/2.5/weather?appid=951913fd7e6c3c0355f0b4b01a818ec7&q='
    url = url + city_name
    json_weather_data = requests.get(url).json()
    weather_main = json_weather_data['main']
    print(weather_main)
    return weather_main
