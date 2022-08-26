#include <SPI.h>
#include <SD.h>

const int CS1=8;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    delay(1);         // wait for serial port to connect. Needed for native USB port only
  }

  Serial.print("Initializing SD card...");

  if (!SD.begin(CS1)) {
    Serial.println("initialization failed!");
    while (1);  // do nothing indefinitely
  }
  Serial.println("initialization done.");

  // Open the file for reading
  File myFile = SD.open("data.txt");
  if (myFile) {
    Serial.print("data.txt: ");

    // read from the file until there's nothing else in it
    while (myFile.available()) {
      Serial.write(myFile.read());
    }
    // close the file
    myFile.close();
  } else {
    // if the file didn't open, print an error
    Serial.println("error opening data.txt");
  }
}

void loop() {}
