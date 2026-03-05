import random
import tkinter as tk
from functions import *

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

def commencer_jeu(frame_menu):
    frame_menu.destroy()   
    creer_grille()         
    ajouter_nombre(matrice)
    ajouter_nombre(matrice)
    afficher_matrice(matrice)
    fenetre.bind("<Key>", touche)

        
def afficher_matrice(matrice):
    for i in range(4):
        for j in range(4):
            valeur=matrice[i][j]
            if valeur==0:
                grille[i][j]["text"]=""
            else:
                grille[i][j]["text"]=str(valeur)

def nouvelle_partie():
    for i in range(4):
        for j in range(4):
            matrice[i][j]=0
    ajouter_nombre(matrice)
    ajouter_nombre(matrice)
    afficher_matrice(matrice)

def quitter():
    fenetre.destroy()

def creer_grille():
    global grille
    grille = []
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

fenetre = tk.Tk()
fenetre.title("2048")

menu_principal=tk.Menu(fenetre)
fenetre.config(menu=menu_principal)
menu_jeu=tk.Menu(menu_principal,tearoff=0)
menu_jeu.add_command(label="Nouvelle partie", command=nouvelle_partie)
menu_jeu.add_command(label="Quitter", command=quitter)
menu_principal.add_cascade(label="Jeu", menu=menu_jeu)


menu_accueil = tk.Frame(fenetre)
menu_accueil.pack(expand=True)

titre = tk.Label(menu_accueil, text="2048", font=("Arial", 48))
titre.pack(pady=20)

btn_jouer = tk.Button(menu_accueil, text="Jouer", font=("Arial", 24),command=lambda: commencer_jeu(menu_accueil))
btn_jouer.pack(pady=10)

btn_quitter = tk.Button(menu_accueil, text="Quitter", font=("Arial", 24),command=fenetre.destroy)
btn_quitter.pack(pady=10)

fenetre.mainloop()   

