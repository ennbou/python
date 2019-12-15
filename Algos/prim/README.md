# Algorithme de Prim

## Definition

L'algorithme de Prim est un algorithme qui calcule un arbre couvrant minimal dans un graphe connexe valué et non orienté. En d'autres termes, cet algorithme trouve un sous-ensemble d'arêtes formant un arbre sur l'ensemble des sommets du graphe initial, et tel que la somme des poids de ces arêtes soit minimale. L'algorithme consiste à choisir arbitrairement un sommet et à faire croître un arbre à partir de ce sommet. Chaque augmentation se fait de la manière la plus économique possible.

## Historique

L'algorithme a été développé en 1930 par le mathématicien tchèque VOJTECH JARNIK ; VOJTECH JARNIK (né le 22 décembre 1897 à Prague où il est mort le 22 septembre 1970) est un mathématicien tchécoslovaque qui a travaillé principalement en théorie des nombres, mais également en analyse et en algorithmique des graphes.


## Concept

L'algorithme consiste à faire croître un arbre depuis un sommet. On commence avec un seul sommet puis à chaque étape, on ajoute une arête de poids minimum ayant exactement une extrémité dans l'arbre en cours de construction. En effet, si ses deux extrémités appartenaient déjà à l'arbre, l'ajout de cette arête créerait un deuxième chemin entre les deux sommets dans l'arbre en cours de construction et le résultat contiendrait un cycle.