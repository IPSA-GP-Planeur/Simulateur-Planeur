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
    WindowEvent.begin()


def __main__():
    global ExecutionTime
    global TimeStep
    global planeurCartesien
    global planeurCylindrique

    commandePlaneur = WindowEvent.actualiseInput()

    if time.time() >= ExecutionTime:
        ExecutionTime += TimeStep
        planeurCylindrique, planeurCartesien = Physics.ExecuteEuler(commandePlaneur, planeurCylindrique, TimeStep)
        WindowEvent.actualiseOutput(planeurCartesien)
        GraphicPane.Display(commandePlaneur, planeurCartesien)


begin()
while True:
    __main__()
