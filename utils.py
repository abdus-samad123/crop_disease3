import requests

API_KEY = "9f244592efe26bbd55cf0f9ddaeb63d6"  # 🔴 Put your OpenWeatherMap API key here


def get_weather(city):
    """
    Returns:
        temp (°C)
        humidity (%)
        rainfall (mm) -> next 24 hours forecast
    """

    try:
        # 🌐 Forecast API (better than current weather)
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        # ❌ Handle invalid city / API error
        if response.status_code != 200 or "list" not in data:
            raise Exception("Invalid city or API issue")

        # 🌡 Current data (first time slot)
        current = data["list"][0]

        temp = current["main"]["temp"]
        humidity = current["main"]["humidity"]

        # 🌧 Rainfall calculation (next 24 hours)
        rainfall = 0

        for item in data["list"][:8]:  # 8 * 3h = 24h
            if "rain" in item:
                rainfall += item["rain"].get("3h", 0)

        rainfall = round(rainfall, 2)

        return temp, humidity, rainfall

    except Exception as e:
        raise Exception(f"Weather fetch error: {str(e)}")
