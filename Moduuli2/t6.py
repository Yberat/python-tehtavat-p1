import random

kolmenumeroinen_koodi = ''.join([str(random.randint(0, 9)) for _ in range(3)])

nelinumeroisen_koodi = ''.join([str(random.randint(1, 6)) for _ in range(4)])

print(f"Kolmenumeroinen koodi: {kolmenumeroinen_koodi}")
print(f"Nelinumeroinen koodi: {nelinumeroisen_koodi}")
