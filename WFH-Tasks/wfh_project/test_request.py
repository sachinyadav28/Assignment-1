import json
import requests
import os


# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"


image_path = os.path.join(os.getcwd(), "logo.jpg")

# headers = {
#     "Content-Type": "application/json",
# }

# data = {
#     'username': 'sachinadmin',
#     'email': 'sachinadmin@api.com',
#     'password': 'sachinadmin',
#     'password2': 'sachinadmin'
# }

# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# # token = r.json()['token']
# print(r.content)

JWT_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"

headers = {
    "Content-Type": "application/json",
}

data = {
    'username': 'sachinadmin',
    'password': 'sachinadmin',
}

r = requests.post(JWT_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']

BASE_ENDPOInT = 'http://127.0.0.1:8000/api/status/'
ENDPOINT = BASE_ENDPOInT + "8/"

headers2 = {
    # "Content-Type": "application/json",
    "Authorization": "JWT " + token
}

data2 = {
    'content': 'posting some updated content by sachinadmin'
}


with open(image_path, 'rb') as image:
    file_data = {
        'image': image
    }
    # r = requests.get(ENDPOINT, headers=headers2)
    # print(r.text)
    r = requests.delete(ENDPOINT,data=data2, headers=headers2, files=file_data)
    print(r.text)
