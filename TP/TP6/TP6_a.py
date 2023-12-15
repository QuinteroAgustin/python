from Domino import Domino

domino1 = Domino()
domino1.afficher_points()

domino2 = Domino(3,5)
domino2.afficher_points()
domino2 = Domino(3,5)
domino2.afficher_points()

print("total des points : {}".format(domino1.valeur()+domino2.valeur()))

liste_domino = []
for i in range(7):
    for x in range(7):
        liste_domino.append(Domino(i,x))

for i in range(len(liste_domino)):
    liste_domino[i].afficher_points()

    