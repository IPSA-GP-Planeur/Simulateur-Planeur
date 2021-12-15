#define PORT_ANEMOMETRE 3
#define PORT_ALTIMETRE 5
#define PORT_VARIOMETRE 6

#define PORT_POT_MANCHE_AXE_1 A0
#define PORT_POT_MANCHE_AXE_2 A1
#define PORT_POT_AEROFREIN A2
#define PORT_POT_PALONNIER A3


#include <Servo.h>

Servo anemometre;
Servo altimetre;
Servo variometre;

int valPotMancheAxe1,valPotMancheAxe1_old;
int valPotMancheAxe2,valPotMancheAxe2_old;
int valPotAerofrein, valPotAerofrein_old;
int valPotPalonnier, valPotPalonnier_old;


int valServoAnemometre;
int valServoAltimetre;
int valServoVariometre;

String cmd = "";


void setup() {
  Serial.begin(9600);
  anemometre.attach(PORT_ANEMOMETRE);
  altimetre.attach(PORT_ALTIMETRE);
  variometre.attach(PORT_VARIOMETRE);
}


void inputData() {
  valPotMancheAxe1 = analogRead(PORT_POT_MANCHE_AXE_1);
  valPotMancheAxe2 = analogRead(PORT_POT_MANCHE_AXE_2);
  valPotAerofrein = analogRead(PORT_POT_AEROFREIN);
  valPotPalonnier = analogRead(PORT_POT_PALONNIER);
}

void exportDataSimu() {
  if (valPotMancheAxe1_old != valPotMancheAxe1){
    valPotMancheAxe1_old = valPotMancheAxe1;
    Serial.print("!MA1");
    Serial.println(valPotMancheAxe1);
  }
  if (valPotMancheAxe2_old != valPotMancheAxe2){
    valPotMancheAxe2_old = valPotMancheAxe2;
    Serial.print("!MA2");
    Serial.println(valPotMancheAxe2);
  }
  if (valPotPalonnier_old != valPotPalonnier){
    valPotPalonnier_old = valPotPalonnier;
    Serial.print("!PAL");
    Serial.println(valPotPalonnier);
  }
  if (valPotAerofrein_old != valPotAerofrein){
    valPotAerofrein_old = valPotAerofrein;
    Serial.print("!AER");
    Serial.println(valPotAerofrein);
  }
}

void importDataSimu() {

  if (Serial.available() > 0) {

    char SerialInByte = Serial.read();

    if (SerialInByte == 10) {
      if (cmd.substring(0, 3) == "ANE") {
        valServoAnemometre = cmd.substring(3).toInt();
      } else if (cmd.substring(0, 3) == "ALT") {
        valServoAltimetre = cmd.substring(3).toInt();
      } else if (cmd.substring(0, 3) == "VAR") {
        valServoVariometre = cmd.substring(3).toInt();
      }
      cmd = "";
      Serial.flush();
    } else {
      cmd += String(SerialInByte);
    }
  }
  delay(10);
}

void outputData() {
  anemometre.write(valServoAnemometre);
  altimetre.write(valServoAltimetre);
  variometre.write(valServoVariometre);
}

void outputDataDebug() {
  Serial.print("anemometre ");
  Serial.print(valServoAnemometre);
  Serial.print(", altimetre ");
  Serial.print(valServoAltimetre);
  Serial.print(", variometre ");
  Serial.println(valServoVariometre);
}

void loop() {
  Serial.println(millis());
  inputData();
  exportDataSimu();
  importDataSimu();
  outputData();
}
