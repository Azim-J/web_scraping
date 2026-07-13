# Moon.py

import requests
import json

url = "https://derekowens.com/cs/moon.aspx"
r = requests.get(url)

moon_data = json.loads(r.text)
print("Next full moon: " + moon_data["Full"])
print("Next new moon:  " + moon_data["New"])
