import sys

# fonctions
def makeLineDir(listeLigne):
	dico = {}
	
	return dico
	
def traitementFichier(f):
	lignes = f.readlines()
	print("le fichier contient {} lignes".format(len(lignes)))
	#print(lignes)
	# lire le fichier
	dicResume = {}
	for ligne in lignes:
#
#
#
#
#
#
	print ("regroupement")
	print (dicResume)

	

	

# programme principal

# Le script doit : 
# être appele depuis la ligne de commande
if __name__ == "__main__":
	# Verifier qu’au moins un argument a ete passe
	if len(sys.argv)<2:
		print("il manque des arguments")
		exit(1)
	else:
		# Prendre en argument le nom du fichier de log (sys.argv)
		nomFichier = sys.argv[1]
		##print("l'argument est {}".format(nomFichier))
		# Verifier que le fichier existe
		try:
			fichier = open(nomFichier,'r')
		except FileNotFoundError:
			print ("le fichier est introuvable")
			exit(1)
		# Fonction 1 : parcourir toutes les lignes du fichier (boucle for)
		traitementFichier(fichier)
# Fonction 2 : 
# Creer un dictionnaire avec trois cles
# Afficher ce dictionnaire
# Faire le regroupement par adresse IP (methode setdefault)