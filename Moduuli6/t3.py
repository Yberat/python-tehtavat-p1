def list_int(list):
    return sum(list)

def paaohjelma():
    numerot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tulos = list_int(numerot)
    print(f"listan {numerot} summa on {tulos}")

paaohjelma()