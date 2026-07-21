from __future__ import annotations

import sys

import requests


FORMULA_E_URL = (
    "https://www.fiaformulae.com/en/calendar/2025-26/r14-tokyo"
)


def main() -> int:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "MotorsportCalendarBot/1.0 "
            "(GitHub Actions calendar updater)"
        )
    }

    response = requests.get(
        FORMULA_E_URL,
        headers=headers,
        timeout=30,
    )
    response.raise_for_status()

    print("Formula E kaynağına erişildi.")
    print(f"HTTP durum kodu: {response.status_code}")
    print(f"İndirilen içerik: {len(response.content)} bayt")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except requests.RequestException as exc:
        print(f"Kaynak okunamadı: {exc}", file=sys.stderr)
        raise SystemExit(1)
