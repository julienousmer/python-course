import random

# Fonction pour choisir le coup de l'ordinateur
def choix_ordinateur():
    coups = ["Pierre", "Feuille", "Ciseaux"]
    choix = random.choice(coups)
    return choix

# Fonction pour déterminer le vainqueur d'une manche
def determiner_vainqueur(coup_joueur, coup_ordinateur):
    if coup_joueur == coup_ordinateur:
        return "Égalité"
    elif (
        (coup_joueur == "Pierre" and coup_ordinateur == "Ciseaux") or
        (coup_joueur == "Feuille" and coup_ordinateur == "Pierre") or
        (coup_joueur == "Ciseaux" and coup_ordinateur == "Feuille")
    ):
        return "Joueur"
    else:
        return "Ordinateur"

# Fonction pour jouer une manche
def jouer_manche():
    print("Choisissez votre coup :")
    print("1. Pierre")
    print("2. Feuille")
    print("3. Ciseaux")
    choix_joueur = int(input("Entrez le numéro de votre choix (1/2/3) : "))

    if choix_joueur not in (1, 2, 3):
        print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
        return jouer_manche()

    coups = ["Pierre", "Feuille", "Ciseaux"]
    coup_joueur = coups[choix_joueur - 1]
    coup_ordinateur = choix_ordinateur()

    print(f"Joueur choisit : {coup_joueur}")
    print(f"Ordinateur choisit : {coup_ordinateur}")

    vainqueur = determiner_vainqueur(coup_joueur, coup_ordinateur)

    if vainqueur == "Égalité":
        print("Manche nulle.")
    else:
        print(f"{vainqueur} remporte la manche !")
    
    return vainqueur

# Fonction principale
def jouer_shifumi():
    score_joueur = 0
    score_ordinateur = 0

    print("Bienvenue à Pierre / Feuille / Ciseaux (Shifumi)")

    while score_joueur < 2 and score_ordinateur < 2:
        print("\nManche en cours...")
        vainqueur = jouer_manche()

        if vainqueur == "Joueur":
            score_joueur += 1
        elif vainqueur == "Ordinateur":
            score_ordinateur += 1

        print(f"=======================================================================")
        print(f"Score actuel - Joueur : {score_joueur}, Ordinateur : {score_ordinateur}")
        print(f"=======================================================================")

    if score_joueur > score_ordinateur:
        print("Le joueur gagne la partie !")
    else:
        print("L'ordinateur gagne la partie !")

# Lancer le jeu
jouer_shifumi()