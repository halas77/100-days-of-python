import requests

api_key = ""

parameters = {
    "lat": 8.980603,
    "lon": 38.757759,
    "appid": api_key

}



response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)

response.raise_for_status()
data = response.json() 
print(data)



key = ""

twilio_phone_numebr = +14086864746


from twilio.rest import Client

account_sid = ''
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+',
  to='+'
)

print(message.sid)
