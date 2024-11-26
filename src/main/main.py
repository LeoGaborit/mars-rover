"""TODO : Le rover possède une direction composée de deux points (x, y), et uen direction orientée (N, E, S, W),
Le rover peut avancer ou reculer d'une case dans la direction orientée à l'aide d'une commande qui prend (f, b) en paramètre : fonction mouvement avant/arrière
Le rover peut tourner à gauche ou à droite de 90° à l'aide d'une commande qui prend (l, r) en paramètre : fonction mouvement latéral
Implementer le fait que le rover est sur une planète, donc n'en sort jamais (99x05 + 01x05 => 00X05) : creer fonction qui détecte si le rover est sur le bord de la planète
Implémenter la détection d'obstacles : creer fonction qui détecte si un obstacle est devant le robot, si oui, il se décale vers le haut, puis vers la position où il souhaitait avancer de base, puis signale l'obstacle


 y  ^
    |
    |
 ---+------ > x
    |
"""

from rover import *

marsRover = Rover()

mapSize : int = marsRover.mapHandler.getMapSize()

marsRover.afficher_position()
marsRover.move('f')
marsRover.afficher_position()

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

marsRover.mapHandler.display_map()

