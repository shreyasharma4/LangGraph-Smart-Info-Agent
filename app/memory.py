from datetime import datetime

# Simple in-memory data store
memory = {
    "weather": {},
    "crypto": {}
}

def save_weather(city: str, temp: str, desc: str):
    """Save weather data to memory with timestamp."""
    memory["weather"][city.lower()] = {
        "temp": temp,
        "desc": desc,
        "timestamp": datetime.now().isoformat()
    }

def get_weather_from_memory(city: str):
    """Return cached weather if available."""
    return memory["weather"].get(city.lower())

def save_crypto(symbol: str, price: float):
    """Save crypto data to memory with timestamp."""
    memory["crypto"][symbol.upper()] = {
        "price": price,
        "timestamp": datetime.now().isoformat()
    }

def get_crypto_from_memory(symbol: str):
    """Return cached crypto if available."""
    return memory["crypto"].get(symbol.upper())
