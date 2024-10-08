import math

kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus:"))
pinta_ala = kanta * korkeus
piiri = (korkeus ** 2) * (kanta ** 2)
print(f"Kolmion piiri on: {piiri:.2f} " )
print(f"Kolmion pinta-ala on :  {pinta_ala:.2f}" )
