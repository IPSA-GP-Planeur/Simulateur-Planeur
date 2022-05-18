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

    if (caractere == 10) {
      Serial.println(commande.toInt());
//      valServoAnemometre = map(constrain(commande.toInt() , 20, 240), 20, 240, 0, VALEUR_LIMITE_ANEMOMETRE);
//      Serial.println(constrain(valServoAnemometre, 0, VALEUR_LIMITE_ANEMOMETRE));
//      anemometre.write(constrain(valServoAnemometre, 0, VALEUR_LIMITE_ANEMOMETRE));
      
      valServoAltimetre1 = map(commande.toInt(), 0, 9132, 0, VALEUR_LIMITE_ALTIMETRE1);
      Serial.println(constrain(valServoAltimetre1, 0, VALEUR_LIMITE_ALTIMETRE1)); 
      altimetre1.write(constrain(valServoAltimetre1, 0, VALEUR_LIMITE_ALTIMETRE1));

//      valServoAltimetre2 = map(commande.toInt(), 0, 886, 0, VALEUR_LIMITE_ALTIMETRE2);
//      Serial.println(constrain(valServoAltimetre2, 0, VALEUR_LIMITE_ALTIMETRE2));
//      altimetre2.write(constrain(valServoAltimetre2, 0, VALEUR_LIMITE_ALTIMETRE2));
      
//      valServoVariometre = (commande.toInt() > 0) ? map(commande.toInt(), 0, 500, VALEUR_MIL_LIMITE_VARIOMETRE, VALEUR_SUP_LIMITE_VARIOMETRE) : map(-commande.toInt(), 500, 0, VALEUR_INF_LIMITE_VARIOMETRE, VALEUR_MIL_LIMITE_VARIOMETRE);
//      Serial.println(constrain(valServoVariometre, VALEUR_INF_LIMITE_VARIOMETRE, VALEUR_SUP_LIMITE_VARIOMETRE));
//      variometre.write(constrain(valServoVariometre, VALEUR_INF_LIMITE_VARIOMETRE, VALEUR_SUP_LIMITE_VARIOMETRE));  //insérer la plage d'entrée en m/s de Vz
      
      commande = ""; // vider la chaine de caractère
      Serial.flush(); // vider la memoire d'entrée du port série
    } else {
      commande += String(caractere); // si le caractère n'est pas \n, ajouter le caractère à la chaîne de caractère
    }
  }

}
