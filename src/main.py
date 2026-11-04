import json

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

    lines.append("✈️ FLIGHT DEALS BOT")
    lines.append("")
    lines.append("🔥 NOVĚ NALEZENÉ LETENKY")
    lines.append("")
    lines.append("═" * 60)
    lines.append("")

    for offer in offers:

        lines.append(f"🌍 Destinace: {offer.get('destination', 'N/A')}")
        lines.append(f"🛫 Odlet: {offer.get('departure_airport', 'N/A')}")
        lines.append(f"💰 Cena: {offer.get('price', 'N/A')} Kč")

        if offer.get("trip_days"):
            lines.append(f"🏖️ Pobyt: {offer['trip_days']} dní")

        if offer.get("outbound_date"):
            lines.append(
                f"📅 Termín: {offer['outbound_date']} - {offer.get('return_date', '')}"
            )

        lines.append(f"🏷️ Zdroj: {offer.get('source', 'N/A')}")

        if offer.get("url"):
            lines.append("")
            lines.append("🔗 Otevřít nabídku:")
            lines.append(offer["url"])

        lines.append("")
        lines.append("─" * 60)
        lines.append("")

    lines.append("")
    lines.append(f"📊 Celkem nalezeno nabídek: {len(offers)}")
    lines.append("")
    lines.append("Automaticky generováno Flight Deals Botem.")

    return "\n".join(lines)


def main():
    print("Načítám konfiguraci...")

    settings = load_json(SETTINGS_FILE)
    history = load_json(HISTORY_FILE)

    print("Vyhledávám letenky...")

    offers = get_flight_offers(settings)

    print(f"Nalezeno nabídek: {len(offers)}")

    filtered_offers = apply_filters(
        offers,
        settings,
        history
    )

    print(f"Po filtraci: {len(filtered_offers)}")

    if not filtered_offers:
        print("Nenalezeny žádné nové zajímavé letenky.")
        return

    limit = settings.get("results_limit", 20)
    filtered_offers = filtered_offers[:limit]

    email_body = build_email(filtered_offers)

    send_email(
        subject=f"✈️ Flight Deals Bot ({len(filtered_offers)} nabídek)",
        body=email_body,
        recipient=settings["recipient"]
    )

    for offer in filtered_offers:
        offer_id = offer.get("id")

        if offer_id:
            save_offer_to_history(
                offer_id,
                history
            )

    save_history(history)

    print("Hotovo.")


if __name__ == "__main__":
    main()
