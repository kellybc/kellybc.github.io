// include the SD library so that the Arduino will be able to talk to the 
// microSD card
#include <SD.h>

// set which pin is the chip select for SPI. For Sparkfun microSD shield it is
// PIN 8.
const int chipSelect=8;

// create variable to save the state of the switch. 0 for off and 1 for on.
int switchState=0;

// create variable to save whether the card initialized or not (i.e. whether
// the Arduino was able to find and talk with a card or not)
boolean cardInitialized=false;

// create an empty filename to be written later
String filename="";
void setup() {
  
  // set switch pin to input
  pinMode(7, INPUT);
  
  // begin the serial interface
  Serial.begin(9600);
  
  // let the user know that it is about to try to talk with the card
  Serial.print("Initializing SD card ... ");
  
  // if the card is not wanting to talk
  if(!SD.begin(chipSelect)){
    
    // let user know that the card is not want to talk
    Serial.println("Card failed, or not present.");
  
  // if the card is talking
  } else {
    
    // let user know the card is talking
    Serial.println("Card initialized.");
    
    // save that the card initialized (or is talking)
    cardInitialized=true;
  }
}
void loop(){
  
  // if the card is talking
  if(cardInitialized){
    
    // read the state of the switch pin (i.e. pin 7)
    switchState=digitalRead(7);
    
    // if the switch is on
    if(switchState==HIGH){
      
      // let user know the Arduino is about to collect data
      Serial.print("Collecting data for file ");
      
      // declare empty string to save data in
      String dataString="";
      
      // CHANGES BEGIN HERE
      // | | | | | | | | |
      // | | | | | | | | |
      // V V V V V V V V V
      
      // for analog pins 0, 1, and 2
      for(int analogPin=0; analogPin<3; analogPin++){
        
        // get analog pin value
        int sensor=analogRead(analogPin);
        
        // add the analog pin value to data string to be saved on card
        dataString+=String(sensor);
        
        // add commas to seperate analog pin values
        if(analogPin<2){
          dataString+=",";
        }
      }
      
      // ^ ^ ^ ^ ^ ^ ^ ^ ^
      // | | | | | | | | |
      // | | | | | | | | |
      // CHANGES END HERE
      
      // if the filename is empty
      if(filename==""){
        
        // get the next filename
        filename=getFilename();
      }
      
      // let user know what file will be used
      Serial.println(filename);
      
      // open the file to write data
      File dataFile=SD.open(filename, FILE_WRITE);
      
      // if file opened properly
      if(dataFile){
        
        // let user know data is about to be written to file
        Serial.println("Writing data "+dataString+" to "+filename+".");
        
        // write data to file
        dataFile.println(dataString);
        
        // close file
        dataFile.close();
      
      // if file did not open properly
      } else {
        
        // let user know file did not open and data was not saved
        Serial.println("Error opening "+filename+". Could not write data.");
      }
    
    // if switch is off
    } else {
      
      // clear filename
      filename="";
    }
  }
  
  // wait 5 seconds
  delay(5000);
}

// Function that gets the next sequential filename.
// Filenames the function checks for appear as DATAXXX.TXT where
// XXX are sequentially number. The function returns a String.
String getFilename(){
  
  // open the root directory of the card
  File dir=SD.open("/");
  
  // reset where the current file index is looking
  dir.rewindDirectory();
  
  // set the initial index to 0
  int dataFileIndex=0;
  
  // declare empty string for the return variable
  String dataFileIndexString;
  
  // loop indefinitely
  while (true){
    
    // open the next available file in root directory
    File entry=dir.openNextFile();
    
    // if the entry is not available, we have reached the end of files
    if(!entry){
      
      // break or stop the indefinite while loop
      break;
    }
    
    // get the name of the entry
    String entryName=entry.name();
    
    // if the name of the file starts with DATA and ends with .TXT
    if(entryName.substring(0,4)=="DATA" && entryName.substring(7)==".TXT"){
      
      // if the number associated with the DATAXXX.TXT file is greater than
      // or equal to the current data file index
      if(dataFileIndex<=entryName.substring(4,7).toInt()){
        
        // set data file index to one higher
        dataFileIndex=entryName.substring(4,7).toInt()+1;
      }
    }
    
    // close the entry
    entry.close();
  }
  
  // if the data file index is less than 10
  if(dataFileIndex<10){
    
    // pad two 0s onto the front of the index string
    dataFileIndexString="00"+String(dataFileIndex);
  
  // if the data file index is less than 100
  } else if(dataFileIndex<100){
    
    // pad one 0 onto the front of the index string
    dataFileIndexString="0"+String(dataFileIndex);
  
  // if the data file index is greater than or equal to 100
  } else {
    
    // create string for data file index
    dataFileIndexString=String(dataFileIndex);
  }
  
  // return the data filename
  return "DATA"+dataFileIndexString+".TXT";
}
