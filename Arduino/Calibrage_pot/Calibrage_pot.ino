#define PORT_POT_MANCHE_AXE_X A0
#define PORT_POT_MANCHE_AXE_Y A1
#define PORT_POT_AEROFREIN A2
#define PORT_POT_PALONNIER A3

int valMancheAxeX;
int valMancheAxeY;
int valPotAerofrein;
int valPotPalonnier;
// déclare les variables pour les potentiomètres (valeur entre 0 et 1023)


void setup() {
  Serial.begin(9600);
}

void loop() {

  valMancheAxeX = analogRead(PORT_POT_MANCHE_AXE_X);
  valMancheAxeY = analogRead(PORT_POT_MANCHE_AXE_Y);
  valPotAerofrein = analogRead(PORT_POT_AEROFREIN);
  valPotPalonnier = analogRead(PORT_POT_PALONNIER);

  Serial.print("Manche axe X: ");
  Serial.println(valMancheAxeX);
  Serial.print("Manche axe Y: ");
  Serial.println(valMancheAxeY);
  Serial.print("Palonnier: ");
  Serial.println(valPotPalonnier);
  Serial.print("Aerofrein: ");
  Serial.println(valPotAerofrein);

  delay(500);
}
