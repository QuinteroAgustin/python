print("1.1 Écrire un programme qui écrit 50 fois « facile ! »")
for x in range(50):
    print("Facile !")

print("\n1.2 Afficher 25 étoiles « * » sur une ligne (avec une boucle ) ")
for x in range(25):
    print('*', end='')

print("\n1.3 Afficher tous les entiers de 21 à 145 avec une boucle for")
for x in range(21,146):
    print(x)

print("\n1.4 Afficher le carré de i avec i variant de 1 à 40 et affiche « le carre de 1 = 1 », « le carre de 2 =4 »… « le carré de 40 = 1600 »")
for x in range (1, 41):
    print('Le carre de {}={}'.format(x,x**2))

print("\n1.5 Calculer la somme de tous les entiers de 21 à 145 puis l’afficher")
somme = 0
for x in range(21,146):
    somme = somme + x
print(somme)

print("\n1.6 Calculer 35! (factorielle).")
result = 1
for x in range(1,36):
    result = result*x
print(result)

print("\n1.7 Afficher un triangle rectangle composé d'étoiles « * » dont la largueur du côté est 15 * :")
for x in range(15):
    for y in range(x):
        print('*', end='')
    print()

print("\n2.1 remplissage de dictionnaire")
choix = "o"
dicoAF = {}
while choix=='o':
    motAnglais = input('Mot en anglais : ')
    dicoAF[motAnglais] = input('Traduction du mot {} : '.format(motAnglais))
    choix = input('Continuer a saisir ? (o/n) : ')
print('Il y a {} éléments dans le dictionaire'.format(len(dicoAF)))
for k,v in dicoAF.items(): 
    print(k,v)

print("\n2.2 remplissage de dictionnaire : variante")
motAnglais=""
dicoAF = {}
while motAnglais != '$':
    motAnglais = input('Mot en anglais : ')
    if motAnglais == '$':
        break
    dicoAF[motAnglais] = input('Traduction du mot {} : '.format(motAnglais))
    if dicoAF[motAnglais] == '$':
        break
print('Il y a {} éléments dans le dictionaire'.format(len(dicoAF)))
for k,v in dicoAF.items(): 
    print(k,v)

print("\n2.3 remplissage de dictionnaire : amélioration")
motAnglais=""
dicoAF = {}
while motAnglais != '$':
    motAnglais = input('Mot en anglais : ')
    if motAnglais == '$':
        break
    dicoAF[motAnglais] = input('Traduction du mot {} : '.format(motAnglais))
    if dicoAF[motAnglais] == '$':
        break
if len(dicoAF) > 1:
    print('Le dictionnaire contient {} éléments'.format(len(dicoAF)))
else:
    print('Le dictionnaire ne contient qu’une paire')
for k,v in dicoAF.items(): 
    print(k,v)

print("\n2.4 Construction d’un dictionnaire français anglais")
x=0
dicoFA={}
while x<len(dicoAF): # utiliser liste pour recuperer les cle en int d'un dico il faut créer deux tableau
    cle = list(dicoAF.keys())
    values = list(dicoAF.values())
    dicoFA[values[x]] = cle[x]
    x+=1

for k,v in dicoFA.items(): 
    print(k,v)