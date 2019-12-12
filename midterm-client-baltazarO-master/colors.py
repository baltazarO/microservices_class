import json
import requests

url="https://reqres.in/api/unknown"

resp = requests.get(url=url)
djson = resp.json()
print(djson["data"][0]["name"])
print(djson["data"][1]["name"])
