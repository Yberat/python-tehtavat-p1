def on_alkuluku(luku):
    if luku <= 1:
        return False
    if luku == 2:
        return True

    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            return False
    return True

try:
    luku = int(input("Syötä kokonaisluku: "))

    if on_alkuluku(luku):
        print(f"Luku {luku} on alkuluku.")
    else:
        print(f"Luku {luku} ei ole alkuluku.")
except ValueError:
    print("Syötä kelvollinen kokonaisluku.")