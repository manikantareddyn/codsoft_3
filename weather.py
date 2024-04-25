# Writing code for getting weather forecast information using request function 
# STEP 1 : we need to generate an api key in openweathermap and copy it
# import required library
import requests
# Asks to enter location
location=str(input('Enter location : '))
# There is a base url to fetch the weather data from openweathermap

# store the api key in a variable
api_key='5b0baa17fb81c7f207af72e166c8982d'
url=f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'

# It takes weather info from url using request library
response=requests.get(url)

# The json() will take important and relevant information from response by filtering all results
data=response.json()
# If the website give weather information without any error the cod=200
if data['cod']==200:
    print(f"Weather in {location} : {data['weather'][0]['description']}")
# temperature prints in kelvin scale so we need to convert it into celcius
    print(f"Temperature : {round(data['main']['temp']-273.15)} °C")
    print(f"Humidity : {data['main']['humidity']}%")
    print(f"Wind speed : {data['wind']['speed']} m/sec")
else :
    print(f'error : {data["message"]}')
