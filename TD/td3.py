import numpy as np
import random as rn


def verif(grille, i, j, x):
    return not (x in grille[:, j] or x in grille[i, :])


def init(grille):
    k = 0
    while k < 15:
        i0 = rn.randint(0, 8)
        j0 = rn.randint(0, 8)
        x = rn.randint(1, 9)
        if verif(grille, i0, j0, x):
            grille[i0, j0] = x
            k += 1

grille = np.zeros((9,9))

init(grille)
print(1)
