from Tkinter import *
import random
import time
import matplotlib.pyplot as plt

def afficher(mat):
    global grille
    tailleMatrice = len(mat)
    tailleCellule = 600/tailleMatrice
    for i in range(tailleMatrice):
        for j in range(tailleMatrice):
            if mat[tailleMatrice-j-1][i] > 0:
                color = 'red'
            elif mat[tailleMatrice-j-1][i] < 0:
                color = 'blue'
            else:
                color = 'white'
            cell = grille.create_rectangle(i*tailleCellule, j*tailleCellule, (i+1)*tailleCellule, (j+1)*tailleCellule, fill=color)

def tracer(liste, tailleMatrice, population):
    global graphe, ligne_rouge, ligne_bleu
    top = graphe.create_line(0, 500-(tailleMatrice*tailleMatrice*), 600, 500-(tailleMatrice*tailleMatrice*2), fill='black')
    bottom = graphe.create_line(0, 500, 600, 500, fill='black')
    listePoint = [0,500]
    for i in range(len(liste)):
        listePoint.append(int(600/(len(liste))*(i+1)))
        listePoint.append(500-int(liste[i])*2)
    if population == 'red':
        graphe.delete(ligne_rouge)
        ligne_rouge = graphe.create_line(listePoint, fill='red')
    if population == 'blue':
        graphe.delete(ligne_bleu)
        ligne_bleu = graphe.create_line(listePoint, fill='blue')

def force(mat, x, y):
    cpt = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if x+i>=0 and x+i<len(mat) and y+j>=0 and y+j<len(mat) and (i!=0 or j!=0):
                #si le voisin est dans la matrice  et pas lui même
                cpt += mat[x+i][y+j]
    return cpt

def generer_matrice(tailleMatrice, creation_rouge, creation_bleu, force_rouge, force_bleu):
    mat = []
    for ligne in range(tailleMatrice):
        listeCellule=[]
        for cellule in range(tailleMatrice):
            i = random.randint(1,100)
            if i <= creation_rouge:
                if force_rouge == 0:
                    listeCellule.append(random.randint(1,11))
                else:
                    listeCellule.append(force_rouge)
            elif i-creation_rouge < creation_bleu:
                if force_bleu == 0:
                    listeCellule.append(-random.randint(1,11))
                else:
                    listeCellule.append(-force_bleu)
            else:
                listeCellule.append(0)
        mat.append(listeCellule)
    return mat

def etape(mat):
    prochaine_matrice = []
    for x in range(len(mat)):
        prochaine_listeCellule = []
        for y in range(len(mat)):
            if force(mat, x, y) > 0:
                prochaine_listeCellule.append(random.randint(1,11))
            elif force(mat, x, y) < 0:                
                prochaine_listeCellule.append(-random.randint(1,11))
            else:
                prochaine_listeCellule.append(0)
        prochaine_matrice.append(prochaine_listeCellule)
    return prochaine_matrice

def compter(mat, population):
    compteur = 0
    for ligne in mat:
        for cellule in ligne:
            if population == 0:
                if cellule == 0:
                    compteur += 1
            elif cellule*population > 0:
                compteur += 1
    return compteur

def graphique(tailleMatrice, creation_rouge, creation_bleu, force_rouge, force_bleu):
    global grille, graphe, ligne_rouge, ligne_bleu
    mat = generer_matrice(tailleMatrice, creation_rouge, creation_bleu, force_rouge, force_bleu)
    fen = Tk()
    fen.wm_attributes("-topmost", 1)
    grille = Canvas(fen, width=600, height=600, background='white')
    grille.pack(side=LEFT)
    graphe = Canvas(fen, width=600, height=600, background='white')
    graphe.pack(side=RIGHT)
    liste_rouge = []
    liste_bleu = []
    ligne_rouge = graphe.create_line(0,0,0,0)
    ligne_bleu = graphe.create_line(0,0,0,0)
    liste_vide= []
    for loop in range(tailleMatrice * 5):
        afficher(mat)
        liste_vide.append(compter(mat,0))
        liste_rouge.append(compter(mat, +1))
        tracer(liste_rouge, tailleMatrice, 'red')
        liste_bleu.append(compter(mat, -1))
        tracer(liste_bleu, tailleMatrice, 'blue')
        fen.update()
        time.sleep(1)
        mat=etape(mat)
    fen.destroy()
    plt.plot(liste_rouge)
    plt.plot(liste_bleu)
    plt.plot(liste_vide)
    plt.ylabel('evolution des populations')
    plt.xlabel('temps')
    plt.show()
    print("test")

def executer_sans_graphique(tailleMatrice, creation_rouge, creation_bleu, force_rouge, force_bleu):
    mat = generer_matrice(tailleMatrice, creation_rouge, creation_bleu, force_rouge, force_bleu)
    liste_rouge = []
    liste_bleu = []
    liste_vide= []
    for loop in range(tailleMatrice * 10):
        nb_rouges = compter(mat, +1)
        if nb_rouges == tailleMatrice * tailleMatrice:
            return "Rouges gagnants"
        if nb_rouges == 0:
            return "Bleus gagnants"
        liste_vide.append(compter(mat,0))
        liste_rouge.append(compter(mat, +1))
        liste_bleu.append(compter(mat, -1))
        mat=etape(mat)
    return "Egalite"

def calcul():
    tailleMatrice = int(input("Taille de la matrice : "))
    creation_rouge = int(input("Chance de création d'une cellule rouge au départ : "))
    creation_bleu = int(input("Chance de création d'une cellule bleu au départ : "))
    force_rouge = int(input("Force de chaque cellule rouges (0 pour alléatoire entre 1 et 10) : "))
    force_bleu = int(input("Force de chaque cellule bleus (0 pour alléatoire entre 1 et 10) : "))
    nombre_execution = int(input("Executer combien de fois ? "))
    for loop in range(nombre_execution):
        print(str(executer_sans_graphique(tailleMatrice, creation_rouge, creation_bleu, force_rouge, force_bleu)))
