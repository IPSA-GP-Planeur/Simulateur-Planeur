import Gestionnaire_Evenement as WindowEvent
import Moteur_Graphique as GraphicPane
import Moteur_Physique as Physics
import time

ExecutionTime = time.time()
TimeStep = 0.1

planeur = {"Y": 0, "Z": 5000, "Vy": 30, "Vz": -1}


def begin():
    GraphicPane.begin(500, 500)
    WindowEvent.begin()


def __main__():
    global ExecutionTime
    global TimeStep
    global planeur

    commandePlaneur = WindowEvent.actualiseInput()

    if time.time() >= ExecutionTime:
        ExecutionTime += TimeStep
        planeur = Physics.ExecuteEuler(commandePlaneur, planeur, TimeStep)
        WindowEvent.actualiseOutput(planeur)
        GraphicPane.Display(commandePlaneur, planeur)


begin()
while True:
    __main__()
