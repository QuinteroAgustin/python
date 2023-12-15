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

	reps = {}
	for i in range(len(tabRepName)):
		reps[tabRepName[i]] = tabRepSize[i]
	
	print("{}".format(reps))
	
	###### exercice 04
	print("exercice 04 #######################")
	
	


	###### exercice 05
	print("exercice 05 #######################")
	


	###### exercice 06
	print("exercice 06 #######################")

	
	###### exercice 07
	print("exercice 07 #######################")

	

	
	###### exercice 08
	print("exercice 08 #######################")
			
	###### exercice 09
	print("exercice 09 #######################")
	
	
	###### exercice 10
	print("exercice 10 #######################")
	
###### exercice 11
	print("exercice 11 #######################")
	
###### exercice 12
	print("exercice 12 #######################")
		

if __name__=="__main__":
	print("main()")
	main()