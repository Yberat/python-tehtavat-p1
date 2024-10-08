def main():
    vuodenajat = {
        "Talvi": (12, 1, 2),
        "Kevät": (3, 4, 5),
        "Kesä": (6, 7, 8),
        "Syksy": (9, 10, 11)
    }

    try:
        kuukausi = int(input("Anna kuukauden numero (1-12): "))
        if 1 <= kuukausi <= 12:
            for vuodenaika, kuukaudet in vuodenajat.items():
                if kuukausi in kuukaudet:
                    print(f"Kuukausi {kuukausi} kuuluu vuoden aikaan: {vuodenaika}")
                    break
        else:
            print("Virheellinen kuukauden numero. Anna numero väliltä 1-12.")
    except ValueError:
        print("Virheellinen syöte. Anna numero väliltä 1-12.")

if __name__ == "__main__":
    main()