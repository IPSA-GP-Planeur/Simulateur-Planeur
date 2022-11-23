#define PORT_SERVO_ANEMOMETRE 6
#define PORT_SERVO_ALTIMETRE1 3
#define PORT_SERVO_ALTIMETRE2 5
#define PORT_SERVO_VARIOMETRE 9

#define VALEUR_LIMITE_ANEMOMETRE 178
#define VALEUR_LIMITE_ALTIMETRE1 179
#define VALEUR_LIMITE_ALTIMETRE2 179
#define VALEUR_INF_LIMITE_VARIOMETRE 12
#define VALEUR_MIL_LIMITE_VARIOMETRE 92
#define VALEUR_SUP_LIMITE_VARIOMETRE 177


#include <Servo.h>

Servo anemometre;
Servo altimetre1;
Servo altimetre2;
Servo variometre;

byte valServoAnemometre = 0;
byte valServoAltimetre1 = 0;
byte valServoAltimetre2 = 0;
byte valServoVariometre = 0;

String commande = "";

void setup() {
  Serial.begin(9600);

  anemometre.attach(PORT_SERVO_ANEMOMETRE);
  altimetre1.attach(PORT_SERVO_ALTIMETRE1);
  altimetre2.attach(PORT_SERVO_ALTIMETRE2);
  variometre.attach(PORT_SERVO_VARIOMETRE);
}

void loop() {
  if (Serial.available() > 0) {
    // check si un message arrive sur le port série

    char caractere = Serial.read();
    // stocke le caractère reçue

    if (caractere == '\n') {

      if (commande.substring(0, 3) == "ANE") { //valeur sur le cadran
        Serial.println(commande.substring(3).toInt());
        valServoAnemometre = map(constrain(commande.substring(3).toInt(), 20, 240), 20, 240, 0, VALEUR_LIMITE_ANEMOMETRE);
        Serial.println(valServoAnemometre);
        anemometre.write(valServoAnemometre);

      } else if (commande.substring(0, 3) == "ALT") { //valeur sur le cadran
        Serial.println(commande.substring(3).toInt());
        Serial.println(commande.substring((commande.length()) - 3).toInt());
        valServoAltimetre1 = map(commande.substring(3).toInt(), 0, 9132, 0, VALEUR_LIMITE_ALTIMETRE1);
        valServoAltimetre2 = map(commande.substring((commande.length()) - 3).toInt(), 0, 886, 0, VALEUR_LIMITE_ALTIMETRE2);
        Serial.println(valServoAltimetre1); 
        Serial.println(valServoAltimetre2);
        altimetre1.write(valServoAltimetre1);
        altimetre2.write(valServoAltimetre2);
        
      } else if (commande.substring(0, 3) == "VAR") { //valeur sur le cadran
        Serial.println(commande.substring(3).toInt());
        valServoVariometre = (commande.substring(3).toInt() > 0) ? map(commande.substring(3).toInt(), 0, 500, VALEUR_MIL_LIMITE_VARIOMETRE, VALEUR_SUP_LIMITE_VARIOMETRE) : map(-commande.substring(3).toInt(), 500, 0, VALEUR_INF_LIMITE_VARIOMETRE, VALEUR_MIL_LIMITE_VARIOMETRE);
        Serial.println(valServoVariometre);
        variometre.write(valServoVariometre);

      } else if (commande.substring(0, 3) == "ALL") { //valeur en degré sur 180°
        Serial.println(commande.substring(3).toInt());
        anemometre.write(constrain(commande.substring(3).toInt(), 0, VALEUR_LIMITE_ANEMOMETRE));
        altimetre1.write(constrain(commande.substring(3).toInt(), 0, VALEUR_LIMITE_ALTIMETRE1));
        altimetre2.write(constrain(commande.substring(3).toInt(), 0, VALEUR_LIMITE_ALTIMETRE2));
        variometre.write(constrain(commande.substring(3).toInt(), VALEUR_INF_LIMITE_VARIOMETRE, VALEUR_SUP_LIMITE_VARIOMETRE));
      }

      commande = ""; // vider la chaine de caractère
      Serial.flush(); // vider la memoire d'entrée du port série
    } else {
      commande += String(caractere); // si le caractère n'est pas \n, ajouter le caractère à la chaîne de caractère
    }
  }
}
