# Définition des chiffres en lettres
chiffres_en_lettres = {
    '0': 'zéro',
    '1': 'un',
    '2': 'deux',
    '3': 'trois',
    '4': 'quatre',
    '5': 'cinq',
    '6': 'six',
    '7': 'sept',
    '8': 'huit',
    '9': 'neuf',
    '+': 'plus'
}

# Fonction pour écrire un numéro de téléphone en toutes lettres
def numero_en_toutes_lettres(numero):
    numero_lettre = ""
    for chiffre in numero:
        if chiffre in chiffres_en_lettres:
            numero_lettre += chiffres_en_lettres[chiffre] + " "
        else:
            numero_lettre += chiffre + " "
    return numero_lettre

# Demander à l'utilisateur d'entrer un numéro de téléphone
numero_telephone = input("Entrez un numéro de téléphone : ")

# Convertir le numéro en toutes lettres
numero_lettre = numero_en_toutes_lettres(numero_telephone)

# Afficher le numéro en toutes lettres
print("Le numéro de téléphone en toutes lettres est :", numero_lettre)