import requests

# How can we authenaticate ourselevs with an api
# provider
# to gain acess to more secure and valuable data.

weather_params = {
    "lat": 30.542959,
    "lon": -97.547089,
    "appid": "33b074f8bf9edd2371e1afd2172333b8",
    "exclude": "current,minutely,daily",

}
response = requests.get(url="http://api.openweathermap.org/data/2.5/onecall", params=weather_params)
if response.status_code != 200:
    response.raise_for_status()
data = response.json()
data_per_hour =data["hourly"][:12]
print(data_per_hour)
will_Rain = False
for data in data_per_hour:
    if int(data["weather"][0]["id"]) < 700:
        will_Rain = True
print(will_Rain)
