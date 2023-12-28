import requests
API_KEY=""#Enter You API HERE
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
city = input("Enter you City Name: ")
request_url  = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temp = data['main']['temp']
    print(round(temp))
    
else:
    print("ERROR")