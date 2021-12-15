# -*- coding: utf-8 -*-
"""
Created on Fri May 14 10:42:38 2021

@author: thoma
"""


import pygame
YaxisValue=0 #valeur initiale de theta
axis_value=[0 for i in range(5)] #liste contenant les valeurs de chaque axe du joystick
joysticks=[] 
offset=[0 for i in range(5)] #liste de valeurs bruts récupérées sur les axes
pygame.joystick.init()

def begin(RepeatFrequency,step):
    global YaxisStep 
    YaxisStep = step
    pygame.key.set_repeat(RepeatFrequency)
    
af=0 #valeur initiale des aérofreins
afstep = 1 #valeur de l'incrément à chaque pression de la touche


for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    
for i in range (5): #cette boucle devrait récupérer la valeur initiale au repos (ne fonctionne pas)
    offset[i]=joysticks[0].get_axis(i) 
    
def Actualise():
    global YaxisValue
    global af
    global offset
    global joysticks
    global axis_value
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.JOYAXISMOTION:
            for i in range (5):
                axis_value[i]=joysticks[0].get_axis(i) - offset[i]
                if axis_value[2]>0.1:
                    YaxisValue += axis_value[2]/200
                if axis_value[2]<-0.1:
                    YaxisValue += axis_value[2]/200
                if axis_value[4]>0.98:
                    af = 0
                if axis_value[4]<0.98 :
                    freins = (axis_value[4] + 1)/2
                    pourcentage = 1 - freins
                    if af <= 100 :
                        af = 100 * pourcentage
        if event.type == pygame.KEYDOWN :
            # if event.key == pygame.K_h :
            #     if af < 100 :
            #         af += afstep #idem pour les aérofreins avec la touche h pour augmenter
            # if event.key == pygame.K_j:
            #     if af > 0:
            #         af -= afstep #et la touche j pour diminuer
            if event.key == pygame.K_ESCAPE :
                pygame.quit() #la touche échap permet de quitter le simulateur
    
           
    