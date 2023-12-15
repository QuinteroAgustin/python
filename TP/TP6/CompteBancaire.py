class CompteBancaire:
    nom = ""
    solde = 0
    
    def __init__(self, nom = "Dupont", solde = 1000):
        self.nom = nom
        self.solde = solde
    
    def depot(self, somme):
        self.solde += int(somme)

    def retrait(self, somme):
        self.solde -= int(somme)

    def affiche(self):
        print("Le solde du compte de {} est de {} euros".format(self.nom, self.solde))