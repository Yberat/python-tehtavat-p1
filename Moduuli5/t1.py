import random

n = int(input("Anna arpakuutioiden lukumäärä: "))

# Alustetaan summa
summa = 0

for i in range(n):
    heitto = random.randint(1, 6)
    print(f"Arpakuutio {i+1}: {heitto}")
    summa += heitto

print(f"Kaikkien arpakuutioiden silmälukujen summa on: {summa}")
