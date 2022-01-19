/* #define remplace une chaine de caractère par une autre chaine de caractère avant la compilation
    ça revient au fonctionnement d'une constante sauf que celle-ci ne prend pas de place en mémoire
    et nous permet de modifier facilement le port sur lequel est branché un composant
*/
#define PORT_SERVO_ANEMOMETRE 3
#define PORT_SERVO_ALTIMETRE1 5
#define PORT_SERVO_ALTIMETRE2 6
#define PORT_SERVO_VARIOMETRE 9
// les ports sur lesquels sont branchés les servomoteurs doivent être compatibles PWM (avoir une ~ à coté du numéro de port)

#define PORT_POT_MANCHE_AXE_X A0
#define PORT_POT_MANCHE_AXE_Y A1
#define PORT_POT_AEROFREIN A2
#define PORT_POT_PALONNIER A3
// les ports sur lesquels sont branchés les potentiomètre doivent être des ports analogiques


#include <Servo.h>
// importe la bibliothèque qui commande les servomoteurs

Servo anemometre;
Servo altimetre1;
Servo altimetre2;
Servo variometre;
// définie trois fonctions qui utiliseront la bibliothèque Servo

int valMancheAxeX;
int valMancheAxeY;
int valPotAerofrein;
int valPotPalonnier;
// déclare les variables pour les potentiomètres (valeur entre 0 et 1023)


byte valServoAnemometre = 0;
byte valServoAltimetre1 = 0;
byte valServoAltimetre2 = 0;
byte valServoVariometre = 0;
// déclare les variables pour les servomoteurs (valeur entre 0 et 255)

String commande = "";
//déclare la variable qui contiendra temporairement la commande reçue de Python


// fonction setup ne s'exécutent qu'une seule fois au démarrage
void setup() {
  Serial.begin(9600);
  // démarre la connexion série avec Python

  anemometre.attach(PORT_SERVO_ANEMOMETRE);
  altimetre1.attach(PORT_SERVO_ALTIMETRE1);
  altimetre2.attach(PORT_SERVO_ALTIMETRE2);
  variometre.attach(PORT_SERVO_VARIOMETRE);
  // définit les ports reliés aux servomoteurs
}

// fonction qui actualise la valeur des entrées (potentiomètres)
void inputData() {
  valMancheAxeX = map (analogRead(PORT_POT_MANCHE_AXE_X), 0, 130, -100, 100);
  valMancheAxeY = map (analogRead(PORT_POT_MANCHE_AXE_Y), 123, 289, -100, 100);
  valPotAerofrein = map (analogRead(PORT_POT_AEROFREIN), 0, 1023, 0, 100);
  valPotPalonnier = map (analogRead(PORT_POT_PALONNIER), 0, 1023, -100, 100);
  // récupère la position des potentiomètres, après les avoir traduient en valeur de -100 à 100
}

// fonction qui gère la communication entrante avec Python
void comSerialSimu() {

  if (Serial.available() > 0) {
    // check si un message arrive sur le port série

    char caractere = Serial.read();
    // stocke le caractère reçue

    if (caractere == 10) { // si le caractère est \n (retour à la ligne: 10 en valeur ASCII), le suffixe,  rechercher à quoi correspond le préfixe
      if (commande.substring(0, 3) == "ANE") { // si le préfixe correspond à "ANE" (anémomètre)
        valServoAnemometre = commande.substring(3).toInt(); // stocker la variable correspondant à l'anémomètre, après l'avoir convertie d'ASCII à entier
      } else if (commande.substring(0, 3) == "ALT") { // (altimètre)
        valServoAltimetre1 = commande.substring(3).toInt();
        valServoAltimetre2 = commande.substring((commande.length()) - 3).toInt(); // ne prend en compte que les 3 derniers chiffres du nombre réprésentant l'altitude
      } else if (commande.substring(0, 3) == "VAR") { // (variomètre)
        valServoVariometre = commande.substring(3).toInt();
      } else if (commande.substring(0, 3) == "REL") { // (reload)
        exportDataSimu(); // éxecuter la fonction exportDataSimu()
      }
      commande = ""; // vider la chaine de caractère
      Serial.flush(); // vider la memoire d'entrée du port série
    } else {
      commande += String(caractere); // si le caractère n'est pas \n, ajouter le caractère à la chaîne de caractère
    }
  }
}

// fonction qui gère la communication sortante avec Python
void exportDataSimu() {
  Serial.print("MAX"); // envoie la chaine de caractère préfixe "MAX" (fonction print)
  Serial.println(valMancheAxeX); // suivie de la variable correspondante et du suffixe "\r\n" (fonction println)
  Serial.print("MAY");
  Serial.println(valMancheAxeY);
  Serial.print("PAL");
  Serial.println(valPotPalonnier);
  Serial.print("AER");
  Serial.println(valPotAerofrein);
}

// fonction qui actualise les sorties (servomoteurs)
void outputData() {
  anemometre.write(map(valServoAnemometre, 0, 0, 0, 180));  //insérer la plage d'entrée en m/s de Vy
  altimetre1.write(map(valServoAltimetre1, 0, 0, 0, 180));  //insérer la plage d'entrée en m de z
  altimetre2.write(map(valServoAltimetre2, 0, 999, 0, 180));  
  variometre.write(map(valServoVariometre, 0, 0, 0, 180));  //insérer la plage d'entrée en m/s de Vz
  // écrit la position des servomoteurs
}

// fonction loop exécutent en boucle (While True) après le setup
void loop() {
  inputData();
  comSerialSimu();
  outputData();
}
