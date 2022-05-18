from time import sleep  # importe la fonction sleep de la bibliothèque time
import serial  # importe la bibliothèque pyserial qui gère la communication série
import serial.tools.list_ports  # importe l'outil list.ports qui sert à lister les ports séries disponibles

with serial.Serial() as arduino:  # défini arduino comme la fonction serial.Serial()

    # fonction d'initialisation de la communication série avec l'Arduino
    def begin():

        available_ports = serial.tools.list_ports.comports()
        # récupère la liste des ports séries disponibles

        for port in available_ports:
            if "Arduino" in port.description:
                portArduino= port.name
                # récupère le port où est connecté l'Arduino

        arduino.baudrate = 9600
        arduino.port = portArduino
        arduino.bytesize = serial.EIGHTBITS
        arduino.parity = serial.PARITY_NONE
        arduino.stopbits = serial.STOPBITS_ONE
        # suite de paramétrages de la communication série

        arduino.open()  # ouverture de la communication série avec l'Arduino (ce qui le fait reboot)
        sleep(2)  # attendre 2 sec que l'Arduino reboot
        return

    # fonction d'actualisation des potentiomètres
    def actualiseInput():

        global dataCellule
        dataCellule = {}
        # définition d'une bibliothèque qui stockera l'information sur les potentiomètres

        arduino.write(b'REL\n')
        # envoie la suite de caractère 'REL' pour reload suivi d'un retour à la ligne (\n)

        for i in range(4):  # répète 4 fois la réception des données pour récupérer les données des 4 potentiomètres
            commande = arduino.read_until().decode('utf-8')  # lit jusqu'à \n et traduit du binaire en utf-8
            if commande[0:3] == 'MAX': # si le message commence par 'MAX', la variable correspond à l'axe x (manche axe x)
                dataCellule['XaxisValue'] = int(commande[3:-2])  # supprime le \r en fin de commande dû au println en arduino, ex cmd: MAX42\r\n et convertit en entier
            if commande[0:3] == 'MAY': # (manche axe y)
                dataCellule['YaxisValue'] = int(commande[3:-2])
            if commande[0:3] == 'PAL': # (palonnier)
                dataCellule['ZaxisValue'] = int(commande[3:-2])
            if commande[0:3] == 'AER': # (aerofrein)
                dataCellule['SpoilerValue'] = int(commande[3:-2])
        return dataCellule

commandePlaneur = {"X": 0, "Y": 0, "Spoiler": 0}

    def XaxisValue(): return dataCellule['XaxisValue']

    def YaxisValue(): return dataCellule['YaxisValue']

    def ZaxisValue(): return dataCellule['ZaxisValue']

    def SpoilerValue(): return dataCellule['SpoilerValue']


    # fonction d'actualisation des servomoteurs
    def actualiseOutput(anemometre, altimetre, variometre):
        arduino.write(b'ANE')
        arduino.write(str(anemometre).encode('utf-8'))
        arduino.write(b'\nALT')
        arduino.write(str(altimetre).encode('utf-8'))
        arduino.write(b'\nVAR')
        arduino.write(str(variometre).encode('utf-8'))
        arduino.write(b'\n')
        # envoie chaque variable avec un préfixe qui permet de la reconnaître et un suffixe '\n' qui signifie la fin du message
        return


"""
Utilisation:

begin() est a appelé une fois au début pour connecter l'arduino (attention y a un délai de 2 secondes 
qui est nécessaire)

actualiseInput() retourne un dictionnaire avec comme clé XaxisValue YaxisValue ZaxisValue et spoilerValue 
avec des valeurs entre 0 et 1023

actualiseOutput(anemometre, altimetre, variometre) prend 3 paramètres qui comme leurs noms l'indique
sont la position de l'aiguille pour chaque instrument (valeur entre 0 et 255)
"""
