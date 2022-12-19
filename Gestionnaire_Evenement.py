import pygame

# le programme va simuler l'input d'un joystick en attendant qu'on en incorpore 1

commandePlaneur = {"X": 0, "Y": -1, "Spoiler": 0}
# avec une assiette de 0 le code ne fonctionne pas !!!


quitter = pygame.image.load('accident.png') # charge l'image
quitter = pygame.transform.scale(quitter, (200,200))
quitter_rect = quitter.get_rect()
quitter_rect.x = 200
quitter_rect.y = 200


def begin(RepeatFrequency, step):
    global YaxisStep, XaxisStep, afstep
    YaxisStep, XaxisStep, afstep = step, step, step
    pygame.key.set_repeat(RepeatFrequency)


def Actualise():  # méthode pour actualiser les actions sur le clavier et la fenetre

    global commandePlaneur
    # On récupère les valeurs de l'assiette et des aérofreins

    global quitter_rect

    for event in pygame.event.get():
        # attribue a des actions de l'utilisateur une réponse du programme
        if event.type == pygame.QUIT:
            pygame.quit()  # échap => quitter le programme

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                commandePlaneur["Y"] -= YaxisStep  # pour chaque pression sur la touche on diminue la valeur de theta

            if event.key == pygame.K_DOWN:
                commandePlaneur["Y"] += YaxisStep  # on augmente sa valeur

            if event.key == pygame.K_RIGHT:
                commandePlaneur["X"] -= XaxisStep #pour chaque pression sur la touche on diminue la valeur de theta
            
            if event.key == pygame.K_LEFT:
                commandePlaneur["X"] += XaxisStep #pour chaque pression sur la touche on augmente la valeur de theta
            
            if event.key == pygame.K_h:

                if commandePlaneur["Spoiler"] < 100:
                    commandePlaneur["Spoiler"] += afstep  # idem pour les aérofreins avec la touche h pour augmenter

            if event.key == pygame.K_j:

                if commandePlaneur["Spoiler"] > 0:
                    commandePlaneur["Spoiler"] -= afstep  # et la touche j pour diminuer
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if quitter_rect.collidepoint(event.pos):
                pygame.quit()  

    return commandePlaneur
