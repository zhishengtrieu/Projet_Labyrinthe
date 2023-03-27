# Partie de Zhi-Sheng Trieu
import random
from src.perso.Zoro import Zoro
from src.graphe.Graphe import Graphe
from src.perso.Player import *
from src.algo.DFS import DFS
from src.algo.BellmanFord import BellmanFord
from src.algo.Dijkstra import Dijkstra


class Maze:
    """
    Classe qui gère le labyrinthe
    """

    def __init__(self, longueur: int, hauteur: int, taille_case: int):
        self.solution = []
        self.longueur = longueur
        self.hauteur = hauteur
        self.taille_case = taille_case
        self.graphe = Graphe(self.longueur, self.hauteur)
        self.depart = self.graphe.depart
        self.fin = self.graphe.fin
        # on crée les chemins
        self.algo = DFS(self.graphe)
        self.algo.generate()
        self.player = Player(self.depart, self.taille_case)
        pos = random.choice(self.graphe.noeuds)
        self.zoro = Zoro(pos, self.taille_case)
        self.algo = BellmanFord(self.graphe)

    def resolution(self):
        """
        On résout le labyrinthe
        """
        self.solution = self.algo.find_shortest_path(self.player)

    def draw_solution(self, screen):
        """
        On dessine la solution
        """
        self.resolution()
        for i in range(len(self.solution) - 1):
            pygame.draw.line(screen, (255, 0, 0),
                             ((self.solution[i].get_x() + 1 / 2) * self.taille_case,
                              (self.solution[i].get_y() + 1 / 2) * self.taille_case),
                             ((self.solution[i + 1].get_x() + 1 / 2) * self.taille_case,
                              (self.solution[i + 1].get_y() + 1 / 2) * self.taille_case),
                             self.taille_case // 2)
            # on dessine un cercle sur chaque nœud de la solution
            pygame.draw.circle(screen, (255, 0, 0),
                               ((self.solution[i].get_x() + 1 / 2) * self.taille_case,
                                (self.solution[i].get_y() + 1 / 2) * self.taille_case),
                               self.taille_case // 4)

    def actualiser(self, screen, taille_case, display_solution, hard_mod):
        """
        On actualise le labyrinthe
        """
        screen.fill((0, 0, 0))
        graphe = self.graphe
        for noeud in graphe.get_noeuds():
            # on dessine un cercle pour chaque nœud
            pygame.draw.circle(screen, (255, 255, 255),
                               ((noeud.get_x() + 1 / 2) * taille_case, (noeud.get_y() + 1 / 2) * taille_case),
                               taille_case * 0.9 // 2)
            # on dessine un arc entre chaque nœud et ses voisins
            for arc in noeud.get_arcs():
                pygame.draw.line(screen, (255, 255, 255),
                                 ((noeud.get_x() + 1 / 2) * taille_case, (noeud.get_y() + 1 / 2) * taille_case),
                                 ((arc.get_destination().get_x() + 1 / 2) * taille_case,
                                  (arc.get_destination().get_y() + 1 / 2) * taille_case),
                                 int(taille_case * 0.9))

        # on affiche la solution si elle est activée ou qu'on croise Zoro
        zoro_solution = self.player.position == self.zoro.position
        for voisin in self.player.position.get_arcs():
            if voisin.destination == self.zoro.position:
                zoro_solution = True

        if display_solution or zoro_solution:
            # on affiche la solution
            self.draw_solution(screen)

        # on affiche le depart et l'arrivée
        img_depart = pygame.image.load('assets/kamehouse.png')
        img_depart = pygame.transform.scale(img_depart, (taille_case // 2, taille_case // 2))
        screen.blit(img_depart, (self.depart.get_x() * taille_case + img_depart.get_width() // 2,
                                 self.depart.get_y() * taille_case + img_depart.get_height() // 2))

        img_fin = pygame.image.load('assets/arrivee.png')
        img_fin = pygame.transform.scale(img_fin, (taille_case / 2, taille_case / 2))
        screen.blit(img_fin, ((self.fin.get_x() + 1 / 4) * taille_case, (self.fin.get_y() + 1 / 4) * taille_case))

        # on affiche le joueur
        self.player.draw(screen)
        self.zoro.draw(screen)

        # on affiche l'ombre si le mode difficile est activé
        if hard_mod:
            self.player.draw_ombre(screen)
