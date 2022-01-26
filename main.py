import Gestionnaire_Evenement as WindowEvent 
import Moteur_Graphique as GraphicPane
import Moteur_Physique as Physics
import time
from matplotlib import pyplot as plt
from matplotlib import axes as ax
import numpy as np

ExecutionTime = 0
TimeStep = 0.1

i = 0 #compteur

def begin():
    Physics.SetTimeStep(TimeStep)
    GraphicPane.begin(1000,1000)
    WindowEvent.begin(10,0.01)

def __main__():
    global ExecutionTime
    global TimeStep
    global A
    global i
    
    if(time.time() >= ExecutionTime):
        ExecutionTime = time.time() + TimeStep
 
        A = Physics.ExecuteEuler(WindowEvent.YaxisValue)
        
  
    GraphicPane.Display(WindowEvent.YaxisValue,A[3],A[2],A[1],WindowEvent.af)
    WindowEvent.Actualise()
 
''' 
Test de programme pour afficher graphique en temps réel
    if i%100 == 0 :
        plt.scatter(A[0],A[1], c='black')
        plt.pause(0.0001)
    i+=1
    plt.xlabel("Distance (m)")
    plt.ylabel("Altitude (m)")
    ax.set_xlim(A[0] + 10)
    ax.set_ylim(A[1] + 10)
    plt.show()
'''    
    
    
begin()
while True:
    
    __main__();