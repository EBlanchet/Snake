# Snake #

## Introduction ##

### Présentation et objectifs ###

Le concept de Snake qui d'origine vient du jeu d'arcade Blockade, développé et édité par Gremlin Industries en 1976, consiste à contrôler une longue et fine ligne semblable à un serpent. Notre projet est de reproduire un clone de ce jeu. Pour cela, nous disposons d'un fichier contenant la structure générale du programme et quelques fonctions utiles.

### Démarche logique ### 

Afin d’écrire notre code, nous avons utiliser le modèle fournit par les professeurs ainsi que le code proposé par un tuteur en informatique, malgré le fait que son jeu fonctionnait différemment du notre nous avons pu avoir une idée d’un code complet et pertinent permettant un Snake fonctionnel.
Nous avons donc commencé par compléter les fonctions utiles qui nous étaient proposées dans le programme modèle : c’est-à-dire les fonctions affiche_pommes, affiche_serpent, et change_direction.
Quand cela a été fait, nous nous sommes mises à implémenter de nouvelles fonctions afin d’obtenir un programme complet, nous allons voir lesquelles dans la partie suivante.

## Le programme ## 

### Démarche programmation ###

Le programme débute par une zone d’importation incorporant la fonction sleep du module time, la fonction randint du module random et de nombreuses fonctions du module fltk, toutes ces fonctions sont nécessaires au bon fonctionnement du code. Par la suite, on peut voir s’ajouter une zone d’assignation des variables utiles aux paramètres des dimensions de la fenêtre du jeu.
Nous allons par la suite avoir une grande partie du code composé des multiples définitions des fonctions qui forment le squelette du code :

    -la fonction case_vers_pixel (qui renvoie les coordonnées du centre 
    d’une case, case qui fait partie d’un ensemble d’autres cases 
    composant la fenêtre)
    -la fonction affiche_pommes_mod_1 (qui affiche une pomme dans la
    fenêtre du jeu)
    -la fonction mange_pomme (qui ajoute 1 point et supprime une pomme 
    quand le serpent passe sur celle-ci)
    -la fonction mort (qui fait stopper le jeu lorsque le serpent touche 
    le bord de la fenêtre ou bien lorsqu’il se mord la queue)
    -la fonction affiche_serpent (qui dessine un cercle vert sur les 
    coordonnées du serpent pour former son corps)
    -la fonction change_direction (qui fait changer le serpent de 
    direction grâce aux entrées du joueur sur les flèches du clavier)
    -la fonction deplacement (qui rafraîchit les coordonnées du serpent 
    en fonction de son mouvement)
    -la fonction coordonees_hasard (qui affecte une valeur entière
    aléatoire à des variables, cette fonction est utilisée pour 
    permettre aux pommes d’apparaître aléatoirement dans la fenêtre)
    -la fonction rejouer (qui permet au joueur, par un simple clic de
    souris, de recommencer une partie lorsqu’il perd ou de quitter 
    le jeu).

Le code se termine par de nombreux appels des fonctions évoquées plus haut, le tout avec de nombreuses hypothèses et boucles formant des ensembles permettant l’affichage d’objet comme la gestion des évènements du jeu.

### Manuel d'utilisation ###

Après avoir lancé le jeu, une fenêtre s'ouvre.
Il vous suffit maintenant d'appuyer sur une touche de votre clavier pour faire fonctionner le jeu.
Le serpent débute avec une tête et une queue (soit deux cercles de couleur) au milieu de la fenêtre.
Le but du jeu est de mangé le plus de pommes pour avoir davantage de points (score final).
Pour se déplacer, il faut utiliser les touches "haut", "bas", "gauche", "droite" sur le clavier.
Le serpent ne peut pas faire demi-tour sur lui-même, c'est à dire que lorsqu'il est dans une direction, il ne peut que continuer tout droit, aller à gauche ou aller à droite.
Le jeu se termine lorsque le serpent meurt. Soit quand il touche le bord de la fenêtre, ou lorsqu'il se mange lui-même.
Quand la partie se termine, une affiche permet de demander à l'utilisateur s’il souhaite rejouer. Si oui, il suffit de faire un clic gauche. Sinon un clic droit ferme la fenêtre pour quitter le jeu.

### Informations complémentaires ###

La fonction affiche_pommes_mod_1 garde une trace en son nom de notre tentative de création de différents modes de jeu.
