def is_valid_price(offer, settings):
    """
    Kontrola maximální ceny.
    """
    price = offer.get("price", 999999)
    destination_type = offer.get("destination_type", "europe")

    limits = settings.get("max_prices", {})

    max_price = limits.get(destination_type, 999999)

    return price <= max_price


def is_valid_trip_length(offer, settings):
    """
    Kontrola délky pobytu.
    """
    days = offer.get("trip_days", 0)

    trip_settings = settings.get("trip_length", {})

    min_days = trip_settings.get("min_days", 3)
    max_days = trip_settings.get("max_days", 14)

    return min_days <= days <= max_days


def is_new_offer(offer_id, history):
    """
    Kontrola, zda nabídka ještě nebyla odeslána.
    """
    return offer_id not in history.get("sent_offers", [])


def apply_filters(offers, settings, history):
    """
    Hlavní filtr.
    """
    result = []

    for offer in offers:

        offer_id = offer.get("id")

        if not offer_id:
            continue

        if not is_valid_price(offer, settings):
            continue

        if not is_valid_trip_length(offer, settings):
            continue

        if not is_new_offer(offer_id, history):
            continue

        result.append(offer)

    return result


def save_offer_to_history(offer_id, history):
    """
    Přidá nabídku do historie.
    """
    if "sent_offers" not in history:
        history["sent_offers"] = []

    if offer_id not in history["sent_offers"]:
        history["sent_offers"].append(offer_id)

    return history
