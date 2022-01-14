import Gestionnaire_Evenement as WindowEvent 
import Moteur_Graphique as GraphicPane
import Moteur_Physique as Physics
import time

ExecutionTime = time.time()
TimeStep = 0.1

planeur = {"Y": 0, "Z": 1000, "Vy": 30, "Vz": -1}


# i = 0 #compteur


def begin():
    GraphicPane.begin(500, 500)
    WindowEvent.begin(10, 0.01)


def __main__():
    global ExecutionTime
    global TimeStep
    global planeur

    if time.time() >= ExecutionTime:
        ExecutionTime += TimeStep
        planeur = Physics.ExecuteEuler(WindowEvent.YaxisValue, WindowEvent.SpoilerValue, planeur, TimeStep)

    GraphicPane.Display(WindowEvent.YaxisValue, planeur, WindowEvent.SpoilerValue)
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