class Pile:
    """ Classe pour les piles
    Utilisation
    p = Pile() renvoie une pile vide
    """

    def __init__(self):
        self.data = []

    def empty(self):
        return self.data == []

    def sommet(self):
        assert not self.empty(), 'Pile vide'
        return self.data[-1]

    def empiler(self, x):
        self.data.append(x)
        return self

    def depiler(self):
        assert not self.empty(), 'Pile vide'
        return self.data.pop()

    def __str__(self):
        string = ""
        for elt in self.data: string = string + " " + str(elt) + " "
        return string
