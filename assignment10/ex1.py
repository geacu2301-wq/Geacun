import requests

duong_dan = "https://api.chucknorris.io/jokes/random"

phan_hoi = requests.get(duong_dan)

du_lieu = phan_hoi.json()

print(du_lieu["value"])