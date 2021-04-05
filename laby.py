#Partie de Zhi-Sheng Trieu
import random
from pile import *

class laby:
    def __init__(self,t):
        self.t=t #t correspond à la taille du labyrinthe

    def predecesseurs(self,pos,lab):
        #cette fonction parcourt les chemins possibles depuis la position donnée et fait la liste des prédécesseurs de chaque case rencontrée
        visite = [] #cette liste permet de garder en mémoire les cases déjà visitées
        P = Pile() #on créé une pile
        P.empiler(pos)
        dico = {} #la liste des predecesseurs est stockée dans un dictionnaire

        while not P.est_vide():
            u = P.depiler() #on créé cuseur qui va contenir la case qu'on visite
            visite.append(u)
            for v in lab[u - 1]: #on fait une boucle pour parcourir chaque voisins de la case qu'on visite
                #si le voisin n'a pas été visité on associe le voisin à la case du curseur dans le dictionnaire des prédecesseurs
                if not v in visite:
                    dico[v] = u
                    P.empiler(v)
        return dico

    def solution(self, pos, lab):  # cette fonction va donner l'un des chemins vers la sortie
        dico = self.predecesseurs(pos, lab) #on récupère le dictionnaire des prédecesseurs
        rep = [] #cette liste conservera les numéros des cases du chemin vers la sortie
        m = len(lab) #m est le nombre de cellules dans le labyrinthe
        cell = m #on part de la dernière cellules qui est l'arrivé avec un curseur

        while not cell == pos:
            #tant qu'on est pas revenu à la position du joueur on parcourt le labyrinthe par les prédécesseurs
            cell = dico[cell]
            rep = [cell] + rep

        return rep+[m]

    #Partie de Yu Tian
    def voisins(self,x, decouvert):
        L = []
        if x + self.t <= self.t ** 2 and x + self.t not in decouvert:
            L.append(x + self.t)
        if x % self.t != 0 and x + 1 not in decouvert:
            L.append(x + 1)
        if x - self.t >= 1 and x - self.t not in decouvert:
            L.append(x - self.t)
        if x % self.t != 1 and x - 1 not in decouvert:
            L.append(x - 1)
        return L

    def chemin(self):
        x = random.choice([i for i in range(1, self.t ** 2 + 1)])
        decouvert = []
        aller = [i for i in range(1, self.t ** 2 + 1)]
        while len(decouvert) < self.t ** 2:
            cases_voisines = self.voisins(x, decouvert)
            if cases_voisines != []:
                x = random.choice(cases_voisines)
            else:
                x = random.choice(aller)
            for i, j in enumerate(aller):
                if j == x: del aller[i]
            decouvert.append(x)
        return decouvert

    def tableau(self, l):
        partition = []
        sous_chemins = []
        for i in range(len(l)):
            sous_chemins.append(l[i])
            if i < self.t ** 2 - 1:
                if l[i] - l[i + 1] not in [1, -1, self.t, -self.t]:
                    partition.append(sous_chemins)
                    sous_chemins = []
                elif l[i] - l[i + 1] in [-1, 1]:
                    if (l[i] % self.t == 0 and l[i + 1] % self.t == 1) or (
                            l[i] % self.t == 1 and l[i + 1] % self.t == 0):
                        partition.append(sous_chemins)
                        sous_chemins = []
        partition.append(sous_chemins)
        tab = []
        for a in partition:
            if len(a) == 1:
                tab.append([])
            else:
                tab.append([a[1]])
                for i, j in enumerate(a):
                    if i > 0:
                        tab.append([a[i - 1]])
                        if i < len(a) - 1: tab[-1].append(a[i + 1])
        return tab, partition

    def generer(self,chemins, graphe):
        for i, chemins_principal in enumerate(chemins):
            if len(chemins_principal) > 1:
                for n, chemin in enumerate(chemins[i + 1:]):
                    if len(chemin) > 1:
                        liers = []
                        for x in chemin:
                            for x_voisin in [x + 1, x - 1, x + self.t, x - self.t]:
                                if (x % self.t == 1 and x_voisin != x - 1) or (
                                        x % self.t == 0 and x_voisin != x + 1) or x % self.t >= 2:
                                    if x_voisin in chemins_principal:
                                        liers.append((x, x_voisin))
                        v = False
                        for lier in liers:
                            if lier[1] in graphe[lier[0] - 1] or lier[0] in graphe[lier[1] - 1]:
                                v = True
                        if not v and liers != []:
                            lier = random.choice(liers)
                            graphe[lier[0] - 1].append(lier[1])
                            graphe[lier[1] - 1].append(lier[0])
        #on s'assure que le depart et l'arrivé ne soit pas isolés
        if graphe[0] == []:
            lier = random.choice([1 + self.t, 2])
            graphe[0].append(lier)
            graphe[lier - 1].append(1)
        if graphe[-1] == []:
            lier = random.choice([self.t ** 2 - 1, self.t ** 2 - self.t])
            graphe[-1].append(lier)
            graphe[lier - 1].append(self.t ** 2)
        return graphe

    def creation(self):
        ch = self.chemin()
        l, partition = self.tableau(ch)

        for i in range(len(ch)):
            for a in range(len(ch) - 1 - i):
                if ch[a] > ch[a + 1]:
                    ch[a], ch[a + 1] = ch[a + 1], ch[a]
                    l[a], l[a + 1] = l[a + 1], l[a]
        return self.generer(partition, l)





