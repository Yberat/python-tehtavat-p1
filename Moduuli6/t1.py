import random

def heita_noppa():
    return random.randint(1,6)

def paaohjelma():
    heitto = 0
    while heitto != 6:
        heitto = heita_noppa()
        print(f"Nopan silmäluku {heitto}")

paaohjelma()