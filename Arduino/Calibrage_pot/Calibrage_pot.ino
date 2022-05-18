#define PORT_POT A3

void setup() {
  Serial.begin(9600);
  
}

void loop() {
  Serial.println(analogRead(PORT_POT));
  delay(500);
}
