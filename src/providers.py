import requests
from bs4 import BeautifulSoup


def get_cestujlevne():
    offers = []

    try:
        url = "https://www.cestujlevne.com"
        html = requests.get(url, timeout=20).text

        soup = BeautifulSoup(html, "html.parser")

        for link in soup.find_all("a", href=True)[:20]:

            title = link.get_text(strip=True)

            if len(title) < 20:
                continue

            href = link["href"]

            if href.startswith("/"):
                href = url + href

            offers.append({
                "id": href,
                "departure_airport": "N/A",
                "destination": title,
                "price": 0,
                "trip_days": 0,
                "source": "Cestujlevne",
                "destination_type": "europe",
                "url": href
            })

    except Exception as e:
        print(f"Cestujlevne chyba: {e}")

    return offers


def get_honzovy_letenky():
    offers = []

    try:
        url = "https://honzovy-letenky.cz"
        html = requests.get(url, timeout=20).text

        soup = BeautifulSoup(html, "html.parser")

        for link in soup.find_all("a", href=True)[:20]:

            title = link.get_text(strip=True)

            if len(title) < 20:
                continue

            href = link["href"]

            offers.append({
                "id": href,
                "departure_airport": "N/A",
                "destination": title,
                "price": 0,
                "trip_days": 0,
                "source": "Honzovy letenky",
                "destination_type": "europe",
                "url": href
            })

    except Exception as e:
        print(f"Honzovy letenky chyba: {e}")

    return offers


def get_zaletsi():
    offers = []

    try:
        url = "https://zaletsi.cz"
        html = requests.get(url, timeout=20).text

        soup = BeautifulSoup(html, "html.parser")

        for link in soup.find_all("a", href=True)[:20]:

            title = link.get_text(strip=True)

            if len(title) < 20:
                continue

            href = link["href"]

            if href.startswith("/"):
                href = url + href

            offers.append({
                "id": href,
                "departure_airport": "N/A",
                "destination": title,
                "price": 0,
                "trip_days": 0,
                "source": "Zaletsi",
                "destination_type": "europe",
                "url": href
            })

    except Exception as e:
        print(f"Zaletsi chyba: {e}")

    return offers


def get_flight_offers(settings):

    offers = []

    offers.extend(get_cestujlevne())
    offers.extend(get_honzovy_letenky())
    offers.extend(get_zaletsi())

    unique = {}

    for offer in offers:
        unique[offer["id"]] = offer

    return list(unique.values())
