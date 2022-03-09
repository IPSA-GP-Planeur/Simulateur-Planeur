#define PORT_SERVO_ANEMOMETRE 3
#define PORT_SERVO_ALTIMETRE1 5
#define PORT_SERVO_ALTIMETRE2 6
#define PORT_SERVO_VARIOMETRE 9

#include <Servo.h>

Servo anemometre;
Servo altimetre1;
Servo altimetre2;
Servo variometre;

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
      anemometre.write(commande.toInt());
      altimetre1.write(commande.toInt());
      altimetre2.write(commande.toInt());  
      variometre.write(commande.toInt());
      commande = ""; // vider la chaine de caractère
      Serial.flush(); // vider la memoire d'entrée du port série
    } else {
      commande += String(caractere); // si le caractère n'est pas \n, ajouter le caractère à la chaîne de caractère
    }
  }

}
