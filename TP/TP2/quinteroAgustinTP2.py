print ('1.1.1 Initialisation de la chaine de caractère CH et afficher sa longueur')
ch = 'Esope reste ici et se repose'
print(len(ch))

print('\n1.1.2 afficher le deuxième mot de la chaine ch en utilisant les crochets et une plage [x :y]')
print(ch[6:11])

print('\n1.1.3 afficher le dernier mot de la chaine ch en utilisant les crochets et une plage [x :y] ')
print(ch[22:28])

print('\n1.1.4 afficher le dernier mot de la chaine ch en utilisant les crochets et une plage [x :]')
print(ch[22:])

print('\n1.1.5 afficher le caractère ‘c’ de deux manières différentes')
print("première manière :", 'c')
c = "c"
print("Seconde manière : {}".format(c))

print('\n1.2.1 Initialiser les chaines suivantes')
meteo = "aujourd’hui, il fait {} , la vitesse du vent est {} ,l’humidité est {}"
tempDeg = "24°"
vitesseVent = "12Km/h"
humidite = "45%"
print(meteo.format(tempDeg, vitesseVent, humidite))

print('\n1.2.2 Variante')
temps="beau"
vitesse="faible"
humid="correcte"
print(meteo.format(temps, vitesse, humid))

print('\n1.2.2 Variante')
chaineA = "cette chaine" 
chaineB = "contient %s caractères" 
chaineC = "par contre" 
chaineD = "celle-ci" 
print(chaineA+chaineB % len(chaineA+chaineB))
print(chaineD+chaineB % len(chaineD+chaineB+chaineC) +chaineC)

print('\n1.2.4 Autre méthode de formatage de chaines')
chaineBnew = chaineB.replace('%s','{}')
chaineE = chaineA + chaineBnew
chaineF = chaineD + chaineBnew + chaineC
print(chaineE.format(len(chaineE)))
print(chaineF.format(len(chaineF)))

