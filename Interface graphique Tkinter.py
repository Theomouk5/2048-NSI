import random
import tkinter as tk
from tkinter import messagebox

# Fonction qui sert à pousser tout nombre != 0 à droite
def _verificationDroite(tab, ligne):
    for colonne in range(len(tab[ligne])-1, -1, -1):
        if tab[ligne][colonne] == 0:
            for k in range(colonne-1, -1, -1):
                if tab[ligne][k] != 0:
                    tab[ligne][colonne] = tab[ligne][k]
                    tab[ligne][k] = 0
                    break

# Fonction qui sert à pousser tout nombre != 0 à gauche 
def _verificationGauche(tab, ligne):
    for colonne in range(len(tab[ligne])):
        if tab[ligne][colonne] == 0:
            for k in range(colonne, len(tab)):
                if tab[ligne][k] != 0:
                    tab[ligne][colonne] = tab[ligne][k]
                    tab[ligne][k] = 0
                    break

# Fonction qui sert à pousser tout nombre != 0 en bas
def _verificationBas(tab, colonne):
    for ligne in range(len(tab)-1, 0, -1):
        if tab[ligne][colonne] == 0:
            for k in range(ligne-1, -1, -1):
                if tab[k][colonne] != 0:
                    tab[ligne][colonne] = tab[k][colonne]
                    tab[k][colonne] = 0
                    break
                

# Fonction qui sert à pousser tout nombre != 0 en haut
def _verificationHaut(tab, colonne):
    for ligne in range(len(tab)):
        if tab[ligne][colonne] == 0:
            for k in range(ligne, len(tab)):
                if tab[k][colonne] != 0:
                    tab[ligne][colonne] = tab[k][colonne]
                    tab[k][colonne] = 0
                    break


# Pousser tout nombre à droite et les additionnés de gauche à droite
def additionnerDroite(tab):
    for ligne in range(len(tab)):
        _verificationDroite(tab, ligne) 
        for colonne in range(len(tab[ligne]) - 1):
            if tab[ligne][colonne] != 0:
                if tab[ligne][colonne] == tab[ligne][colonne+1]:
                    tab[ligne][colonne+1] = tab[ligne][colonne] * 2
                    tab[ligne][colonne] = 0
                    _verificationDroite(tab, ligne)
                    break
    return tab

# Pousser tout nombre à gauche et les additionnés de droite à gauche
def additionnerGauche(tab):
    for ligne in range(len(tab)):
        _verificationGauche(tab, ligne)
        for colonne in range(len(tab[ligne])-1, -1, -1):
            if tab[ligne][colonne] != 0:
                if tab[ligne][colonne] == tab[ligne][colonne-1]:
                    tab[ligne][colonne-1] = tab[ligne][colonne] * 2
                    tab[ligne][colonne] = 0
                    _verificationGauche(tab, ligne)
                    break
    return tab

# Pousser tout nombre en bas et les additionnés de haut en bas
def additionnerBas(tab):
    for colonne in range(len(tab)):
        _verificationBas(tab, colonne)
        for ligne in range(len(tab)-1):
            if tab[ligne][colonne] != 0:
                if tab[ligne][colonne] == tab[ligne+1][colonne]:
                    tab[ligne+1][colonne] = tab[ligne][colonne] * 2
                    tab[ligne][colonne] = 0
                    _verificationBas(tab, colonne)
                    break
    return tab

# Pousser tout nombre en haut et les additionnés de bas en haut
def additionnerHaut(tab):
    for colonne in range(len(tab)):
        _verificationHaut(tab, colonne)
        for ligne in range(len(tab)-1, 0, -1):
            if tab[ligne][colonne] != 0:
                if tab[ligne][colonne] == tab[ligne-1][colonne]:
                    tab[ligne-1][colonne] = tab[ligne][colonne] * 2
                    tab[ligne][colonne] = 0
                    _verificationHaut(tab, colonne)
                    break
    return tab

# Vérifie si une case = 2048
def verificationScore(tab):
    resultat = False
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 2048:
                resultat = True
                return resultat

