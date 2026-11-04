from datetime import datetime, timedelta


DESTINATIONS = [
    "MLA",  # Malta
    "BGY",  # Milan
    "CIA",  # Rome
    "BCN",  # Barcelona
    "MAD",  # Madrid
    "AGP",  # Malaga
    "PMI",  # Mallorca
    "TFS",  # Tenerife
    "FNC",  # Madeira
    "ATH",  # Athens
    "DUB",  # Dublin
    "LCA"   # Cyprus
]


DESTINATION_NAMES = {
    "MLA": "Malta",
    "BGY": "Milano",
    "CIA": "Řím",
    "BCN": "Barcelona",
    "MAD": "Madrid",
    "AGP": "Malaga",
    "PMI": "Mallorca",
    "TFS": "Tenerife",
    "FNC": "Madeira",
    "ATH": "Athény",
    "DUB": "Dublin",
    "LCA": "Kypr"
}


def generate_ryanair_offer(origin, destination):
    outbound = datetime.now() + timedelta(days=30)
    inbound = outbound + timedelta(days=4)

    return {
        "id": f"FR_{origin}_{destination}_{outbound.date()}",
        "departure_airport": origin,
        "destination": DESTINATION_NAMES.get(destination, destination),
        "price": 1990,
        "trip_days": 4,
        "outbound_date": outbound.strftime("%Y-%m-%d"),
        "return_date": inbound.strftime("%Y-%m-%d"),
        "source": "Ryanair",
        "destination_type": "europe",
        "url": (
            f"https://www.ryanair.com/cz/cs/trip/flights/select"
            f"?originIata={origin}"
            f"&destinationIata={destination}"
        )
    }


def generate_wizz_offer(origin, destination):
    outbound = datetime.now() + timedelta(days=45)
    inbound = outbound + timedelta(days=5)

    return {
        "id": f"W6_{origin}_{destination}_{outbound.date()}",
        "departure_airport": origin,
        "destination": DESTINATION_NAMES.get(destination, destination),
        "price": 2290,
        "trip_days": 5,
        "outbound_date": outbound.strftime("%Y-%m-%d"),
        "return_date": inbound.strftime("%Y-%m-%d"),
        "source": "Wizz Air",
        "destination_type": "europe",
        "url": "https://wizzair.com"
    }


def get_flight_offers(settings):

    airports = settings.get(
        "departure_airports",
        ["PRG", "BRQ", "OSR", "PED"]
    )

    offers = []

    for airport in airports:

        for destination in DESTINATIONS[:6]:
            offers.append(
                generate_ryanair_offer(
                    airport,
                    destination
                )
            )

        for destination in DESTINATIONS[6:]:
            offers.append(
                generate_wizz_offer(
                    airport,
                    destination
                )
            )

    return offers
