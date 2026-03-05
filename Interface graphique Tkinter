import tkinter as tk

# création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("2048")

# création de la grille
for ligne in range(4):
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

# boucle principale
fenetre.mainloop()
