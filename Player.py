import pygame


class Player:
    """
    Classe pour représenter le joueur
    """
    def __init__(self, noeud, taille):
        self.position = noeud
        self.taille = taille
        self.image = pygame.transform.scale(pygame.image.load("assets/goku.gif"), (self.taille, self.taille))
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x * self.taille
        self.rect.y = self.position.y * self.taille
        self.ombre = pygame.image.load("assets/dark.png")

    def move(self, maze, action):
        """
        Déplace le joueur dans la direction donnée
        """
        arcs = self.position.get_arcs()
        # On récupère le voisin dans la direction donnée
        destination = self.position.voisin(action, maze.graphe)
        if destination is not None:
            # On vérifie que le voisin est bien un arc possible
            for arc in arcs:
                if arc is not None:
                    # si c'est le cas, on déplace le joueur
                    if arc.destination == destination:
                        self.position = destination
                        self.rect.x = self.position.x * self.taille
                        self.rect.y = self.position.y * self.taille

    def draw(self, screen):
        """
        Dessine le joueur sur l'écran
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def draw_ombre(self, screen):
        """
        Dessine la zone d'ombre autour du joueur pour le mode difficile
        """
        screen.blit(self.ombre, (self.rect.x - self.ombre.get_width() // 2 + self.image.get_width() // 2,
                                 self.rect.y - self.ombre.get_height() // 2 + self.image.get_height() // 2))
