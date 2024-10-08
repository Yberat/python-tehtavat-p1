kuha = float(input("Kuinka monta cm kuha on:  "))
pyyntimitta = 37 - kuha
if kuha < 37:
    print(f"Laske kuha takaisin järveen. Se on {pyyntimitta} cm alamitassa.")
else:
    print("Kuha on riittävä, voit pitää sitä.")