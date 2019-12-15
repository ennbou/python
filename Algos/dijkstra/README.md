# DIJKSTRA ALGORITHME

## DEFINITION

En théorie des graphes, le problème de plus court chemin est le problème algorithmique qui consiste à trouver un chemin d'un sommet à un autre de façon que la somme des poids des arcs de ce chemin soit minimale.
Alors l'algorithme de Dijkstra sert à résoudre le problème du plus court chemin entre deux sommets d'un graphe connexe dont le poids lié aux arêtes est positif ou nul.

## Exemple

Pour illustrer l'intérêt de cet algorithme, on peut prendre pour exemple le réseau routier d'une région : chaque sommet est une ville et chaque arc est une route dont le poids est le kilométrage. L'algorithme de Dijkstra permet alors de trouver le plus court chemin d'une ville à une autre.
Une application des plus courantes de l'algorithme de Dijkstra est le protocole open shortest path first qui permet un routage internet très efficace des informations en cherchant le parcours le plus efficace.
Les routeurs IS-IS utilisent également l'algorithme. Les sites d'itinéraires routiers l'utilise de la même manière et permettent de nombreuses adaptations en ajustant le poids des arcs comme par exemple : trajet le plus économique, le plus rapide
