import serial
import serial.tools.list_ports

availablePorts = serial.tools.list_ports.comports()
for port in availablePorts:
    if "Arduino" in port.description:
        portArduino = port.name

with serial.Serial(portArduino, 9600) as arduino:
    while True:
        if arduino.read().decode('utf-8') == '!':
            valInstrument = []
            commande = arduino.read_until().decode('UTF-8')
            valInstrument.append(commande[0:3])
            valInstrument.append(commande[3:])
            print("instru", valInstrument[0], "valInstrument", valInstrument[1])
