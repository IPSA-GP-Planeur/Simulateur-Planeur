import Gestionnaire_Evenement as WindowEvent
# import Moteur_Graphique as GraphicPane
import Moteur_GraphTestNew as GraphicPane
# import Moteur_Physique_cylindrique as Physics
import Moteur_Physique_cartésien as Physics
import time

ExecutionTime = time.time()
TimeStep = 0.1

planeurCartesien = {"Y": 0, "Z": 2000, "Vy": 70, "Vz": -1}
# planeurCylindrique = {"r": 1, "theta": 0, "z": 1000, "rp": 25, "thetap": 0, "zp": -1}


def begin():
    GraphicPane.begin(700,700)
    WindowEvent.begin(10, 0.01)


def __main__():
    global ExecutionTime
    global TimeStep
    global planeurCartesien
    # global planeurCylindrique
    global intersec

    commandePlaneur = WindowEvent.Actualise()

    if time.time() >= ExecutionTime:
        ExecutionTime += TimeStep
        # planeurCylindrique, planeurCartesien = Physics.ExecuteEuler(commandePlaneur, planeurCylindrique, TimeStep)
        planeurCartesien = Physics.ExecuteEuler(commandePlaneur, planeurCartesien, TimeStep)
        intersec = GraphicPane.Intersection(planeurCartesien["Y"], planeurCartesien["Z"], commandePlaneur["Y"])

    GraphicPane.Display(commandePlaneur, planeurCartesien, intersec)
    # GraphicPane.Display(commandePlaneur, planeurCartesien)

begin()
while True:
    __main__()
