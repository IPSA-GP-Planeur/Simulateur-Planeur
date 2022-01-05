import pygame

window_surface = None
largeur = 0
longueur = 0

sky=135,206,235
dirt=91,60,17
black = 0, 0, 0
white = 250,250,250
arial_font = None


def begin(ScreenWidth,ScreenHeight):
    global window_surface

    global arial_font
    
    global largeur,longueur
    
    largeur = ScreenHeight
    longueur = ScreenWidth
    
    pygame.init()
    window_surface = pygame.display.set_mode(size=(ScreenWidth,ScreenHeight))
    arial_font = pygame.font.SysFont("arial", 30)
    
    
def Display(positionY,vitesseVerticale,vx_new,h,freins):
    
    
    global window_surface
    global largeur
    global longeur
    global arial_font
    global black
    global dirt
    global sky
 
    rect_form=pygame.Rect(0,largeur/2+positionY*3,longueur,largeur)
    
    pygame.draw.rect(window_surface,dirt,rect_form)
    
    pygame.draw.line(window_surface,black,[0,largeur/2+positionY*3],[longueur,largeur/2+positionY*3],5)

    pygame.draw.line(window_surface,white,[0*longueur/5,(3*largeur/4+positionY*3)-200+0.2*h],[5*longueur/5,(3*largeur/4+positionY*3)-200+0.2*h],4) #Ajout ligne horizontale haute dépendant de la hauteur
    pygame.draw.line(window_surface,white,[0*longueur/5,(14*largeur/16+positionY*3)+200-0.2*h],[5*longueur/5,(14*largeur/16+positionY*3)+200-0.2*h],4) #Ajout ligne horizontale basse dépendant de la hauteur

    pygame.draw.line(window_surface,white,[(2*longueur/14)-250+h/4,largeur/2+positionY*3],[(1*longueur/14)-1000+h,largeur],2)#ligne verticale gauche  
    pygame.draw.line(window_surface,white,[(4*longueur/14)-250+h/4,largeur/2+positionY*3],[(3*longueur/14)-1000+h,largeur],2)#ligne verticale gauche  
    pygame.draw.line(window_surface,white,[(6*longueur/14)-250+h/4,largeur/2+positionY*3],[(5*longueur/14)-1000+h,largeur],2)#ligne verticale gauche  
    pygame.draw.line(window_surface,white,[(8*longueur/14)+250-h/4,largeur/2+positionY*3],[(9*longueur/14)+1000-h,largeur],2)#ligne verticale droite
    pygame.draw.line(window_surface,white,[(10*longueur/14)+250-h/4,largeur/2+positionY*3],[(11*longueur/14)+1000-h,largeur],2)#ligne verticale droite  
    pygame.draw.line(window_surface,white,[(12*longueur/14)+250-h/4,largeur/2+positionY*3],[(13*longueur/14)+1000-h,largeur],2)#ligne verticale droite
    
    rect_sky=pygame.Rect(0,0,longueur,largeur/2+positionY*3)#déplacement ciel pour passer au premier plan
    
    pygame.draw.rect(window_surface,sky,rect_sky)

    # display text
    
    
    vitesse_verticale = arial_font.render('Vz : {:.2f} m/s'.format(vitesseVerticale), True, (0,0,0) )
    vitesse_horizontal = arial_font.render('Vh : {:.2f} km/h'.format(vx_new*3,6), True, (0,0,0) )
    assiette = arial_font.render('θ: {:.2f}°'.format(positionY), True, (0,0,0) )
    Haltitude = arial_font.render('H : {:.2f} m'.format(h), True, (0,0,0) )   
    aerofreins = arial_font.render('af: {:.2f}%'.format(freins), True, (0,0,0) )
    finesse = arial_font.render('f: {:.2f}'.format(abs(vx_new/vitesseVerticale)), True, (0,0,0) )
    
    window_surface.blit(vitesse_verticale,(30,30))    
    window_surface.blit(vitesse_horizontal,(30,70)) 
    window_surface.blit(Haltitude,(30,110)) 
    window_surface.blit(assiette,(30,160))  
    window_surface.blit(aerofreins,(30,210))
    window_surface.blit(finesse,(300,30))
    
       
    pygame.display.flip()
    

def display(a,b,c,d):
    
    global window_surface
        
    window_surface.fill((255,255,255))
    
    
    window_surface.fill((0,255,0),rect=[0,0,500,250])
    
    
    
    window_surface.fill((255,0,0),rect=[0,250,500,250])
    pygame.display.update()