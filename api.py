import requests
import pprint

r = requests.get("https://pokeapi.co/")
print(r.text)

r.json()

