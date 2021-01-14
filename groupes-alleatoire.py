# La bibliothèque math est importer pour utiliser les fonctions math.ceil et math.floor
import math
import json
from random import *
import logging 

logging.basicConfig(filename="loggroupe.log",level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')  
logging.info("Ouverture du script")      

nom_fichier=input("veuiller saisir le nom du fichier: ")
listefile = open(nom_fichier, "r", encoding="utf-8")  #on ouvre les fichiers en gérant l'encodage (les accent)
listefile = (listefile.readlines())
logging.info("On demande a l'uilisateur quel fichier il veux qu'on ouvre. On ouvre le fichier et on le lit.")

# nbPersonnesDansFichier est une variable temporaire pour connaitre la quantité..
# des personnes dans notre fichier (à changer par la longeur de notre fichier)
# maxPersonnesParGroupe nombre maximal des personnes par groupe

nbPersonnesDansFichier =len(listefile)
maxPersonnesParGroupe = int(input("nb de personnes max par groupe: "))
logging.info("On attribue une variable pour la le nombre de personne dans le fichier.")
logging.info("Et on lui demande le nombre de personne maximum par groupe")
logging.info("on défini le nombre des groupe et le nombre des personnes par groupe")
# avec math.ceil() on arrondi à l'entier supérieur
# avec math.floor() on arrondi à l'entier inférieur

nbDesGroupes = math.ceil(nbPersonnesDansFichier/maxPersonnesParGroupe)
nbDesPeronnesParGroupe = math.floor(nbPersonnesDansFichier/nbDesGroupes)
logging.info("on défini le nombre des groupe et le nombre des personnes par groupe")
logging.info("avec math.ceil() on arrondi à l'entier supérieur")
# avec math.floor() on arrondi à l'entier inférieur")

# On initialise une liste vide et dont la longeur finale est la quantité de groupes
# et où chaque élément est le nombre des personnes par groupe

membresParGroupe = []
nbDesPersonnesRestantes = nbPersonnesDansFichier%nbDesGroupes

# La boucle prends les personnes restantes et créé un nouveau groupe s'il faut et redistribue
# les personnes restantes dans chaque groupe

#extend permet de rajouter un element dans une liste

for i in range(nbDesGroupes):
    if nbDesPersonnesRestantes>0:
        membresParGroupe.extend([nbDesPeronnesParGroupe+1])
        nbDesPersonnesRestantes -= 1
    else:
        membresParGroupe.extend([nbDesPeronnesParGroupe])

print("Nombre de groupes: ",len(membresParGroupe))
print("Nombre de personnes par groupe: ", membresParGroupe)

nombre_groupe = len(membresParGroupe)
shuffle(listefile)
liste_des_groupes = []
while nombre_groupe > 0:
    try:
        len(listefile)!=0
    
        for element_max in membresParGroupe :
            groupe = sample(listefile,element_max)
            liste_des_groupes.append(groupe)
        
            for nom in groupe:
                listefile.remove(nom)

    except:
        break
    nombre_groupe-=1

print(liste_des_groupes)

with open("resultat_groupe.json", "w", encoding="utf-8") as write_file:
    json.dump(liste_des_groupes, write_file)    