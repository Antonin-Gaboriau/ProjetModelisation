from Tkinter import *
import random
import time
import matplotlib.pyplot as plt

def draw(mat):
    global grille
    size = len(mat)
    width = 600/size
    for i in range(size):
        for j in range(size):
            if mat[size-j-1][i] > 0:
                color = 'red'
            elif mat[size-j-1][i] < 0:
                color = 'blue'
            else:
                color = 'white'
            cell = grille.create_rectangle(i*width, j*width, (i+1)*width, (j+1)*width, fill=color)

            

def tracer(liste, size, population):
    global graph, line_r, line_b
    top = graph.create_line(0, 500-(size*size*2), 600, 500-(size*size*2), fill='black')
    bottom = graph.create_line(0, 500, 600, 500, fill='black')
    curve = [0,500]
    for i in range(len(liste)):
        curve.append(int(600/(len(liste))*(i+1)))
        curve.append(500-int(liste[i])*2)
    if population == 'red':
        graph.delete(line_r)
        line_r = graph.create_line(curve, fill='red')
    if population == 'blue':
        graph.delete(line_b)
        line_b = graph.create_line(curve, fill='blue')

def force(mat, x, y):
    cpt = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if x+i>=0 and x+i<len(mat) and y+j>=0 and y+j<len(mat) and (i!=0 or j!=0):
                #si le voisin est dans la matrice  et pas lui même
                cpt += mat[x+i][y+j]
    return cpt

def generate_matrix(size):
    mat = []
    for line in range(size):
        row=[]
        for cell in range(size):
            i = random.randint(0,10)
            if i == 0:
                row.append(random.randint(1,11))
            elif i == 1:
                row.append(-random.randint(1,11))
            else:
                row.append(0)
        mat.append(row)
    return mat


def step(mat):
    next_mat = []
    for x in range(len(mat)):
        next_row = []
        for y in range(len(mat)):
            #print(force(mat, x, y))
            if force(mat, x, y) > 0:
                next_row.append(random.randint(1,11))
            elif force(mat, x, y) < 0:                
                next_row.append(-random.randint(1,11))
            else:
                next_row.append(0)
        next_mat.append(next_row)
    return next_mat

def compter(mat, population):
    compteur = 0
    for row in mat:
        for column in row:
            if population == 0:
                if column == 0:
                    compteur += 1
            elif column*population > 0:
                compteur += 1
    return compteur

size = 13
mat = generate_matrix(size)
fen = Tk()
fen.wm_attributes("-topmost", 1)
global grille, graph
grille = Canvas(fen, width=600, height=600, background='white')
grille.pack(side=LEFT)
graph = Canvas(fen, width=600, height=600, background='white')
graph.pack(side=RIGHT)
liste_rouge = []
liste_bleu = []
global line_r, line_b
line_r = graph.create_line(0,0,0,0)
line_b = graph.create_line(0,0,0,0)
#Label(fen,text=str(compteur), fg="black",width=31,font="parade 42 bold")
liste= []
liste2= []
liste3= []
for loop in range(100):
    draw(mat)
    liste.append(compter(mat,+1))
    liste2.append(compter(mat,-1))
    liste3.append(compter(mat,0))
    liste_rouge.append(compter(mat, +1))
    tracer(liste_rouge, size, 'red')
    liste_bleu.append(compter(mat, -1))
    tracer(liste_bleu, size, 'blue')
    fen.update()
    mat=step(mat)

plt.plot(liste)
plt.plot(liste2)
plt.plot(liste3)
plt.ylabel('nombre de rouge')
plt.xlabel('temps')
plt.show()

fen.mainloop()    

