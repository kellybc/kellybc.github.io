// defining sketch variables
// analogPin - declares which analog pin to use
// pt - declares variable to store previous time
// reading - declares variable for analogRead
// preading - declares variable for prevous reading value
// no_snap - declares varaible for determining if someone snapped or not
int analogPin=1;
long pt=0;
float reading, preading=0;
boolean no_snap=true;

void setup(){
  // initialize serial communications
  Serial.begin(9600);

  // set analog reference voltage to 1.1V
  analogReference(INTERNAL);

  // set a random speed - see https://www.arduino.cc/reference/en/language/functions/random-numbers/randomseed/ for more details
  randomSeed(analogRead(0));
}

void loop(){
  // display message to signal begin
  Serial.println("Are you ready to snap?");
  delay(3000);
  Serial.print("Ready!  ...  ");
  delay(3000);
  Serial.print("Set!  ...  ");
  delay(random(0, 10000));
  Serial.println("Go!!!");
  
  // record the starting time
  pt=millis();
  
  // while the elapse time is less than 10 seconds
  while((millis()-pt)<10000){
    
    // set reading to zero to begin average
    reading=0;
  
    // sum 50 readings
    for(int i=0; i<50; i++){
      reading+=analogRead(analogPin);
    }
  
    // divide by 50 to get average of 50 readings
    reading/=50;

    // if there is an increase of more than 100
    if((reading-preading)>100){

      // display reaction time
      Serial.print("Your reaction time is ");
      Serial.print(millis()-pt);
      Serial.println("ms.");

      // set no_snap to false to signal that a snap occurred
      no_snap=false;

      // exit while loop
      break;
    }
    
    // set previous reading to current reading
    preading=reading;
  }

  // if no snap occurred
  if(no_snap){
    // Display you're too slow
    Serial.println("You took too long. Try again.");
  }

  // waite 3 seconds
  delay(3000);

  // set no_snap to true
  no_snap=true;

  // create blank line
  Serial.println("");
}

