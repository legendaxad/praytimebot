import requests


def get_prayer_times(city, country):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2&school=1"

    response = requests.get(url)
    data = response.json()

    if data["code"] != 200:
        return None

    timings = data["data"]["timings"]

    return {
        "Fajr": timings["Fajr"],
        "Dhuhr": timings["Dhuhr"],
        "Asr": timings["Asr"],
        "Maghrib": timings["Maghrib"],
        "Isha": timings["Isha"],
    }