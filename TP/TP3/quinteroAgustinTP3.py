print("1.1.1 Supprimez les trois derniers éléments un par un, dans un premier temps")
annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]
del(annee[-1])
del(annee[-1])
del(annee[-1])
print(annee)

print("\n1.1.2 Puis rajoutez les mois 'Octobre', 'Novembre', 'Décembre' à la fin")
annee.append('Octobre')
annee.append('Novembre')
annee.append('Décembre')
print(annee)

print("\n1.1.3 Supprimez les trois derniers éléments d'un coups")
annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]
annee[9] = "Octobre"
annee[10] = "Novembre"
annee[11] = "Décembre"
print(annee)

print("\n1.1.4 Pour aller plus loin : la liste ‘en compréhension’")
x = [1, 2, 3, 4, 3, 5, 3, 1, 3, 2]
resultat = [y+1 for y in x] 
print(resultat)

print("\n2.1 Accès aux éléments d’un tuple")
moisDeLannee = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre')
print(moisDeLannee[3])

print("\n2.2 Vérifier la présence d’un élément dans un tuple")
print('Mars' in moisDeLannee)

print("\n3.1 Ajoutez des éléments au dictionnaire")
age = {"pierre" : 35 , "paul" : 32 , "Jacques" : 27 , "andre" : 23}
age['david'] = 22
age['veronique'] = 21
age['sylvie'] = 30
age['damien'] = 37
print(age)

print("\n3.2 Accéder à une valeur à partir d’une clé")
print(age['sylvie'])

print("\n3.3 Accéder à une valeur à partir d’une clé")
print('jean' in age)

print("\n3.4 Gérer des valeurs multiples")
club={}
club['pierre durand'] = (1986,1.72,70)
club['victor dupont'] = (1987,1.89,57)
club['paul dupuis'] = (1989,1.60,92)
club['jean rieux'] = (1985,1.88,77)
print(club)

print("\n3.5 Afficher les données d’un sportif ")
varTuple = 'pierre durand'
dateNaissSportif = club[varTuple][0]
tailleSportif = club[varTuple][1]
poidsSportif = club[varTuple][2]

print("Le sportif nommé {} est né en {}, sa taille est de {}m et son poids est de {}Kg".format(varTuple, dateNaissSportif, tailleSportif, poidsSportif))


print("\n4.1 Club sportif : variante")
nomSportif = input("Nom du sportif : ")
if nomSportif in club :
    formatDonnees = "Le sportif nommé {} est né en {}, sa taille est de {}m et son poids est de {}Kg"
    dateNaissSportif = club[nomSportif][0]
    tailleSportif = club[nomSportif][1]
    poidsSportif = club[nomSportif][2]
    print(formatDonnees.format(nomSportif, dateNaissSportif, tailleSportif, poidsSportif))
else:
    print(nomSportif, "n'existe pas")