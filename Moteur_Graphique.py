import pygame

window_surface = None
largeur = 0
longueur = 0

sky = 135, 206, 235
dirt = 91, 60, 17
black = 0, 0, 0
arial_font = None


def begin(ScreenWidth, ScreenHeight):
    global window_surface
    global arial_font
    global largeur, longueur

    largeur = ScreenHeight
    longueur = ScreenWidth

    pygame.init()
    window_surface = pygame.display.set_mode(size=(ScreenWidth, ScreenHeight))
    arial_font = pygame.font.SysFont("arial", 30)


def Display(commandePlaneur, planeur):
    global window_surface
    global largeur
    global longueur
    global arial_font
    global black
    global dirt
    global sky

    rect_form = pygame.Rect(0, largeur / 2 + commandePlaneur["Y"] * 3, longueur, largeur)

    pygame.draw.rect(window_surface, dirt, rect_form)

    rect_sky = pygame.Rect(0, 0, longueur, largeur / 2 + commandePlaneur["Y"] * 3)

    pygame.draw.rect(window_surface, sky, rect_sky)

    pygame.draw.line(window_surface, black, [0, largeur / 2 + commandePlaneur["Y"] * 3],
                     [longueur, largeur / 2 + commandePlaneur["Y"] * 3], 5)

    # display text
    vitesse_verticale = arial_font.render('Vz : {:.2f} m/s'.format(planeur["Vz"]), True, (0, 0, 0))
    vitesse_horizontal = arial_font.render('Vh : {:.2f} km/h'.format(planeur["Vy"] * 3.6), True, (0, 0, 0))
    assiette = arial_font.render('θ: {:.2f}°'.format(commandePlaneur["Y"]), True, (0, 0, 0))
    Haltitude = arial_font.render('H : {:.2f} m'.format(planeur["Z"]), True, (0, 0, 0))
    aerofreins = arial_font.render('af: {:.2f}%'.format(commandePlaneur["Spoiler"]), True, (0, 0, 0))
    finesse = arial_font.render('f: {:.2f}'.format(abs(planeur["Vy"] / planeur["Vz"])), True, (0, 0, 0))

    window_surface.blit(vitesse_verticale, (30, 30))
    window_surface.blit(vitesse_horizontal, (30, 70))
    window_surface.blit(Haltitude, (30, 110))
    window_surface.blit(assiette, (30, 160))
    window_surface.blit(aerofreins, (30, 210))
    window_surface.blit(finesse, (300, 30))

    pygame.display.flip()
