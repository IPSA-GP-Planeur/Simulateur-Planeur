import pygame
import numpy as np

window_surface = None
hauteur = 0
largeur = 1000

sky = 135, 206, 235
dirt = 91, 60, 17
black = 0, 0, 0
white = 250, 250, 250
red = 242, 42, 42
arial_font = None


'''
def var_color(h):
    if h > 1000:
        color = 95, 65, 23
    elif h <=0:
        color = 255, 255, 255
    else :
        color = 255-h*0.159, 255-h*0.19, 255-h*0.232
    return color
'''


def Intersection(planeur, teta):

    Xp = planeur["Y"]
    Zp = planeur["Z"]

    # Calcul les intersections
    X_PointAffiche = []
    Y_PointAffiche = []
    X_PointsSol = [500 * i for i in range(4)]  # Abscisse des points au sol
    Z_PointsSol = [0 for i in range(len(X_PointsSol))]  # Ordonnée des points au sol
    CoordonneePointSol = [(X_PointsSol[i], Z_PointsSol[i]) for i in
                          range(len(X_PointsSol))]  # Liste avec les coordonnées des points au sol
    P = [Xp, Zp]  # Coordonnées du pilote fixe pour l'instant
    X_PointsSol.append(P[0])  # Pas très utile permet juste de rajouter le point du pilote dans le graph pyplot
    Z_PointsSol.append(P[1])  # Same
    X_Droite = np.linspace(X_PointsSol[2], P[0],
                           100)  # Créer les points d'abscisse pour la droite reliant LE point X1(A 500m) et le pilote
    Z_Droite = np.linspace(Z_PointsSol[2], P[1], 100)
    Xc = [P[0] + np.cos(np.radians(
        teta)) * 1]  # Abscisse Ecran de vision en face du pilote situé à un metre du pilote et dépendant de l'assiette
    Zc = [P[1] + np.sin(np.radians(
        teta)) * 1]  # Ordonnée Ecran de vision en face du pilote situé à un metre du pilote et dépendant de l'assiette'''
    Xa = [P[0] + np.cos(np.radians(
        teta) + np.pi / 4) * 2 ** 0.5]  # Abscisse écran de vision point superieur situé à un mètre du point C
    Za = [P[1] + np.sin(np.radians(
        teta) + np.pi / 4) * 2 ** 0.5]  # Ordonnée écran de vision point superieur situé à un mètre du point C
    Xb = [P[0] + np.cos(np.radians(
        teta) - np.pi / 4) * 2 ** 0.5]  # Abscisse écran de vision point inferieur situé à un mètre du point C
    Zb = [P[1] + np.sin(np.radians(
        teta) - np.pi / 4) * 2 ** 0.5]  # Ordonnée écran de vision point inferieur situé à un mètre du point C
    '''X_segmentAB = Xb+Xc+Xa  # Abscisse dans l'ordre pour tracer le segment'''
    '''Z_segmentAB = Zb+Zc+Za  #Ordonnes dans l'ordre pour tracer le segment'''
    # Droite d'eq de l'écran de vision
    CoeffDroiteEcran = (Zb[0] - Za[0]) / (
                Xb[0] - Xa[0])  # On obtient le coeff directeur de la droite qui est materialisé par l'écran de vision
    OrdonneOrigineEcran = Za[0] - CoeffDroiteEcran * Xa[
        0]  # On obtient l'ordonnée à l'origine de la droite qui est materialisé par l'écran de vision
    # print(CoeffDroiteEcran)
    # print(OrdonneOrigineEcran)
    # print("L'équation de la droite que forme l'ecran de vision est :\n y = {}x + {}".format(CoeffDroiteEcran,OrdonneOrigineEcran))
    # Droites d'eq entre le pilote et les points au sol
    CoeffDroitesSol = [(CoordonneePointSol[i][1] - P[1]) / (CoordonneePointSol[i][0] - P[0]) for i in range(
        len(CoordonneePointSol))]  # on trouve les coeffs dir des droites formees par les points pilote et sol
    OrdonneOrigineSol = [P[1] - P[0] * CoeffDroitesSol[i] for i in
                         range(len(CoordonneePointSol))]  # Pareil pour l'ordonée à l'origine
    # print("L'équation de la droite que forme les points sol et pilote est :\n y = {}x + {}".format(CoeffDroitesSol[1],OrdonneOrigineSol[1]))
    # Coordonnées du point d'intersection
    X_intersection = [(OrdonneOrigineSol[i] - OrdonneOrigineEcran) / (CoeffDroiteEcran - CoeffDroitesSol[i]) for i in
                      range(len(CoordonneePointSol))]  # On cherche l'abscisse du point d'intersection'''
    Z_intersection = [CoeffDroiteEcran * X_intersection[i] + OrdonneOrigineEcran for i in
                      range(len(CoordonneePointSol))]  # On cherche l'ordonnée du point d'intersection'''

    def convertion_x(x):
        return Zp * (abs(x - Xb[0])) / abs(Xa[0] - Xb[0])

    for i in range(len(CoordonneePointSol)):  # metre dans des listes les coordonnées des points a afficher
        if (abs(Zc[0] - Z_intersection[i]) + abs(Xc[0] - X_intersection[i])) ** (1 / 2) < (
                abs(Zc[0] - Zb[0]) + abs(Xc[0] - Xb[0])) ** (1 / 2):
            X_PointAffiche.append(convertion_x(X_intersection[i]))
            Y_PointAffiche = [largeur / 2 for i in range(len(X_PointAffiche))]
    return X_PointAffiche, Y_PointAffiche


