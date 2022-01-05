import pygame


#le programme va simuler l'input d'un joystick en attendant qu'on en incorpore 1



YaxisStep = 10             #valeur de l'incrément a chaque pression sur la fleche
YaxisValue = 0            #valeur de l'assiete initiale

af=0
afstep = 1


def begin(RepeatFrequency,step):
    global YaxisStep 
    YaxisStep = step
    pygame.key.set_repeat(RepeatFrequency)
    
    
def Actualise():           #méthode pour actualiser les actions sur le clavier et la fenetre

    global YaxisValue
    global af
    #On récupère les valeurs de l'assiette et des aérofreins
    
    for event in pygame.event.get():
        #attribue a des actions de l'utilisateur une réponse du programme
        if event.type == pygame.QUIT:
            
            pygame.quit() #échap => quitter le programme
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                YaxisValue -= YaxisStep #pour chaque pression sur la touche on diminue la valeur de theta
                    
            if event.key == pygame.K_DOWN:
             
                YaxisValue += YaxisStep #on augmente sa valeur 
           
            if event.key == pygame.K_h:
                
                if af < 100 :
                    af += afstep #idem pour les aérofreins avec la touche h pour augmenter
                
            if event.key == pygame.K_j:
                
                if af > 0:
                    af -= afstep #et la touche j pour diminuer
            