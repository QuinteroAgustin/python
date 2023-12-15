from CompteBancaire import CompteBancaire
class CompteEpargne(CompteBancaire):
    taux = 0
    def __init__(self, nom, solde, taux = 0.3):
        super().__init__(nom, solde)
        self.taux = taux

    def changeTaux(self, valeur):
        self.taux = valeur
    
    def capitalisation(self, mois):
        print("Capitalisation sur {} mois au taux mensuel de {} %.".format(mois, self.taux))
        self.solde = self.solde+self.solde*self.taux*mois