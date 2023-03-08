# Partie de Zhi-Sheng Trieu
import random
from pile import *


class laby:
    def __init__(self, t):
        self.t = t  # t correspond à la taille du labyrinthe

    def predecesseurs(self, pos, lab):
        # cette fonction parcourt les chemins possibles depuis la position donnée et fait la liste des prédécesseurs
        # de chaque case rencontrée
        visite = []  # cette liste permet de garder en mémoire les cases déjà visitées
        pile = Pile()
        pile.empiler(pos)
        dico = {}  # la liste des prédécesseurs est stockée dans un dictionnaire

        while not pile.empty():
            u = pile.depiler()  # on crée un curseur qui va contenir la case qu'on visite
            visite.append(u)
            for v in lab[u - 1]:  # on fait une boucle pour parcourir chaque voisin de la case qu'on visite
                # si le voisin n'a pas été visité on associe le voisin à la case du curseur dans le dictionnaire des
                # prédécesseurs
                if v not in visite:
                    dico[v] = u
                    pile.empiler(v)
        return dico

    def solution(self, pos, lab):  # cette fonction va donner l'un des chemins vers la sortie
        dico = self.predecesseurs(pos, lab)  # on récupère le dictionnaire des prédecesseurs
        rep = []  # cette liste conservera les numéros des cases du chemin vers la sortie
        nb = len(lab)  # nb est le nombre de cellules dans le labyrinthe
        cell = nb  # on part de la dernière cellule qui est l'arrivé avec un curseur

        while not cell == pos:
            # tant qu'on n'est pas revenu à la position du joueur, on parcourt le labyrinthe par les prédécesseurs
            cell = dico[cell]
            rep = [cell] + rep

        return rep + [nb]

    # Partie de Yu Tian
    def voisins(self, x, decouvert):  # trouver les voisins de la casse x qui n'ont pas été découverts
        L = []  # pour enregistrer les casses voisines
        if x + self.t <= self.t ** 2 and x + self.t not in decouvert:  # si x n'est pas dans la dernière ligne, il a un voisin qui est en bas
            L.append(x + self.t)
        if x % self.t != 0 and x + 1 not in decouvert:  # si x n'est pas dans dernière colonne, il a un voisin qui est à gauche
            L.append(x + 1)
        if x - self.t >= 1 and x - self.t not in decouvert:  # si x n'est pas dans première ligne, il a un voisin qui est en haut
            L.append(x - self.t)
        if x % self.t != 1 and x - 1 not in decouvert:  # si x n'est pas dans la première colonne, il a un voisin à droite
            L.append(x - 1)
        return L

    def chemin(self):  # découvre les casses
        x = random.choice([i for i in range(1, self.t ** 2 + 1)])  # créer un terrain avec la taille du labyrinthe
        decouvert = []  # pour enregistrer les casse découverte
        aller = [i for i in range(1, self.t ** 2 + 1)]  # pour enregistrer les casses non découvertes
        while len(decouvert) < self.t ** 2:  # si la programme parcourt toutes les casses, il finit la boucle
            cases_voisines = self.voisins(x, decouvert)
            if cases_voisines:  # s'il y a des voisins, il continue le chemin
                x = random.choice(cases_voisines)
            else:  # sinon, ce chemin est fini
                x = random.choice(aller)
            for i, j in enumerate(aller):  # supprime les casses de la liste aller qui ont été découvertes
                if j == x: del aller[i]
            decouvert.append(x)  # enregistre les casses découvertes
        return decouvert

    def tableau(self, l):  # transforme les données
        partition = []  # les chemins ensembles
        sous_chemins = []  # les casses d'un chemin
        for i in range(len(l)):
            sous_chemins.append(l[i])
            if i < self.t ** 2 - 1:
                if l[i] - l[i + 1] not in [1, -1, self.t,
                                           -self.t]:  # si la casse suivante est voisine de cette casse, enregistre le
                    # chemin
                    partition.append(sous_chemins)
                    sous_chemins = []
                elif l[i] - l[i + 1] in [-1, 1]:  # mais il y a le cas particulier
                    if (l[i] % self.t == 0 and l[i + 1] % self.t == 1) or (l[i] % self.t == 1 and l[
                        i + 1] % self.t == 0):  # si une casse est la casse suivante, une est dans première colonne et
                        # l'autre est dans la dernière colonne, enregistre le chemin
                        partition.append(sous_chemins)
                        sous_chemins = []
        partition.append(sous_chemins)
        tab = []  # les casses qui peuvent aller pour chaque casse
        for a in partition:
            if len(a) == 1:  # c'est une casse isolée
                tab.append([])
            else:
                tab.append([a[1]])  # la casse peut aller la casse suivante
                for i, j in enumerate(a):
                    if i > 0:
                        tab.append([a[i - 1]])  # la casse peut aller la casse avant
                        if i < len(a) - 1: tab[-1].append(a[i + 1])  # le casse avant peux aller la casse suivante
        return tab, partition

    def generer(self, chemins, graphe):  # lie les deux chemins
        for i, chemins_principal in enumerate(chemins):
            if len(chemins_principal) > 1:  # si ce n'est pas chemin isolé
                for n, chemin in enumerate(chemins[i + 1:]):
                    if len(chemin) > 1:  # si ce n'est pas chemin isolé
                        liers = []
                        for x in chemin:
                            for x_voisin in [x + 1, x - 1, x + self.t, x - self.t]:  # prendre les 4 voisins
                                if (x % self.t == 1 and x_voisin != x - 1) or (
                                        x % self.t == 0 and x_voisin != x + 1) or x % self.t >= 2:  # si le voisin n'est pas voisin faux
                                    if x_voisin in chemins_principal:  # si le voisin dans autre chemin
                                        liers.append((x, x_voisin))
                        v = False  # ils ne sont pas encore liés
                        for lier in liers:
                            if lier[1] in graphe[lier[0] - 1] or lier[0] in graphe[lier[1] - 1]:
                                v = True
                        if not v and liers != []:  # lie une paire de casses
                            lier = random.choice(liers)
                            graphe[lier[0] - 1].append(lier[1])
                            graphe[lier[1] - 1].append(lier[0])
        # on s'assure que le depart et l'arrivée ne soient pas isolés
        if not graphe[0]:
            lier = random.choice([1 + self.t, 2])
            graphe[0].append(lier)
            graphe[lier - 1].append(1)
        if not graphe[-1]:
            lier = random.choice([self.t ** 2 - 1, self.t ** 2 - self.t])
            graphe[-1].append(lier)
            graphe[lier - 1].append(self.t ** 2)
        return graphe

    def creation(self):  # en origine l'ordre de la casse est ordre de découverte,
        # mais il faut rendre en ordre de numéro
        ch = self.chemin()
        l, partition = self.tableau(ch)

        for i in range(len(ch)):
            for a in range(len(ch) - 1 - i):
                if ch[a] > ch[a + 1]:
                    ch[a], ch[a + 1] = ch[a + 1], ch[a]
                    l[a], l[a + 1] = l[a + 1], l[a]

        return self.generer(partition, l)
