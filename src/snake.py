from time import sleep
from random import randint
from fltk import cercle,\
                 rectangle,\
                 efface,\
                 cree_fenetre,\
                 texte,\
                 attend_ev,\
                 efface_tout,\
                 mise_a_jour,\
                 donne_ev,\
                 type_ev,\
                 touche,\
                 ferme_fenetre\

# dimensions du jeu
TAILLE_CASE = 15
LARGEUR_PLATEAU = 40  # en nombre de cases
HAUTEUR_PLATEAU = 30  # en nombre de cases


def case_vers_pixel(case):
    '''
    Fonction recevant les coordonnées d'une case du plateau sous la
    forme d'un couple d'entiers (ligne, colonne) et renvoyant les
    coordonnées du pixel se trouvant au centre de cette case. Ce calcul
    prend en compte la taille de chaque case, donnée par la variable
    globale TAILLE_CASE.

    :param float case: les coordonnees d'un case sur le plateau
    '''
    i, j = case
    return (i + .5) * TAILLE_CASE, (j + .5) * TAILLE_CASE

def affiche_pommes_mod_1(pommes):
    '''
    Fonction recevant la liste correspondant au coordonnées de la pomme
    et renvoit une forme de pomme sur la fenetre de coordonnées aléatoires
    différentes de celles du serpent.

    :param lst pommes: liste de coordonees de la pomme
    '''
    for _ in pommes:
        casea = (a, b)
        coa = case_vers_pixel(casea)
        idc = 'idc'
        idr = 'idr'
        idcercle = ''
        ancien_idcercle = idcercle
        while ancien_idcercle == idcercle :
            idcercle = cercle(coa[0], coa[1], TAILLE_CASE/2,
            couleur='darkred', remplissage='red',tag='idc')
            rectangle(coa[0]-2, coa[1]-TAILLE_CASE*.4, coa[0]+2, coa[1]-TAILLE_CASE*.7,
            couleur='darkgreen', remplissage='darkgreen',tag='idr')
    return (idc, idr)

def mange_pomme(serpent, POINT, idobjet):
    '''
    Fonction recevant la liste pomme, serpent, la variable POINT
    et les tags de la pomme, elle efface la pomme dessiner et
    ajoute 1 à la variable point.

    :param lst pomme : liste des coordonnes de la pomme
    :param lst serpent: liste des coordonnees du serpent
    :param int POINT: le compte des points
    '''
    casea = (a, b)
    casex = serpent[0][0], serpent[0][1]
    coa = case_vers_pixel(casea)
    cox = case_vers_pixel(casex)
    if coa[0]==cox[0] and coa[1]==cox[1]:
        efface(idobjet[0])
        efface(idobjet[1])
        POINT += 1
    return POINT

def mort(coordonnees):
    '''
    Fonction recevant les coordonees du serpent et si il dépasse
    les limites du plateau alors le jeu s'arrete.

    :param float cordionnees : coordonnees du serpent
    '''
    cox = coordonnees[0]
    coy = coordonnees[1]
    tempx = cox + direction[0]
    tempy = coy + direction[1]
    if cox >= LARGEUR_PLATEAU or cox <= 0 or coy >= HAUTEUR_PLATEAU or coy <= 0:
        reponse = False
    elif (tempx,tempy) in serpent and len(serpent) > 1 :
        reponse = False
    else:
        reponse = True
    return reponse

def affiche_serpent(serpent):
    '''
    Fonction recevant les coordonées du serpent
    puis dessine un cercle vert

    :param float serpent: coordonées du serpent
    '''
    for case in serpent:
        xmaille, ymaille = case_vers_pixel(case)
        cercle(xmaille, ymaille, TAILLE_CASE/2 + 1,
           couleur='darkgreen', remplissage='green')

def change_direction(direction, touche):
    '''
    Fonction recevant la direction initiale du serpent et les touche,
    renvoi une nouvelle direction

    :param float direction : direction initiale du serpent
    :param str touche : touche presser pour faire bouger le serpent
    >>> "Up"
    0,1
    '''
    # à compléter !!!
    if str(type(direction)) != "<class 'tuple'>":
        direction = (0, 0)
    if touche == 'Up' and direction != (0, 1) :
    # flèche haut pressée
        reponse = (0, -1)
    elif touche == 'Down' and direction != (0, -1) :
        reponse = (0, 1)
    elif touche == 'Right' and direction != (-1, 0) :
        reponse = (1, 0)
    elif touche == 'Left' and direction != (1, 0):
        reponse = (-1, 0)
    else:
        # pas de changement !
        reponse = direction
    return reponse

