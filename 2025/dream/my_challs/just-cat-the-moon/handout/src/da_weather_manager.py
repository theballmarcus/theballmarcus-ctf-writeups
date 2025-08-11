import requests
import uuid

def check_weather():
    # need to check weather first.
    user_uuid = str(uuid.uuid4())
    url = f"https://science.nasa.gov/moon/weather-on-the-moon/?username={user_uuid}"
    try:
        requests.get(url, timeout=2)
        return "Meow, good weather for a cat!"
    except requests.RequestException:
        return "Meow, bad weather for a cat!"
