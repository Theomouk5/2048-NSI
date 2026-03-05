def additionnerDroite(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])-1):
            if tab[i][j] != 0:
                if tab[i][j]*2 == tab[i][j] + tab[i][j+1]:
                    tab[i][j+1] = tab[i][j] * 2
                    tab[i][j] = 0
    return tab


def additionnerGauche(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])-1, -1, -1):
            if tab[i][j] != 0:
                if tab[i][j]*2 == tab[i][j] + tab[i][j-1]:
                    tab[i][j-1] = tab[i][j] * 2
                    tab[i][j] = 0
    return tab

def additionnerBas(tab):
    for colonne in range(len(tab)):
        for ligne in range(len(tab)-1):
            if tab[ligne][colonne] != 0:
                if tab[ligne][colonne] == tab[ligne+1][colonne]:
                    tab[ligne+1][colonne] = tab[ligne][colonne] * 2
                    tab[ligne][colonne] = 0
    return tab

matrice = [
    [2, 0, 0, 2],
    [2, 2, 8, 2],
    [0, 0, 8, 4],
    [0, 0, 0, 8]
]

print(matrice)
matrice = additionnerBas(matrice)
print(matrice)
