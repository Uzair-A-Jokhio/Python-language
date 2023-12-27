import urllib.request, urllib.error, urllib.parse
import json


link = input("Enter location: ")
print(f"Retreving: {link}")

url = urllib.request.urlopen(link)
data = url.read()

print(f"Recived {len(data)} characters ")

js = json.loads(data).decode


