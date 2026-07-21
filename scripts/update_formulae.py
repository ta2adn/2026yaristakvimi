import requests

print("Formula E Robot Basladi")

url = "https://www.fiaformulae.com/en/calendar"

r = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30,
)

print(r.status_code)

with open("formulae_calendar.html", "w", encoding="utf-8") as f:
    f.write(r.text)

print("Kaydedildi.")