def deplacement(direction, serpent):
    '''
    Fonction recevant les coordonées du serpent
    et sa direction créer dans la precédente fonction
    puis renvoi de nouvelle coordonées
    pour le serpent

    :param float direction: direction initiale du serpent
    :param float serpent: coordonées du serpent
    '''
    # Tête du serpent
    cox,coy = serpent[0]

    # Nouvelles coordonnées de la tête
    # X = X + direction[0]*TAILLE_CASE
    # Y = Y + direction[1]*TAILLE_CASE
    cox = cox + direction[0]
    coy = coy + direction[1]

    # But de la manoeuvre :
    # Index de serpent :
    # [0][1][2] -> [0'][0][1][2] -> [2][1][0][0'] -> [1][0][0'] -> [0'][0][1]
    # Pour un décalage d'un cran des coordonnées du serpent vers la droite
    # et l'ajout des nouvelles coordonnées de la tête en premier.
    serpent.insert(0,(cox, coy))
    serpent.reverse()
    del serpent[0]
    serpent.reverse()
    return serpent

def coordonnees_hasard():
    '''
    Fonction qui crée des coordonnées aléatoires
    '''
    haa = randint(TAILLE_CASE, LARGEUR_PLATEAU)-1
    hab = randint(TAILLE_CASE, HAUTEUR_PLATEAU)-1
    return haa,hab

def rejouer(even):
    '''
    Fonction qui permet de rejouer, recevant un evenemment qu'il converti en
    chaine de caractere. Elle renvoi les valeurs booléennes de jouer et fin.

    param: even = str()
    >>>"ClicGauche"
    jouer,fin == True,True
    '''
    if str(even[0]) == "ClicGauche":
        play=True
        ending = True
    elif str(even[0]) == "ClicDroit":
        play=False
        ending = True
    return play,ending

# programme principal
if __name__ == "__main__":

    # initialisation du jeu
    COX = 20
    COY = 15
    a,b = coordonnees_hasard()
    POINT = 0
    direction = (1, 0)  # direction initiale du serpent
    pommes = [a, b] # liste des coordonnées des cases contenant des pommes
    serpent = [(COX, COY),(COX+2*TAILLE_CASE,COY)]
    # liste des coordonnées de cases adjacentes décrivant le serpent
    cree_fenetre(TAILLE_CASE * LARGEUR_PLATEAU,
                 TAILLE_CASE * HAUTEUR_PLATEAU)
    # boucle principale
    jouer = False
    texte(0, 0, "Bienvenue, appuyez sur n'importe quelle touche.",
          couleur='black', ancrage='nw', police='Helvetica', taille=12, tag='')
    attend_ev()
    jouer = True
    fin = True

    while jouer:
        FRAMERATE = 10
        if FRAMERATE <= 20 :
            FRAMERATE = FRAMERATE + POINT
        # affichage des objets
        # print(serpent)
        # affichage des objets
        efface_tout()
        idobjets = affiche_pommes_mod_1(pommes)
        # affiche_serpent(None)  # à modifier !
        serpent = deplacement(direction, serpent)
        fin = mort(serpent[0])
        affiche_serpent(serpent)
        #print(idobjets)
        ANCIEN_POINT = POINT
        POINT = mange_pomme(serpent, POINT, idobjets)

        # correction du défaut d'apparition sur la tête du serpent
        ANCIEN_OBJET = idobjets[0]
        if idobjets[0] == ANCIEN_OBJET:
            idobjets = affiche_pommes_mod_1(pommes)

        if ANCIEN_POINT != POINT:
            a,b = coordonnees_hasard()
            serpent.append((COX+POINT*TAILLE_CASE,COY))
        mise_a_jour()

        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        # if ty == 'Quitte':
        if ty == 'Touche' and touche(ev) == 'Escape':
            fin = False
        elif ty == 'Touche' and touche(ev) != 'Escape':
            # print(touche(ev))
            direction = change_direction(direction, touche(ev))
        texte(2, 2, "Vous avez fait un score de " + str(POINT) +".\n",
              couleur='black', ancrage='nw', police='Helvetica',
              taille=12, tag='')
        while not fin:
            texte(0, 0,
                  "\nVoulez-vous rejouer ? Si oui, faites clique gauche sinon faites clique droit",
                  couleur='black', ancrage='nw', police='Helvetica',
                  taille=12, tag='')
            ev = attend_ev()
            jouer,fin = rejouer(ev)
            if (jouer,fin) == (True,True):
                serpent = [(20, 15),(22*TAILLE_CASE,15)]
                FRAMERATE = 10
                POINT = 0
            elif (jouer,fin) == (False, True):
                ferme_fenetre()
        # attente avant rafraîchissement

        sleep(1/FRAMERATE)
