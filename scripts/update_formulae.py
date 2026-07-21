import requests

URL = "https://www.fiaformulae.com/en/calendar/2025-26"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("Formula E sayfasi indiriliyor...")

r = requests.get(
    URL,
    headers=headers,
    timeout=30
)

print("Status:", r.status_code)

print("\n==============================")
print("HTML ILK 3000 KARAKTER")
print("==============================\n")

print(r.text[:3000])
