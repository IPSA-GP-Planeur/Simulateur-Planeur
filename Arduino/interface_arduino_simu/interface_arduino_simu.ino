/* #define remplace une chaine de caractère par une autre chaine de caractère avant la compilation
    ça revient au fonctionnement d'une constante sauf que celle-ci ne prend pas de place en mémoire
    et nous permet de modifier facilement le port sur lequel est branché un composant
*/
#define PORT_SERVO_ANEMOMETRE 6
#define PORT_SERVO_ALTIMETRE1 3
#define PORT_SERVO_ALTIMETRE2 5
#define PORT_SERVO_VARIOMETRE 9
// les ports sur lesquels sont branchés les servomoteurs doivent être compatibles PWM (avoir une ~ à coté du numéro de port)

#define PORT_POT_MANCHE_AXE_X A0
#define PORT_POT_MANCHE_AXE_Y A1
#define PORT_POT_AEROFREIN A2
#define PORT_POT_PALONNIER A3
// les ports sur lesquels sont branchés les potentiomètre doivent être des ports analogiques

#define PORT_SWITCH_START_STOP 11
#define PORT_SWITCH_PAUSE 12
// les ports sur lesquels sont branchés les interrupteurs (switchs)

#define VALEUR_LIMITE_ANEMOMETRE 178
#define VALEUR_LIMITE_ALTIMETRE1 179
#define VALEUR_LIMITE_ALTIMETRE2 179
#define VALEUR_INF_LIMITE_VARIOMETRE 12
#define VALEUR_MIL_LIMITE_VARIOMETRE 92
#define VALEUR_SUP_LIMITE_VARIOMETRE 177
// les valeurs limites atteintes par les servomoteurs (en m/s et m)


#include <Servo.h>
// importe la bibliothèque qui commande les servomoteurs

Servo anemometre;
Servo altimetre1;
Servo altimetre2;
Servo variometre;
// définie trois fonctions qui utiliseront la bibliothèque Servo

int valServoAnemometre = 0;
int valServoAltimetre1 = 0;
int valServoAltimetre2 = 0;
int valServoVariometre = 0;
// déclare les variables pour les servomoteurs (valeur entre 0 et 255)

int valMancheAxeX;
int valMancheAxeY;
int valPotAerofrein;
int valPotPalonnier;
// déclare les variables pour les potentiomètres (valeur entre 0 et 1023)

bool valSwitchStartStop;
bool valSwitchPause;
// déclare les variables pour les interrupteurs (valeur 0 ou 1)
// la position par défaut des interrupteurs (cache fermé) donne 1

String commande = "";
//déclare la variable qui contiendra temporairement la commande reçue de Python


// fonction setup ne s'exécutent qu'une seule fois au démarrage
void setup() {
  Serial.begin(57600);
  // démarre la connexion série avec Python

  anemometre.attach(PORT_SERVO_ANEMOMETRE);
  altimetre1.attach(PORT_SERVO_ALTIMETRE1);
  altimetre2.attach(PORT_SERVO_ALTIMETRE2);
  variometre.attach(PORT_SERVO_VARIOMETRE);
  // définit les ports reliés aux servomoteurs

  pinMode(PORT_SWITCH_START_STOP, INPUT_PULLUP);
  pinMode(PORT_SWITCH_PAUSE, INPUT_PULLUP);
}

// fonction qui actualise la valeur des entrées (potentiomètres)
void inputData() {
  valMancheAxeX = map (analogRead(PORT_POT_MANCHE_AXE_X), 237, 388, -100, 100);
  valMancheAxeY = map (analogRead(PORT_POT_MANCHE_AXE_Y), 89, 289, -100, 100);
  valPotAerofrein = map (analogRead(PORT_POT_AEROFREIN), 0, 1023, 0, 100);
  valPotPalonnier = map (analogRead(PORT_POT_PALONNIER), 0, 1023, -100, 100);
  // récupère la position des potentiomètres, après les avoir traduient en valeur de -100 à 100

  valSwitchStartStop = !digitalRead(PORT_SWITCH_START_STOP);
  valSwitchPause = !digitalRead(PORT_SWITCH_PAUSE);
  //récupère la position des interrupteurs
}

// fonction qui gère la communication entrante avec Python
void comSerialSimu() {

  if (Serial.available() > 0) {
    // check si un message arrive sur le port série

    char caractere = Serial.read();
    // stocke le caractère reçue

    if (caractere == '\n') { // si le caractère est \n (retour à la ligne: 10 en valeur ASCII), le suffixe,  rechercher à quoi correspond le préfixe
      if (commande.substring(0, 3) == "ANE") { // si le préfixe correspond à "ANE" (anémomètre)
        valServoAnemometre = commande.substring(3).toInt(); // stocker la variable correspondant à l'anémomètre, après l'avoir convertie d'ASCII à entier
        outputAnemometre();
      } else if (commande.substring(0, 3) == "ALT") { // (altimètre)
        valServoAltimetre1 = commande.substring(3).toInt();
        valServoAltimetre2 = commande.substring((commande.length()) - 3).toInt(); // ne prend en compte que les 3 derniers chiffres du nombre réprésentant l'altitude
        outputAltimetre();
      } else if (commande.substring(0, 3) == "VAR") { // (variomètre)
        valServoVariometre = commande.substring(3).toInt();
        outputVariometre();
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
  Serial.print("STA");
  Serial.println(valSwitchStartStop);
  Serial.print("PAU");
  Serial.println(valSwitchPause);
}

// fonctions qui actualise les sorties (servomoteurs)

void outputAnemometre() {
  valServoAnemometre = map(constrain(valServoAnemometre, 20, 240), 20, 240, 0, VALEUR_LIMITE_ANEMOMETRE);  //insérer la plage d'entrée en m/s de Vy et prendre en compte la limite des servomoteurs
  anemometre.write(valServoAnemometre);
}

void outputAltimetre() {
  valServoAltimetre1 = map(valServoAltimetre1, 0, 9132, 0, VALEUR_LIMITE_ALTIMETRE1);  //insérer la plage d'entrée en m de z et prendre en compte la limite des servomoteurs
  altimetre1.write(constrain(valServoAltimetre1, 0, VALEUR_LIMITE_ALTIMETRE1));
  valServoAltimetre2 = map(valServoAltimetre2, 0, 886, 0, VALEUR_LIMITE_ALTIMETRE2);
  altimetre2.write(constrain(valServoAltimetre2, 0, VALEUR_LIMITE_ALTIMETRE2));
}

void outputVariometre() {
  valServoVariometre = (valServoVariometre > 0) ? map(valServoVariometre, 0, 500, VALEUR_MIL_LIMITE_VARIOMETRE, VALEUR_SUP_LIMITE_VARIOMETRE) : map(-valServoVariometre, 500, 0, VALEUR_INF_LIMITE_VARIOMETRE, VALEUR_MIL_LIMITE_VARIOMETRE);
  variometre.write(constrain(valServoVariometre, VALEUR_INF_LIMITE_VARIOMETRE, VALEUR_SUP_LIMITE_VARIOMETRE));  //insérer la plage d'entrée en cm/s de Vz
  // écrit la position des servomoteurs
}

// fonction loop exécutent en boucle (While True) après le setup
void loop() {
  inputData();
  comSerialSimu();
}
