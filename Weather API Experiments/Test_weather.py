import requests

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
API_KEY = '71fa3028cf6cad0df7a41a60655ed78e'

# Replace 'YOUR_CITY' and 'YOUR_COUNTRY_CODE' with your city and country code
CITY = 'Brussels'
COUNTRY_CODE = '032'

# URL to fetch weather data
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY_CODE}&appid={API_KEY}&units=metric'

try:
    response = requests.get(URL)
    data = response.json()
#    print((data))
    
    if data['cod'] == 200:
        temperature = data['main']['temp']
        print(f'The local temperature in {CITY} is {temperature}°C.')
    else:
        print(f'Error: {data["message"]}')
except Exception as e:
    print(f'An error occurred: {str(e)}')