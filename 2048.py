import tkinter as tk

#fenetre du jeu
fenetre = tk.Tk()
fenetre.title("2048")

#la grille
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

fenetre.mainloop()



def main():
    print("Hello World")

if __name__ == "__main__":
    main()
