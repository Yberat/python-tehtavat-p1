kaupungit = []

for i in range(5):
    kaupunki = input(f"Syötä kaupungin nimi #{i + 1}: ")
    kaupungit.append(kaupunki)

print("\nSyötetyt kaupungit ovat:")
for kaupunki in kaupungit:
    print(kaupunki)
