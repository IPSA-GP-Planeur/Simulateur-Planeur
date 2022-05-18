import Gestionnaire_Evenement as WindowEvent
import Moteur_Graphique as GraphicPane
import Moteur_Physique as Physics
import time

ExecutionTime = time.time()
TimeStep = 0.1

planeurCylindrique = {"r": 1, "theta": 0, "z": 1000, "rp": 25, "thetap": 0, "zp": -1}
planeurCartesien = {"X": 0, "Y": 0, "Z": 1000, "Vy": 30, "Vz": -1, "Vz": 0}


# i = 0 #compteur


def begin():
    GraphicPane.begin(500, 500)
    WindowEvent.begin(10, 0.01)


def __main__():
    global ExecutionTime
    global TimeStep
    global planeurCartesien
    global planeurCylindrique

    commandePlaneur = WindowEvent.Actualise()

    if time.time() >= ExecutionTime:
        ExecutionTime += TimeStep
        planeurCylindrique, planeurCartesien = Physics.ExecuteEuler(commandePlaneur, planeurCylindrique, TimeStep)

    GraphicPane.Display(commandePlaneur, planeurCartesien)


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
    __main__()
