from Tkinter import *
import random
import time
import matplotlib.pyplot as plt


def draw(mat):
    global canvas
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
            cell = canvas.create_rectangle(i*width, j*width, (i+1)*width, (j+1)*width, fill=color)

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
            print(force(mat, x, y))
            if force(mat, x, y) > 0:
                next_row.append(random.randint(1,11))
            elif force(mat, x, y) < 0:                
                next_row.append(-random.randint(1,11))
            else:
                next_row.append(0)
        next_mat.append(next_row)
    return next_mat

def compter(mat):
    compteur = 0
    for row in mat:
        for column in row:
            if column > 0:
                compteur += 1
    return compteur

def compter2(mat):
    compteur = 0
    for row in mat:
        for column in row:
            if column < 0:
                compteur += 1
    return compteur
def compter3(mat):
    compteur = 0
    for row in mat:
        for column in row:
            if column == 0:
                compteur += 1
    return compteur

size = 13
mat = generate_matrix(size)
fen = Tk()
fen.wm_attributes("-topmost", 1)
global canvas
canvas = Canvas(fen, width=600, height=600, background='white')
canvas.pack()
#label=Label(fen,text=str(compteur), fg="black",width=31,font="parade 42 bold")
#label.pack()
op = False
liste= []
liste2= []
liste3= []
for loop in range(30):
    #print("rouges: " + str(compter(mat)) + " | " + str(compter(mat)/(len(mat)*len(mat))*100) + "%")
    liste.append(compter(mat))
    liste2.append(compter2(mat))
    liste3.append(compter3(mat))
    draw(mat)
    if op == False :
        op = True
    fen.update()
    mat=step(mat)
fen.mainloop()
plt.plot(liste)
plt.plot(liste2)
plt.plot(liste3)
plt.ylabel('nombre de rouge')
plt.xlabel('temps')
plt.show()

    

