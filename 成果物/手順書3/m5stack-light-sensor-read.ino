const int lightPin = 36;

void setup() {
  Serial.begin(115200);
  delay(1000);
}

void loop() {
  int value = analogRead(lightPin);
  Serial.println(value);
  delay(100);
}
