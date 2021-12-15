import time
import serial
import serial.tools.list_ports

with serial.Serial() as arduino:

    def begin():
        available_ports = serial.tools.list_ports.comports()
        for port in available_ports:
            if "Arduino" in port.description:
                port_arduino = port.name
        arduino.baudrate = 9600
        arduino.port = port_arduino
        arduino.bytesize = serial.EIGHTBITS
        arduino.parity = serial.PARITY_NONE
        arduino.stopbits = serial.STOPBITS_ONE
        arduino.open()
        time.sleep(2)
        return


    def actualiseInput():
        global XaxisValue
        global YaxisValue
        global ZaxisValue
        global spoilerValue
        arduino.write(b'REL\n')
        for i in range(4):
            commande = arduino.read_until().decode('utf-8')  # lit jusqu'à \n
            if commande[0:3] == 'MA1':
                XaxisValue = commande[3:-2] # supprime le \r en fin de commande du au println
            if commande[0:3] == 'MA2':
                YaxisValue = commande[3:-2]
            if commande[0:3] == 'PAL':
                ZaxisValue = commande[3:-2]
            if commande[0:3] == 'AER':
                spoilerValue = commande[3:-2]
        #print("X", XaxisValue, "Y", YaxisValue, "Z", ZaxisValue, "Spoiler", spoilerValue)
        return


    def actualiseOutput(anemometre, altimetre, variometre):
        arduino.write(b'ANE')
        arduino.write(str(anemometre).encode('utf-8'))
        arduino.write(b'\nALT')
        arduino.write(str(altimetre).encode('utf-8'))
        arduino.write(b'\nVAR')
        arduino.write(str(variometre).encode('utf-8'))
        arduino.write(b'\n')
        #print(arduino.read_until())
        #print(arduino.read_until())
        #print(arduino.read_until())
        return


#begin()
#actualiseInput()
#actualiseOutput(100, 25, 63)

"""
Bon voilà, comme vous pouvez le constater, j'ai pas de vie xD

Explications:
begin() est a appelé une fois au début pour connecter l'arduino (attention y a un délai de 2 secondes qui est nécessaire)
actualiseInput() retourne XaxisValue YaxisValue ZaxisValue et spoilerValue avec des valeurs entre 0 et 1023
et enfin actualiseOutput(anemometre, altimetre, variometre) prend 3 paramètres qui comme leurs noms l'indique
sont la position de l'aiguille pour chaque instrument (valeur entre 0 et 255)
"""
