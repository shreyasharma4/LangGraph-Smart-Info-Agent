import requests

def get_weather(city: str) -> str:
    """Fetch real-time weather from wttr.in API"""
    try:
        url = f"https://wttr.in/{city}?format=j1"
        resp = requests.get(url, timeout=5)
        if resp.status_code != 200:
            return f"Couldn't fetch weather for {city}."

        data = resp.json()
        current = data["current_condition"][0]
        temp = current["temp_C"]
        desc = current["weatherDesc"][0]["value"]
        return f"{desc}, {temp}°C in {city.capitalize()}."
    except Exception:
        return f"Sorry, I couldn’t fetch the weather for {city}."


def compare_weather(city1: str, city2: str) -> str:
    """Compare weather between two cities"""
    try:
        url1 = f"https://wttr.in/{city1}?format=j1"
        url2 = f"https://wttr.in/{city2}?format=j1"
        r1 = requests.get(url1, timeout=5).json()
        r2 = requests.get(url2, timeout=5).json()

        t1 = int(r1["current_condition"][0]["temp_C"])
        t2 = int(r2["current_condition"][0]["temp_C"])

        if t1 > t2:
            return f"{city1.capitalize()} is warmer than {city2.capitalize()} by {t1 - t2}°C ({t1}°C vs {t2}°C)."
        elif t2 > t1:
            return f"{city2.capitalize()} is warmer than {city1.capitalize()} by {t2 - t1}°C ({t2}°C vs {t1}°C)."
        else:
            return f"Both {city1.capitalize()} and {city2.capitalize()} have the same temperature: {t1}°C."
    except Exception:
        return f"Sorry, I couldn’t compare the weather for {city1} and {city2}."


def get_crypto(coin: str) -> str:
    """Fetch crypto price in USD"""
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin.lower()}&vs_currencies=usd"
        r = requests.get(url, timeout=5)
        data = r.json()
        price = data.get(coin.lower(), {}).get("usd")
        if not price:
            return f"Couldn't fetch price for {coin}."
        return f"The current price of {coin.capitalize()} is ${price}."
    except Exception:
        return f"Sorry, I couldn’t fetch the price for {coin}."


def compare_crypto(coin1: str, coin2: str) -> str:
    """Compare crypto prices"""
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin1.lower()},{coin2.lower()}&vs_currencies=usd"
        r = requests.get(url, timeout=5)
        data = r.json()

        p1 = data.get(coin1.lower(), {}).get("usd")
        p2 = data.get(coin2.lower(), {}).get("usd")

        if not p1 or not p2:
            return f"Couldn't fetch prices for {coin1} and {coin2}."

        if p1 > p2:
            return f"{coin1.capitalize()} is more expensive than {coin2.capitalize()} (${p1} vs ${p2})."
        elif p2 > p1:
            return f"{coin2.capitalize()} is more expensive than {coin1.capitalize()} (${p2} vs ${p1})."
        else:
            return f"Both {coin1.capitalize()} and {coin2.capitalize()} are priced equally at ${p1}."
    except Exception:
        return f"Sorry, I couldn’t compare {coin1} and {coin2}."
