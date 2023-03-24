import pygame

class Player:
    def __init__(self, noeud, taille):
        self.position = noeud
        self.taille = taille
        self.image = pygame.transform.scale(pygame.image.load("assets/goku.gif"), (self.taille, self.taille))
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x * self.taille
        self.rect.y = self.position.y * self.taille
        self.ombre = pygame.image.load("assets/dark.png")

    def move(self, maze, action):
        arcs = self.position.get_arcs()
        destination = self.position.voisin(action, maze.graphe)
        if destination is not None:
            for arc in arcs:
                if arc is not None:
                    if arc.destination == destination:
                        self.position = destination
                        self.rect.x = self.position.x * self.taille
                        self.rect.y = self.position.y * self.taille

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def draw_ombre(self, screen):
        screen.blit(self.ombre, (self.rect.x - self.ombre.get_width() // 2 + self.image.get_width() // 2,
                                 self.rect.y - self.ombre.get_height() // 2 + self.image.get_height() // 2))
