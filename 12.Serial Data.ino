void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
}

void loop() {
  // Send the time in milliseconds from when the Arduino was powered one
  Serial.print(millis());

  // Send the delimiting character. In this case, a comma
  Serial.print(',');

  // Send the analogRead value of analog pin 1 with a newline character
  Serial.println(analogRead(1));

  // Delay 100 milliseconds
  delay(100);
}
