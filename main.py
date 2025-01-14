import re


def etalon(fichier_txt):
    somme = 0

    # Ouverture du fichier en mode lecture
    with open(fichier_txt, 'r') as fichier:
        lignes = fichier.readlines()  # Lecture de toutes les lignes du fichier

    # parcours de chaque ligne
    for ligne in lignes:
        # recherche de tous les chiffres
        chiffres = re.findall(r'\d', ligne)

        if len(chiffres) >= 2:
            premier = chiffres[0]
            dernier = chiffres[-1]

            # Concatène le premier et le dernier chiffre pour former un nombre
            etalon = int(premier + dernier)

            somme += etalon

    return somme


fichier = "document.txt"

somme = etalon(fichier)
print(f"Somme d'etalonnage : {somme}")
