#!/usr/bin/env python3.6
import csv

fichier = 'entiers.csv'
nombre = []

#Fonction qui permet d'ouvrir le fichier
def lecture_fichier(fichier):
    with open(fichier, 'r') as fcsv:
        lecteur = csv.reader(fcsv, delimiter=';')
        for ligne in lecteur:
            nombre.append(ligne)
        print(nombre)
    return nombre

#Permet d'écrire dans un fichier et d'ajouter les élément avec 'a'
def ajoute_element():
    file = open(fichier, "a")
    print('Veuillez saisir un nombre : ')
    saisi = input()
    file.write(saisi)

#Permet d'effacer le contenu du fichier
def supprime_contenu():
    file = open(fichier, 'w')
    
#Permet d'afficher le max de la liste
def valeur_max():
    file = open(fichier, 'r')
    contenu = csv.reader(file, delimiter=",")
    for row in contenu:
        for string in row:
           nombre.append(int(string))
    m = max(nombre)
    print ('Le maximum est de : ' + str(m))

#Permet d'afficher le min de la liste
def valeur_min():
    file = open(fichier, 'r')
    contenu = csv.reader(file, delimiter=",")
    for row in contenu:
        for string in row:
           nombre.append(int(string))
    m = min(nombre)
    print ('Le minimum est de : ' + str(m))

#Permet d'afficher la somme du fichier
def somme():
    file = open(fichier, 'r')
    contenu = csv.reader(file, delimiter=",")
    for row in contenu:
        for string in row:
           nombre.append(int(string))
    m = sum(nombre)
    print ('La somme est de : ' + str(m))

#Permet de faire la moyenne de la liste
def moyenne():
    file = open(fichier, 'r')
    contenu = csv.reader(file, delimiter=",")
    for row in contenu:
        for string in row:
            nombre.append(int(string))
    moy = sum(nombre) / len(nombre)
    print ('La moyenne est de : ' + str(moy))

#Permet de trier par ordre croissant la lite
def ordre_croissant():
    file = open(fichier, 'r')
    contenu = csv.reader(file, delimiter=",")
    for row in contenu:
        for string in row:
            nombre.append(int(string))
    croissant = sorted(nombre)
    print(croissant)

#Permet de trier par ordre décroissant la lite
def ordre_decroissant():
    file = open(fichier, 'r')
    contenu = csv.reader(file, delimiter=",")
    for row in contenu:
        for string in row:
            nombre.append(int(string))
    decroissant = sorted(nombre, reverse=True)
    print(decroissant)

#menu
choice ='0'
while choice =='0':
    print('\nAide de la commande: ')
    print('-l, Affiche le contenu de la liste')
    print('-a [nb1 nb2 nb3 ...], Ajoute tout les nombres données en arguments à la liste')
    print('-c, Supprime tout les éléments de la liste')
    print('-s --min, Affiche la plus petite valeur de la liste')
    print('-s --max, Affiche la plus grande valeur de la liste')
    print('-s --moy, Affiche la moyenne des valeurs de la liste')
    print('-s --sum, Affiche la somme des valeurs de la liste')
    print('-t, Trie les éléments de la liste dans l\'ordre croissant')
    print('-t --desc, Trie les éléments de la liste dans l\'ordre décroissant')
    print('--help, Affiche l\'aide')

    choice = input ("veuiller saisir votre option ")

if choice == "-l":
    lecture_fichier(fichier)    
elif choice == "-a":
    ajoute_element()
elif choice == "-c":
    supprime_contenu()
elif choice == "-s --min":
    valeur_min()
elif choice == "-s --max":
    valeur_max()
elif choice == "-s --moy":
    moyenne()
elif choice == "-s --sum":
    somme()
elif choice == "-t":
    ordre_croissant()
elif choice == "-t --desc":
    ordre_decroissant()
else:
    print("Veuiller faire votre choix entre les différents options !")