import requests
from datetime import datetime

USERNAME = "minhlam"
TOKEN = "324djkhfs329hsasd25ahd23"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": "324djkhfs329hsasd25ahd23",
    "username": "minhlam",
    "agreeTermsOfService" : "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name": "gym",
    "unit": "Hr",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you gym today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

pixel_update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# new_pixel_data = {
#     "quantity": "3.4",
# }
#
# requests.put(url=pixel_update, json=new_pixel_data, headers=headers)

# pixel_delete = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# response = requests.delete(url=pixel_delete, headers=headers)
print(response.text)