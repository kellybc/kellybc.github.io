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

  // see if the card is present and can be initialized:
  if (!SD.begin(CS1)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    while (1);  // loop indefinitely
  }
  Serial.println("card initialized.");

  File dataFile = SD.open("myFile.txt", FILE_WRITE);

  String dataString="All your base are belong to us";

  // if the file is available, write to it:
  if (dataFile) {
    dataFile.println(dataString);
    dataFile.close();
    // print to the serial port too:
    Serial.println(dataString);
  }
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening myFile.txt");
  }

}

void loop() {}
