import requests
from bs4 import BeautifulSoup

URL = "https://www.fiaformulae.com/en/calendar/2025-26"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(URL, headers=headers, timeout=30)
print("Status:", r.status_code)

soup = BeautifulSoup(r.text, "html.parser")

links = set()

for a in soup.find_all("a", href=True):
    href = a["href"]

    if "/calendar/2025-26/" in href:
        links.add(href)

print("\nBulunan yarış linkleri:\n")

for link in sorted(links):
    print(link)
