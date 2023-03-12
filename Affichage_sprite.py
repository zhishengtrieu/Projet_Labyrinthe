import pygame


class Affichage_sprite(pygame.sprite.Sprite):

    def __init__(self, taille, empl, cote):
        super().__init__()
        self.taille = int(10 / taille * 70)
        self.tourner = cote[1]
        self.nb_cote = cote[0]
        self.image = pygame.image.load('assets/' + str(self.nb_cote) + '.png')
        self.image = pygame.transform.scale(self.image, (self.taille, self.taille))
        self.image = pygame.transform.rotate(self.image, 90 * self.tourner)
        self.rect = self.image.get_rect()
        self.rect.x = self.taille * empl[1]
        self.rect.y = self.taille * empl[0]


def nb_de_cote(nb, cote):
    match nb:
        case 4:
            return 4, 0
        case 3:
            if cote['haut']:
                if cote['droite']:
                    if cote['bas']:
                        return 3, 0
                    else:
                        return 3, 1
                else:
                    return 3, 2
            else:
                return 3, -1
        case 2:
            if cote['haut']:
                if cote['droite']:
                    return 21, 2
                elif cote['bas']:
                    return 2, 0
                else:
                    return 21, -1
            elif cote['droite']:
                if cote['bas']:
                    return 21, 1
                else:
                    return 2, 1
            else:
                return 21, 0

        case 1:
            if cote['haut']:
                return 1, 0
            elif cote['droite']:
                return 1, -1
            elif cote['bas']:
                return 1, 2
            else:
                return 1, 1
        case 0:
            return 0, 0


def les_cotes(matrice, empl):
    res = 0
    cote = {'haut': False, 'bas': False, 'droite': False, 'gauche': False}
    for i in matrice:
        if i < empl:
            if i + 1 == empl:
                cote['gauche'] = True
                res += 1
            else:
                cote['haut'] = True
                res += 1
        else:
            if i - 1 == empl:
                cote['droite'] = True
                res += 1
            else:
                cote['bas'] = True
                res += 1
    return nb_de_cote(res, cote)


def add(taille, matrice, liste):
    for i in range(len(matrice)):
        cote = les_cotes(matrice[i], i + 1, )
        liste.add(Affichage_sprite(taille, (i // taille, i % taille), cote))
