import pygame


class Player:
    def __init__(self, noeud, taille):
        self.position = noeud
        self.taille = taille
        self.image = pygame.transform.scale(pygame.image.load("assets/perso.png"), (self.taille, self.taille))
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x*self.taille
        self.rect.y = self.position.y*self.taille

    def test_emplacement(self, maze, action):
        arcs = self.position.get_arcs()
        destination = self.position.voisin(action, maze.graphe)
        for arc in arcs:
            if arc.destination == destination:
                self.position = destination
                self.rect.x = self.position.x*self.taille
                self.rect.y = self.position.y*self.taille

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
