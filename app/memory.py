from datetime import datetime

# Shared in-memory store
memory = {
    "weather": {},
    "crypto": {}
}


def save_to_memory(category: str, key: str, data):
    """Save data into in-memory cache"""
    if category not in memory:
        memory[category] = {}

    memory[category][key.lower()] = {
        "data": data,
        "timestamp": datetime.now()
    }


def get_from_memory(category: str, key: str, max_age_seconds: int):
    """Retrieve cached data if not too old"""
    key = key.lower()
    if category not in memory or key not in memory[category]:
        return None

    cached = memory[category][key]
    age = (datetime.now() - cached["timestamp"]).seconds
    if age < max_age_seconds:
        return cached["data"]
    return None
