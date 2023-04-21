import json
import sys
import requests

def songs():
    '''This function Gives names of 5 songs
      of the artists/bands from itunes web site '''
    

    band = input("write the bands name: ")
    responce = requests.get("http://itunes.apple.com/search?entity=song&limit=5&term=" + band)

    o = responce.json()

    for result in o["results"]:
        print(result["trackName"])



