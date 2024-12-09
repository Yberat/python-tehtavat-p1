from car import Car
import random

autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Car(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailu_kaynnissa = True

while kilpailu_kaynnissa:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)

        auto.kulje(1)

        if auto.matka >= 10000:
            kilpailu_kaynnissa = False
            break

print(f"{'Rekisteritunnus':<10} | {'Huippunopeus':<12} | {'Nopeus':<6} | {'Kuljettu matka':<10}")
print("-" * 45)
for auto in autot:
    print(auto)
