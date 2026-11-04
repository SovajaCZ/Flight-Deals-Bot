import json
import os

from providers import get_flight_offers
from filters import apply_filters, save_offer_to_history
from mailer import send_email


SETTINGS_FILE = "config/settings.json"
HISTORY_FILE = "data/history.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def build_email(offers):
    lines = []

    lines.append("✈️ LEVNÉ LETENKY")
    lines.append("=" * 50)
    lines.append("")

    for offer in offers:
        lines.append(f"ODLET: {offer.get('departure_airport', 'N/A')}")
        lines.append(f"DESTINACE: {offer.get('destination', 'N/A')}")
        lines.append(f"CENA: {offer.get('price', 'N/A')} Kč")

        if offer.get("trip_days"):
            lines.append(f"DÉLKA POBYTU: {offer['trip_days']} dní")

        if offer.get("outbound_date"):
            lines.append(
                f"TERMÍN: {offer['outbound_date']} - {offer.get('return_date', '')}"
            )

        lines.append(f"ZDROJ: {offer.get('source', 'N/A')}")

        if offer.get("url"):
            lines.append(f"ODKAZ: {offer['url']}")

        lines.append("")
        lines.append("-