matrice = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
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
    
    ajouter_nombre(matrice, len(matrice))
    afficher_matrice(matrice, len(matrice))
    
    
    if jeu_terminer(matrice, len(matrice)):
        return

def ajouter_nombre(matrice, taille):
        case_vide=[]
        for i in range(taille):
            for j in range(taille):
                if matrice[i][j]==0:
                    case_vide.append((i,j))
        if not case_vide:
            return
        ligne, colonne= random.choice(case_vide)
        matrice[ligne][colonne]=2


def commencer_jeu(frame_menu):
    global frame_grille
    frame_menu.destroy()   
    frame_grille=tk.Frame(fenetre)
    barre_bouton.pack(pady=10)

    btn_nouvelle=tk.Button(
        barre_bouton,
        text="Nouvelle partie",
        font=("Arial",14),
        command=nouvelle_partie,
        bg="#8f7a66",
        fg="white",
        padx=10,
        pady=5
        )
    btn_nouvelle.pack(side="left", padx=10)
    btn_quitter=tk.Button(
        barre_bouton,
        text="Quitter",
        font=("Arial",14),
        command=quitter,
        bg="#8f7a66",
        fg="white",
        padx=10,
        pady=5
        )
    btn_quitter.pack(side="left", padx=10)
    frame_grille.pack()
    creer_grille(frame_grille, len(matrice))         
    ajouter_nombre(matrice, len(matrice))
    ajouter_nombre(matrice, len(matrice))
    afficher_matrice(matrice, len(matrice))
    fenetre.bind("<Key>", touche)
    

def jeu_terminer(tab, taille):
    for i in range(taille):
        for j in range(taille):
            if tab[i][j]==0:
                return False
    for i in range(taille):
        for j in range(taille):
            if j < (taille-1) and tab[i][j]==tab[i][j+1]:
                return False
            if i < (taille-1) and tab[i][j]==tab[i+1][j]:
                return False
    messagebox.showinfo("ta perdue")
    return True
        
def afficher_matrice(matrice, taille):
    for i in range(taille):
        for j in range(taille):
            valeur=matrice[i][j]
            if valeur==0:
                grille[i][j]["text"]=""
                grille[i][j]["bg"]="#cdc1b4",
            else:
                grille[i][j]["text"]=str(valeur)
                accumulateur = 2
                for k in range(0, 12):
                    if valeur == 2**k:
                        grille[i][j]["bg"]=couleur_liste[k]
            
def nouvelle_partie():
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            matrice[i][j]=0
    ajouter_nombre(matrice, len(matrice))
    ajouter_nombre(matrice, len(matrice))
    afficher_matrice(matrice, len(matrice))

def quitter():
    fenetre.destroy()


couleur_liste = [
    "#CDC1B4",
    "#EEE4DA",
    "#EDE0C8",
    "#F2B179",
    "#F59563",
    "#F67C5F",
    "#F65E3B",
    "#EDCF72",
    "#EDCC61",
    "#EDC850",
    "#CCF527",
    "#68F527"
]


def creer_grille(parent_frame, taille):
    global grille
    grille = []
    for ligne in range(taille):
        ligne_cases = []
        for colonne in range(taille):
            case = tk.Label(
                parent_frame,
                text="",
                width=6,
                height=3,
                font=("Arial", 24),
                borderwidth=4,
                relief="solid",
                bg="#cdc1b4",
                fg="#3c3a32"

            )
            case.grid(row=ligne, column=colonne, padx=5, pady=5)
            ligne_cases.append(case)
        grille.append(ligne_cases)

fenetre = tk.Tk()
fenetre.title("2048")
barre_bouton=tk.Frame(fenetre)


menu_accueil = tk.Frame(fenetre)
menu_accueil.pack(expand=True)

titre = tk.Label(menu_accueil, text="2048", font=("Arial", 48))
titre.pack(pady=20)

btn_jouer = tk.Button(menu_accueil, text="Jouer", font=("Arial", 24),command=lambda: commencer_jeu(menu_accueil))
btn_jouer.pack(pady=10)

btn_quitter = tk.Button(menu_accueil, text="Quitter", font=("Arial", 24),command=fenetre.destroy)
btn_quitter.pack(pady=10)

fenetre.mainloop()   
