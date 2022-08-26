void setup(){
  Serial.begin(9600);
}

void loop(){

  Serial.print("In Decimal: ");
  Serial.write(72);            // send H character in decimal
  Serial.write(69);            // send E character in decimal
  Serial.write(76);            // send L character in decimal
  Serial.write(76);            // send L character in decimal
  Serial.write(79);            // send O character in decimal
  Serial.write(10);            // send newline character in decimal
  delay(200);                  // wait 200 ms

  Serial.print("In Hexadecimal: ");
  Serial.write(0x48);          // send H character in hexadecimal
  Serial.write(0x45);          // send E character in hexadecimal
  Serial.write(0x4C);          // send L character in hexadecimal
  Serial.write(0x4C);          // send L character in hexadecimal
  Serial.write(0x4F);          // send O character in hexadecimal
  Serial.write(0x0A);          // send newline character in hexadecimal
  delay(200);                  // wait 200 ms

  Serial.print("In Binary: ");
  Serial.write(B01001000);     // send H character in binary
  Serial.write(B01000101);     // send E character in binary
  Serial.write(B01001100);     // send L character in binary
  Serial.write(B01001100);     // send L character in binary
  Serial.write(B01001111);     // send O character in binary
  Serial.write(B00001010);     // send newline character in binary
  delay(200);                  // wait 200 ms

  Serial.println();
}
