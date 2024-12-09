import requests


def hae_saatiedot():
    paikkakunta = input("Anna paikkakunnan nimi: ")

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "OMA_API_AVAIN"

    params = {
        "q": paikkakunta,
        "appid": api_key,
        "units": "metric"  # Celsius-asteet
    }

    try:
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()

            saatilanne = data["weather"][0]["description"]
            lampotila = data["main"]["temp"]

            print(f"\nPaikkakunta: {paikkakunta.capitalize()}")
            print(f"Säätila: {saatilanne}")
            print(f"Lämpötila: {lampotila} °C")
        else:
            print(f"Paikkakunnan tietoja ei löytynyt. Tarkista nimi.")
    except Exception as e:
        print(f"Tapahtui virhe: {e}")


hae_saatiedot()
