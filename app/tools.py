import requests
from .memory import save_to_memory, get_from_memory


def get_weather(city: str) -> str:
    """Fetch real-time weather from wttr.in API with shared memory cache"""
    city_key = city.lower()

    # Check cache first
    cached = get_from_memory("weather", city_key, max_age_seconds=600)
    if cached:
        return cached + " (cached)"

    try:
        url = f"https://wttr.in/{city}?format=j1"
        resp = requests.get(url, timeout=5)
        if resp.status_code != 200:
            return f"Couldn't fetch weather for {city}."

        data = resp.json()
        current = data["current_condition"][0]
        temp = current["temp_C"]
        desc = current["weatherDesc"][0]["value"]
        result = f"{desc}, {temp}°C in {city.capitalize()}."

        # Save result to memory
        save_to_memory("weather", city_key, result)
        return result

    except Exception:
        return f"Sorry, I couldn’t fetch the weather for {city}."


def compare_weather(city1: str, city2: str) -> str:
    """Compare weather between two cities"""
    w1 = get_weather(city1)
    w2 = get_weather(city2)

    try:
        t1 = int("".join(filter(str.isdigit, w1.split("°C")[0].split()[-1])))
        t2 = int("".join(filter(str.isdigit, w2.split("°C")[0].split()[-1])))

        if t1 > t2:
            return f"{city1.capitalize()} is warmer than {city2.capitalize()} by {t1 - t2}°C ({t1}°C vs {t2}°C)."
        elif t2 > t1:
            return f"{city2.capitalize()} is warmer than {city1.capitalize()} by {t2 - t1}°C ({t2}°C vs {t1}°C)."
        else:
            return f"Both {city1.capitalize()} and {city2.capitalize()} have the same temperature ({t1}°C)."
    except Exception:
        return f"Couldn't compare weather between {city1} and {city2}."


def get_crypto(coin: str) -> str:
    """Fetch crypto price (in USD) with shared memory cache"""
    coin_key = coin.lower()

    # Check cache first
    cached = get_from_memory("crypto", coin_key, max_age_seconds=300)
    if cached:
        return f"{coin.upper()} price (cached): ${cached}"

    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_key}&vs_currencies=usd"
        resp = requests.get(url, timeout=5)
        data = resp.json()
        price = data.get(coin_key, {}).get("usd")

        if not price:
            return f"Couldn't fetch price for {coin}."

        save_to_memory("crypto", coin_key, price)
        return f"The current price of {coin.capitalize()} is ${price}."

    except Exception:
        return f"Sorry, I couldn’t fetch the price for {coin}."


def compare_crypto(coin1: str, coin2: str) -> str:
    """Compare two cryptocurrencies by price"""
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin1.lower()},{coin2.lower()}&vs_currencies=usd"
        resp = requests.get(url, timeout=5)
        data = resp.json()

        p1 = data.get(coin1.lower(), {}).get("usd")
        p2 = data.get(coin2.lower(), {}).get("usd")

        if not p1 or not p2:
            return f"Couldn't compare {coin1} and {coin2}."

        if p1 > p2:
            return f"{coin1.capitalize()} is more expensive than {coin2.capitalize()} (${p1} vs ${p2})."
        elif p2 > p1:
            return f"{coin2.capitalize()} is more expensive than {coin1.capitalize()} (${p2} vs ${p1})."
        else:
            return f"{coin1.capitalize()} and {coin2.capitalize()} have the same price (${p1})."
    except Exception:
        return f"Sorry, I couldn’t compare {coin1} and {coin2}."
