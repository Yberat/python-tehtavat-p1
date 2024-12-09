import requests

def hae_chuck_norris_vitsi():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")

        if response.status_code == 200:
            data = response.json()
            print("Chuck Norris -vitsi:")
            print(data["value"])
        else:
            print("Vitsin haku epäonnistui. Yritä myöhemmin uudelleen.")
    except Exception as e:
        print(f"Tapahtui virhe: {e}")


hae_chuck_norris_vitsi()
