import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.20&current_weather=true"

response = requests.get(url)

print(response.json())