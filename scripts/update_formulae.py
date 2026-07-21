import requests

URL = "https://calendar.google.com/calendar/ical/g791th1scjtapctba1j0fl6qhg%40group.calendar.google.com/public/basic.ics"
OUTPUT = "data/2026/formula-e.ics"

r = requests.get(URL, timeout=30)
r.raise_for_status()

with open(OUTPUT, "wb") as f:
    f.write(r.content)

print("Formula E ICS güncellendi.")
