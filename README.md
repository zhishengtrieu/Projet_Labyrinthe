# Projet_Labyrinthe


Interface graphique choisie : Pygame

Algorithme de résolution : parcours en profondeur pour faire une liste des prédécesseurs de chaque cellules et faire un chemin depuis l'arrivé jusqu'au joueur

Structure du labyrinthe : le labyrinthe est sous la forme d'une liste d'adjacence


Contenu du projet :
Dossier : 
  -"assets" : contient toutes les images du jeu

Fichiers :

    -main.py : Gère l'interface pygame et fait appelle au autres fonctions

    -affichage.py : Gère l'affichage des différents assets 

    -boutton.py : S'occupe de l'affichage des différents boutons de l'interface

    -moteur.py : S'occupe de l'affichage du labyrinthe

    -perso.py : Définit l'objet Perso qui gère les déplacements du personnage

    -laby.py : Définit l'objet laby qui s'occupe de la génération et la résolution du labyrinthe

    -pile.py : Définit l'objet Pile qui contient les fonctions de base d'une pile 

    -depart_arrive.py : Gébère le point de départ et d'arrivé du labyrinthe
