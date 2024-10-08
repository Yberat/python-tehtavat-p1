luoti_grammoina = 13.3
naula_luoteina = 32
leiviska_nauloina = 20

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

mitat = leiviskat * leiviska_nauloina * naula_luoteina
naulojen_summa = naulat * naula_luoteina

kokonais_luodit = mitat + naulojen_summa + luodit
massa_grammoina = kokonais_luodit * luoti_grammoina

kilot = int(massa_grammoina // 1000)
grammat = massa_grammoina % 1000

print(f"Massasi nykymittojen mukaan on {kilot} kilogrammaa ja {grammat:.2f} grammaa")

