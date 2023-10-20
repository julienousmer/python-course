import random

level = int(input('Choisissez un niveau de difficulté (1: Facile, 2: Moyen, 3: Difficile ?)\n'))

if level == 1:
    random_number = random.randint(0, 10)
elif level == 2:
    random_number = random.randint(0, 100)
elif level == 3:
    random_number = random.randint(0, 1000)


print(random_number)
input_number = int(input("Entrez un nombre : "))

counter = 1
while input_number != random_number:
    if input_number < random_number:
        print(f"Le nombre est plus grand que {input_number} ")
        counter = counter + 1
        input_number = int(input("Entrez un nombre : "))
    elif input_number > random_number:
        print(f"Le nombre est plus petit que {input_number} ")
        counter = counter + 1
        input_number = int(input("Entrez un nombre : "))

print(f"Bravo vous avez trouvé le nombre en {counter} essais.")