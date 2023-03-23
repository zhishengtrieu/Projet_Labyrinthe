import pygame
from Laby import *

pygame.init()
pygame.display.set_caption("Labyrinthe")
font = pygame.font.SysFont("Times New Roman, Arial", 50)
screen = pygame.display.set_mode((800, 800))

# on a un fond noir
screen.fill((0, 0, 0))
lab = Laby(8, 5)
graphe = lab.graphe


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # on dessine un cercle vert pour chaque nœud du graphe
    for noeud in graphe.get_noeuds():
        pygame.draw.circle(screen, (0, 255, 0), (noeud.get_x() * 100 + 50, noeud.get_y() * 100 + 50), 10)
        # on dessine un arc entre chaque nœud et ses voisins
        for arc in noeud.get_arcs():
            pygame.draw.line(screen, (0, 255, 0), (noeud.get_x() * 100 + 50, noeud.get_y() * 100 + 50),
                             (arc.get_destination().get_x() * 100 + 50, arc.get_destination().get_y() * 100 + 50), 10)



    pygame.display.flip()
