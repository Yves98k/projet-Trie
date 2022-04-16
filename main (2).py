
import random
import numpy as np
import pandas
import matplotlib.pyplot as plt
import time
#création des fichiers
def remplissageFichier():
    #ne pas oublier de changer le chemin
    tri1= open(r'C:\Users\thiba\Contacts\Desktop\pythonProject\tri1.txt', 'w', encoding='utf8')
    for i in range(100000):
        tri1.write(str(i) +'\n')
    tri1.close()
    tri2 = open(r'C:\Users\thiba\Contacts\Desktop\pythonProject\tri2.txt', 'w', encoding='utf8')
    for i in random.sample(range(100000),100000):
        tri2.write(str(i)+'\n')
    tri2.close()
    tri3 = open(r'C:\Users\thiba\Contacts\Desktop\pythonProject\tri3.txt', 'w', encoding='utf8')
    for i in reversed(range(100000)):
        tri3.write(str(i)+'\n')
    tri3.close()



def manipulation():
    #choix du fichier à traiter
    choix=int(input("donnez un nombre entre compris entre 1 et 3: "))
    if choix == 1:
        trie= np.loadtxt(r'C:\Users\thiba\Contacts\Desktop\pythonProject\tri1.txt', dtype=list)
    elif choix ==2:
        trie = np.loadtxt(r'C:\Users\thiba\Contacts\Desktop\pythonProject\tri2.txt', dtype=list)
    elif choix==3:
        trie = np.loadtxt(r'C:\Users\thiba\Contacts\Desktop\pythonProject\tri3.txt', dtype=list)
    else:
        print("on avait dit un chiffre entre 1 et 3... :( ")

    #traitement du fichier
    TempsDepart1=float(time.time_ns())#donne le temps initiale
    x1= np.sort(trie,kind='quicksort',)#fait le trie en mode quicksort
    TempsFin1=float(time.time_ns())#donne le temps a la fin  du traitement
    TempsFinal1= TempsFin1-TempsDepart1#donne le temps final


    TempsDepart2=float(time.time_ns())
    x2= np.sort(trie, kind='heapsort', )
    TempsFin2 = float(time.time_ns())
    TempsFinal2 = TempsFin2 - TempsDepart2


    TempsDepart3 = float(time.time_ns())
    x3 = np.sort(trie, kind='mergesort', )
    TempsFin3 = float(time.time_ns())
    TempsFinal3 = TempsFin3 - TempsDepart3

    #creation du tableau et du graphe
    donnees={'valeurs':{'quicksort':x1,'heapsort':x2,'mergesort':x3},'temps':{'quicksort':TempsFinal1,'heapsort':TempsFinal2,'mergesort':TempsFinal3}}
    graphic=pandas.DataFrame(data=donnees)
    print(graphic)
    graphic.plot()



#fonction principale
def menu():
    remplissageFichier()
    manipulation()

menu()
