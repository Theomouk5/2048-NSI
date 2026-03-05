import random
import tkinter as tk

matrice = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

def touche(event):
    if event.keysym=="Right":
        additionnerDroite(matrice) 
    elif event.keysym=="Left":
        additionnerGauche(matrice)
    elif event.keysym=="Up":
        additionnerHaut(matrice)
    elif event.keysym=="Down":
        additionnerBas(matrice)
    
    ajouter_nombre(matrice)
    afficher_matrice(matrice)

def ajouter_nombre(matrice):
        case_vide=[]
        for i in range(4):
            for j in range(4):
                if matrice[i][j]==0:
                    case_vide.append((i,j))
        if not case_vide:
            return
        ligne, colonne= random.choice(case_vide)
        matrice[ligne][colonne]=2

def afficher_matrice(matrice):
    for i in range(4):
        for j in range(4):
            valeur=matrice[i][j]
            if valeur==0:
                grille[i][j]["text"]=""
            else:
                grille[i][j]["text"]=str(valeur)

fenetre = tk.Tk()
fenetre.title("2048")


grille=[]
for ligne in range(4):
    ligne_cases = []
    for colonne in range(4):
        
        case = tk.Label(
            fenetre,
            text="",
            width=6,
            height=3,
            font=("Arial", 24),
            borderwidth=2,
            relief="solid"
        )

        case.grid(row=ligne, column=colonne, padx=5, pady=5)

        ligne_cases.append(case)
    grille.append(ligne_cases)
ajouter_nombre(matrice)  
ajouter_nombre(matrice)
afficher_matrice(matrice)
fenetre.bind("<Key>", touche)
fenetre.mainloop()   
