import requests
import os
from twilio.rest import Client


account_sid = 'ACa5c48c331f5d295f38fbd9807f0114be'
auth_token = 'c35fa39ee434efe6c8c8c974accb6fc3'
PARAMETERS = {
                "lat": 21.701660,
                "lon" : 69.722183,
                "appid": "6ff99f6fdd02a4fda9484d0ba938c9ac",
                "exclude": "daily,current,minutely"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=PARAMETERS)
response.raise_for_status()

weather_data = response.json()
weather_slicing = weather_data['hourly'][:12]
will_rain = False
for weather in weather_slicing:
    hour_data = weather_slicing[0]['weather'][0]["id"]
    if int(hour_data) <= 500:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring umbrella :)",
        from_='your_phone_number',
        to='user_number'
    )
    print(message.status)



