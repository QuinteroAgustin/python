import sys

# fonctions
def makeLineDir(listeLigne):
	dico = {}
	log = listeLigne.split()
	dico["remote_host"] = log[0]
	dico["status"] = log[8]
	dico["bytes_sent"] = log[9]
	return dico
	
def traitementFichier(f):
	lignes = f.readlines()
	print("le fichier contient {} lignes".format(len(lignes)))
	#print(lignes)
	# lire le fichier
	dicResume = {}
	for ligne in lignes:
		ligne = makeLineDir(ligne)
		print(ligne)
		# Vérifie si la clé existe déjà dans le dictionnaire
		if(dicResume.get(ligne['remote_host'])):
			# Ajoute la valeur à la liste existante
			dicResume[ligne['remote_host']].append(ligne['bytes_sent'])
		else:
			# Crée une nouvelle liste pour cette clé
			dicResume[ligne['remote_host']] = [ligne['bytes_sent']]

	print("regroupement")

	print(dicResume)

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