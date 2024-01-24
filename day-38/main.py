import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""

BASE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = ""


user_input = input("Tell me which exercise you did: ")


parameters = {
    "query": user_input
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


response = requests.post(url=BASE_URL, json=parameters, headers=headers)
data = response.json()["exercises"][0]


now = datetime.now()
formmatedNow = now.strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

SHEETY_BODY = {
    "workout": {
        "date": formmatedNow,
        "time": now_time,
        "duration": data["duration_min"],
        "exercise": data["name"].title(),
        "calories": data["nf_calories"]     
    }
}

response = requests.post(url=SHEETY_ENDPOINT, json=SHEETY_BODY)
print(response.text)





