from .tools import get_weather, compare_weather, get_crypto, compare_crypto

def intent_node(state):
    user_input = state["input"].lower()

    # weather comparison
    if "compare" in user_input and "weather" in user_input:
        parts = user_input.replace("compare the weather between", "").replace("compare weather between", "").split("and")
        if len(parts) == 2:
            city1, city2 = parts[0].strip(), parts[1].strip()
            return {"result": compare_weather(city1, city2)}
        return {"result": "Please mention two cities to compare."}

    # single city weather
    elif "weather" in user_input:
        city = user_input.replace("what's the weather in", "").replace("what is the weather in", "").strip(" ?")
        if not city:
            return {"result": "Please specify a city name."}
        return {"result": get_weather(city)}

    # crypto comparison
    elif "compare" in user_input and ("bitcoin" in user_input or "ethereum" in user_input):
        coins = []
        if "bitcoin" in user_input:
            coins.append("bitcoin")
        if "ethereum" in user_input:
            coins.append("ethereum")
        if len(coins) == 2:
            return {"result": compare_crypto(coins[0], coins[1])}
        return {"result": "Please specify two cryptocurrencies to compare."}

    # single crypto
    elif "price" in user_input or "crypto" in user_input:
        if "bitcoin" in user_input:
            return {"result": get_crypto("bitcoin")}
        elif "ethereum" in user_input:
            return {"result": get_crypto("ethereum")}
        else:
            return {"result": "Please specify a cryptocurrency name like Bitcoin or Ethereum."}

    else:
        return {"result": "I can currently provide weather and cryptocurrency information."}
