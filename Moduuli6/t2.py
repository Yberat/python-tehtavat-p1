import random

def bensiini_maara(galon):
    litra =  galon * 3,785
    return litra

def paaohjelma():
    while True:
        galon = float(input("Galon: "))
        if galon < 0:
            print("Ohjelma lopetetaan")
            break
        litra = bensiini_maara(galon)
        print(f"{galon} galonnaa vastaa {litra: .2f} litraa.")

paaohjelma()