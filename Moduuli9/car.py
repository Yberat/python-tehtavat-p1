class Car:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        uusi_nopeus = self.nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

    def __str__(self):
        return (f"Rekisteritunnus: {self.rekisteritunnus}, "
                f"Huippunopeus: {self.huippunopeus} km/h, "
                f"Nopeus: {self.nopeus} km/h, "
                f"Kuljettu matka: {self.matka} km")

