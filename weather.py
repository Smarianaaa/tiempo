import requests

city = input("Enter a city: ")
url = f"https://es.wttr.in/{city}"

res = requests.get(url)
print(res.text)
