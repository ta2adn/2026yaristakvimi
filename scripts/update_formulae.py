import requests
import re

URL = "https://www.fiaformulae.com/en/calendar/2025-26"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("Formula E sayfasi indiriliyor...\n")

r = requests.get(URL, headers=headers, timeout=30)

print("Status:", r.status_code)

print("\nJavascript dosyalari:\n")

js = sorted(set(re.findall(r'src="([^"]+\.js[^"]*)"', r.text)))

for f in js:
    print(f)
