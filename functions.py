def additionnerDroite(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])-1, -1, -1):
            if tab[i][j] == 0:
                for k in range(j-1, -1, -1):
                    if tab[i][k] != 0:
                        tab[i][j] = tab[i][k]
                        tab[i][k] = 0
                        break

        for j in range(len(tab[i]) - 1):
            if tab[i][j] != 0:
                if tab[i][j] == tab[i][j+1]:
                    tab[i][j+1] = tab[i][j] * 2
                    tab[i][j] = 0
                    break
    return tab

def additionnerGauche(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 0:
                for k in range(j, len(tab)):
                    if tab[i][k] != 0:
                        tab[i][j] = tab[i][k]
                        tab[i][k] = 0
                        break

        for j in range(len(tab[i])-1, -1, -1):
            if tab[i][j] != 0:
                if tab[i][j] == tab[i][j-1]:
                    tab[i][j-1] = tab[i][j] * 2
                    tab[i][j] = 0
                    break
    return tab

matrice = [
    [0, 2, 0, 2],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print(matrice)
matrice = additionnerGauche(matrice)
print(matrice)

# def additionnerBas(tab):
#     for colonne in range(len(tab)):
#         for ligne in range(len(tab)-1):
#             if tab[ligne][colonne] != 0:
#                 if tab[ligne][colonne] == tab[ligne+1][colonne]:
#                     tab[ligne+1][colonne] = tab[ligne][colonne] * 2
#                     tab[ligne][colonne] = 0
#     return tab
# 
# 
# def additionnerHaut(tab):
#     for colonne in range(len(tab)-1, -1, -1):
#         for ligne in range(len(tab)-1, 0, -1):
#             if tab[ligne][colonne] != 0:
#                 if tab[ligne][colonne] == tab[ligne-1][colonne]:
#                     tab[ligne-1][colonne] = tab[ligne][colonne] * 2
#                     tab[ligne][colonne] = 0
#     return tab