import random

level = int(
    input("Choisissez un niveau de difficulté (1: Facile, 2: Moyen, 3: Difficile ?)\n")
)

if level == 1:
    secret = random.randint(0, 10)
elif level == 2:
    secret = random.randint(0, 100)
elif level == 3:
    secret = random.randint(0, 1000)

print(secret)
user_input = int(input("Entrez un nombre : "))

attempt = 1
while user_input != secret:
    if user_input < secret:
        print(f"Le nombre est plus grand que {user_input}")
        attempt += 1
    else:
        print(f"Le nombre est plus petit que {user_input}")
        attempt += 1
    user_input = int(input("Entrez un nombre : "))

print(f"Bravo vous avez trouvé le nombre en {attempt} essais.")
