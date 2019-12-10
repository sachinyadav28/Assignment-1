import requests
import json

URL = "https://api.nasa.gov/planetary/apod?api_key=FDAYYhgApUVapIMuhLb7cmlDrTXu0hLJRMjY7VD4"

x = requests.get(URL)

dict = json.loads(x.text)

for key , value in dict.items():
    print(f"{key} : {value}")

