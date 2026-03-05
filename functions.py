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
