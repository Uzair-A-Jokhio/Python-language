import json
import sys
import requests

band = input("write the bands name: ")
responce = requests.get("http://itunes.apple.com/search?entity=song&limit=5&term=" + band)

o = responce.json()

for result in o["results"]:
    print(result["trackName"])
    


