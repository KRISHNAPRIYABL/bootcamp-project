import requests
from datetime import datetime

api_key ='5aeed2b44028756bb27474f1de1a7980'
location = input ("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city=((api_data['main']['temp'])-273.15)
weather_desc = api_data['weather'][O]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("---------------------------------------------------------")
print("Weather Stats for - {} || {}".format(location.upper,date_time))
print("---------------------------------------------------------")

print("Current temperature is:{:.2f} deg C".format(temp_city))
print("Current weather desc  :",weather_desc)
print("Current Humidity      :",hmdt, '%')
print("Current wind speed    :",wind_spd,'kmph')

