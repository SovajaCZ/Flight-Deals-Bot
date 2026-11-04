from datetime import datetime


def get_flight_offers(settings):
    """
    Testovací data.
    Později nahradíme skutečným načítáním z Azairu.
    """

    return [
        {
            "id": "PRG_Rome_1290_2027-04-12",

            "departure_airport": "PRG",

            "destination": "Rome",

            "price": 1290,

            "trip_days": 4,

            "outbound_date": "2027-04-12",
            "return_date": "2027-04-16",

            "source": "Azair",

            "destination_type": "europe",

            "url": "https://www.azair.com/"
        },

        {
            "id": "VIE_Bangkok_8990_2027-05-03",

            "departure_airport": "VIE",

            "destination": "Bangkok",

            "price": 8990,

            "trip_days": 14,

            "outbound_date": "2027-05-03",
            "return_date": "2027-05-17",

            "source": "Azair",

            "destination_type": "long_haul",

            "url": "https://www.azair.com/"
        }
    ]
