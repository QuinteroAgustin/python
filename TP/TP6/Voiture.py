class Voiture:
    marque = ""
    couleur = ""
    pilote = ""
    vitesse = 0

    def __init__(self, marque = 'Ford', couleur = 'rouge'):
        self.marque = marque
        self.couleur = couleur
        self.pilote = 'personne'
        self.vitesse = 0
    
    def choix_conducteur(self, nom):
        self.pilote = nom

    def accelerer(self, taux, duree):
        
        if(self.pilote == 'personne'):
            print("Cette voiture n'as pas de conducteur !")
            self.vitesse = 0
        else:
            self.vitesse = taux*duree

    def affiche_tout(self):
        print("{} {} pilotée par {}, vitesse = {}m/s.".format(self.marque, self.couleur, self.pilote, self.vitesse))