def begin(ScreenWidth, ScreenHeight):
    global window_surface
    global arial_font
    global hauteur, largeur

    hauteur = ScreenHeight
    largeur = ScreenWidth

    pygame.init()
    window_surface = pygame.display.set_mode(size=(ScreenWidth, ScreenHeight))
    arial_font = pygame.font.SysFont("arial", 30)


def Display(commandePlaneur, planeur, Intersec):
    global window_surface
    global hauteur
    global largeur
    global arial_font
    global black
    global dirt
    global sky
    global red


    rect_form = pygame.Rect(0, (hauteur / 2 + commandePlaneur["Y"] * 3) - 200 + 0.2 * planeur["Z"], largeur, hauteur)

    pygame.draw.rect(window_surface, dirt, rect_form)

    pygame.draw.line(window_surface, black, [0, (hauteur / 2 + commandePlaneur["Y"] * 3) - 200 + 0.2 * planeur["Z"]],
                     [largeur, (hauteur / 2 + commandePlaneur["Y"] * 3) - 200 + 0.2 * planeur["Z"]], 5)
    "hf"

    rect_sky = pygame.Rect(0, 0, largeur, (hauteur / 2 + commandePlaneur["Y"] * 3) - 200 + 0.2 * planeur["Z"])

    pygame.draw.rect(window_surface, sky, rect_sky)

    pygame.draw.circle(window_surface, red, [largeur / 2, 2.25 * hauteur / 3], 4)  # Ajout Sam

    if planeur["Z"] < 100 and planeur["Vz"] < -1:
        a = pygame.image.load('accident.png')  # charge une image de crsh
        b = pygame.transform.scale(a, (100, 100))  # redimmensionne image
        window_surface.blit(b, (900, 900))  # affiche image

    # display text
    vitesse_verticale = arial_font.render('Vz : {:.2f} m/s'.format(planeur["Vz"]), True, (0, 0, 0))
    vitesse_horizontal = arial_font.render('Vh : {:.2f} km/h'.format(planeur["Vy"] * 3, 6), True, (0, 0, 0))
    assiette = arial_font.render('θ: {:.2f}°'.format(commandePlaneur["Y"]), True, (0, 0, 0))
    Haltitude = arial_font.render('H : {:.2f} m'.format(planeur["Z"]), True, (0, 0, 0))
    aerofreins = arial_font.render('af: {:.2f}%'.format(commandePlaneur["Spoiler"]), True, (0, 0, 0))
    finesse = arial_font.render('f: {:.2f}'.format(abs(planeur["Vy"] / planeur["Vz"])), True, (0, 0, 0))
    T = arial_font.render('T : {:.2f} {:.2f}'.format(Intersec[0][0], Intersec[1][0]), True, (0, 0, 0))
    for i in range(len(Intersec[0])):
        pygame.draw.line(window_surface, black, [0, hauteur - Intersec[0][i]], [largeur, hauteur - Intersec[0][i]])

    window_surface.blit(vitesse_verticale, (30, 30))
    window_surface.blit(vitesse_horizontal, (30, 70))
    window_surface.blit(Haltitude, (30, 110))
    window_surface.blit(assiette, (30, 160))
    window_surface.blit(aerofreins, (30, 210))
    window_surface.blit(finesse, (300, 30))
    window_surface.blit(T, (30, 260))

    pygame.display.flip()


'''
---------------------------------------------------------------------
Ca sert à quoi?
---------------------------------------------------------------------
def display(a, b, c, d):
    global window_surface

    window_surface.fill((255, 255, 255))

    window_surface.fill((0, 255, 0), rect=[0, 0, 500, 250])

    window_surface.fill((255, 0, 0), rect=[0, 250, 500, 250])
    
    pygame.display.update()
'''
