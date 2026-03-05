def _verificationDroite(tab, ligne):
    for colonne in range(len(tab[ligne])-1, -1, -1):
        if tab[ligne][colonne] == 0:
            for k in range(colonne-1, -1, -1):
                if tab[ligne][k] != 0:
                    tab[ligne][colonne] = tab[ligne][k]
                    tab[ligne][k] = 0
                    break

def _verificationGauche(tab, ligne):
    for colonne in range(len(tab[ligne])):
        if tab[ligne][colonne] == 0:
            for k in range(colonne, len(tab)):
                if tab[ligne][k] != 0:
                    tab[ligne][colonne] = tab[ligne][k]
                    tab[ligne][k] = 0
                    break

def _verificationBas(tab, colonne):
    for ligne in range(len(tab)-1, 0, -1):
        if tab[ligne][colonne] == 0:
            for k in range(ligne-1, -1, -1):
                if tab[k][colonne] != 0:
                    tab[ligne][colonne] = tab[k][colonne]
                    tab[k][colonne] = 0
                    break

def _verificationHaut(tab, colonne):
    for ligne in range(len(tab)):
        if tab[ligne][colonne] == 0:
            for k in range(ligne, len(tab)):
                if tab[k][colonne] != 0:
                    tab[ligne][colonne] = tab[k][colonne]
                    tab[k][colonne] = 0
                    break



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
