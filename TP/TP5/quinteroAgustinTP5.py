print("1.1 Génération de tables de multiplication\n")

def multiplication(table):
    result = ""
    for x in range(1,11):
        somme = table*x
        result = result + ("{}*{} = {} |\n".format(x, table, somme))
    return result

fileName = input("Quel est le nom du fichier ?")
file = open(fileName, 'w')
for x in range(2, 31):
    file.write(multiplication(x))
file.close()


print("1.2 Recherche et affichage de la phrase la plus longue\n")
fileName = "lorem_ipsum.txt"
file = open(fileName, 'r')
maxligne = ""
maxlen = 0
maxPos = 0
x=0
for ligne in file.readlines():
    if(maxlen < len(ligne)):
        maxligne = ligne
        maxlen = len(ligne)
        maxPos = x
    x = x+1
print("La ligne la plus longue est la {}eme,".format(maxPos+1))
print("Elle contient {} caractères, la voici :".format(maxlen))
print("{}\n".format(maxligne))


print("1.3 Recherche et affichage de la phrase la plus longue : variante\n")
fileName = "lorem_ipsum.txt"
file = open(fileName, 'r')

def nbmots(chaine):
    espace = 1
    for x in chaine:
        if(x == " "):
            espace = espace+1
    return espace

x=1
posMax = 0
posLigne = ""
posLen = 0

posMotMax = 0
posMotLigne = ""
posMotxMax = 0
for ligne in file.readlines():
    nbChar = len(ligne)
    nbMots = nbmots(ligne)
    print("Ligne n°{}, longueur = {}, {} mots".format(x, nbChar, nbMots))
    if(nbChar > posLen):
        posLen = nbChar
        posLigne = ligne
        posMax = x
    if(nbMots > posMotMax):
        posMotMax = nbMots
        posMotLigne = ligne
        posMotxMax = x
    x=x+1

print("La ligne la plus longue est la {}eme,".format(posMax))
print("Elle contient {} caractères, la voici :".format(posLen))
print("{}".format(posLigne))

print("La ligne ayant le plus de mots est la {}eme,".format(posMotxMax))
print("Elle contient {} mots, la voici :".format(posMotMax))
print("{}".format(posMotLigne))

print("1.4 Recherche et affichage de la phrase la plus longue : variante avec filter\n")
#Ne sais pas utiliser la fonction filter 

print("1.5 Arrondi de nombres à virgule\n")

def arrondi(ligne):
    ligne = str(ligne)
    entier = ligne.split(sep='.')
    if(float('0.' + entier[1]) >= 0.5):
        entier[0] = int(entier[0]) +1
    return int(entier[0])
fileName = "listeNombres.txt"
file = open(fileName, 'r')

fileName = "result.txt"
file2 = open(fileName, 'w')

for ligne in file.readlines():
    nb = int(arrondi(ligne))
    file2.write("{}\n".format(nb))
file2.close()