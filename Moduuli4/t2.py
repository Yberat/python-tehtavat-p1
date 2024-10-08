muunnoskerroin = 2.54

while True:
    tuumat = float(input("Anna tuumamäärä (negatiivinen luku lopettaa): "))

    if tuumat < 0:
        print("Ohjelma lopetettu.")
        break

    sentit = tuumat * muunnoskerroin
    print(f"{tuumat} tuumaa on {sentit:.2f} senttimetriä.")
