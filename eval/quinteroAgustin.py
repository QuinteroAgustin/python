# Zone a completer avec vos reponses


def main() :
	###### exercice 00 (la fonction est definie puis appelee dans cette zone afin de confirmer son bon fonctionnement)
	print("exercice 00 #######################")
	def exempleHello (msg):
		return "bonjour {}, comment allez-vous ?".format(msg)
	salutations = exempleHello("Michel")
	print(salutations)
	print(salutations.split(sep=" "))
 
	###### exercice 01
	print("exercice 01 #######################")

	nbSaisie = 0
	nomSaisie = input("saisir un prénom : ")
	while nomSaisie != '$': #on boucle tant que nomsaisie est différent de $
		nbSaisie += 1
		nomSaisie = input("Saisir un nom d'utilisateur : ")
	print("{}prenoms saisis".format(nbSaisie))
	
	###### exercice 02
	print("exercice 02 #######################")
	t =["Mary","Patricia","Linda","Barbara","Elizabeth","Jennifer","Maria","Susan","Margaret"]
	
	# on boucle sur le nombre d'élément du tableau en fonction de sa taille
	for i in range(len(t)):
		print("{}".format(t[i]))

	###### exercice 03
	print("exercice 03 #######################")
	import itertools

	tabRepName = ['cdrom','lib64','root','srv','mnt','snap','lost+found','tmp','run','sbin','bin','home','boot','opt','etc','swapfile','lib','var','media','usr']
	tabRepSize = [4,4,4,4,8,8,16,76,2692,15416,15872,99992,108272,116300,191872,385840,616360,647768,1308416,3357908]

	reps = {} #on initialise le dico
	for i in range(len(tabRepName)):
		reps[tabRepName[i]] = tabRepSize[i] #on remplie le dico, avec taprepname en cle et size en value avec l'indice I 
	
	print("{}".format(reps))
	
	###### exercice 04
	print("exercice 04 #######################")
	for i in range(len(reps)): # on fait une boucle du nombre d'élément dans le dictionnaire
		cle = list(reps.keys()) # on créer deux tableau séparé pour qu'ils soit indépendant
		valeur = list(reps.values())
		print("dossier {} : taille = {}".format(cle[i], valeur[i])) # on les affiche

	###### exercice 05
	print("exercice 05 #######################")
	
	#on partour le dico avec la key et la value, mais dans la meme boucle en prenant l'objet du dico en cours
	for k,v in reps.items():
		if v < 100000 and v > 10000: # on vérifie si la valeur est bien présente dans la condition sinon on n'affiche riens
			print("dossier {} : taille = {}".format(k,v))


	###### exercice 06
	print("exercice 06 #######################")

	tabSize = [] # on initialise un tableau vide
	for k,v in reps.items():#on boucle dans le dico
		tabSize.append(v)
	print("affichage de 'tabSize' :\n{}".format(tabSize))

	###### exercice 07
	print("exercice 07 #######################")

	def totalSize(tableau):
		total = 0
		for i in tableau:#on parcour le tableau, avec i l'élément du tableau
			total = total+i#on aditionne l'élément avec le reste du tableau
		return total #on renvoie le tableau

	print("pour le tableau {}".format(tabSize))
	print("la somme est de {}".format(totalSize(tabSize)))
	
	###### exercice 08
	print("exercice 08 #######################")
	fileName = "liste_etudiants_admin_sys.csv"
	file = open(fileName, 'r')
	lignes = file.readlines()
	totalLigne = 0
	for ligne in lignes:
		print("{}".format(ligne))
		totalLigne += 1
	print("le fichier contient {} lignes".format(totalLigne))
			
	###### exercice 09
	print("exercice 09 #######################")
	
	def makeStudentClass(fileName, typeSeparateur = ";"):
		dico = {}
		file = open(fileName, 'r')
		lignes = file.readlines()
		totalLigne = 0
		for ligne in lignes:
			etudiant = str(ligne).split(typeSeparateur)
			dico[totalLigne+1] = etudiant
			totalLigne += 1
		print("Creation d'un dictionnaire a partir du fichier '{}' avec {} entrees".format(fileName, totalLigne))
		return dico
	
	uneClasse = makeStudentClass('liste_etudiants_admin_sys.csv', ';')
	print(uneClasse)
	###### exercice 10
	print("exercice 10 #######################")
	def makeUser(prenom, nom):
		prenom2 = prenom[:2]
		nom2 = nom[:2]
		user = str(prenom2)+str(nom2)
		return user
	nomCompte = makeUser('Mary','Smith')

	print("nom du nouvel identifiant de compte de {} {}:{}".format('Mary', 'Smith', nomCompte))

	###### exercice 11
	print("exercice 11 #######################")
	def makeUserVar(prenom, nom, n):
		if(int(n)> 4):
			print("ERREUR taille demandée trop longue !!!")
			return False
		else:
			prenom2 = prenom[:int(n)]
			nom2 = nom[:int(n)]
			user = str(prenom2)+str(nom2)
			return user
	nomCompte = makeUserVar('Mary','Smith', 3)
	print("nom du nouvel identifiant de compte de {} {} avec {} lettres:{}".format('Mary', 'Smith', 3, nomCompte))
	nomCompte = makeUserVar('Mary','Smith', 4)
	print("nom du nouvel identifiant de compte de {} {} avec {} lettres:{}".format('Mary', 'Smith', 4, nomCompte))
	nomCompte = makeUserVar('Mary','Smith', 5)
	print("nom du nouvel identifiant de compte de {} {} avec {} lettres:{}".format('Mary', 'Smith', 5, nomCompte))

	
	###### exercice 12
	print("exercice 12 #######################")
	
	def makeUserScript(uneClasse):
		for k,v in uneClasse.items():
			prenom = v[1]
			nom = v[0]
			parent = v[6]
			user = makeUserVar(prenom, nom, 3)
			print("{}, {}, {}, {}".format(prenom, nom, parent, user))
		return 0
	
	print(makeUserScript(makeStudentClass('liste_etudiants_admin_sys.csv', ';')))

if __name__=="__main__":
	print("main()")
	main()