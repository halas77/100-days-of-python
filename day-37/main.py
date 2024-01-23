import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "halas7"
TOKEN = "qazwsx1234qazwWSX"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_url = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
  "id":"graph1",
  "name": "Read book",
  "unit": "min",
  "type":"float",
  "color": "shibafu"

}

headers = {
   "X-USER-TOKEN": TOKEN 
}


# response = requests.post(url=graph_url, json=graph_params, headers=headers)
# print(response.text)

pixel_url = f"{graph_url}/graph1"

today = datetime.now().strftime("%Y%m%d")

pixel_params = {
    "date": "",
    "quantity": "9.25"
}

# response = requests.post(url=pixel_url, json=pixel_params, headers=headers)
# print(response.text)

update_url = f"{pixel_url}/{today}"

new_data = {
    "quantity": "34.25"
}

# response = requests.put(url=update_url, json=new_data, headers=headers)
# print(response.text)

delete_url = f"{pixel_url}/{today}"

response = requests.delete(url=delete_url, headers=headers)
print(response.text)




