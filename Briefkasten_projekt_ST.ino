#include <SoftwareSerial.h>
#include "DumbServer.h"
#define echopin 12
#define triggerpin 13
#define speedfactor 29.41/2 //halbierte Zeit die eine Microsekunde für einen Centimierter braucht
float postkastenlaenge = 6.1; //Muss je nach Modell angepasst werden, kann mit einem Programm berechnet werden
const byte BUTTON = 7; //unser Button pin


SoftwareSerial esp_serial(3, 2);
EspServer esp_server;


void setup()
{
  Serial.begin(9600);
  esp_serial.begin(9600); 


  esp_server.begin(&esp_serial, "iPhone von Leonie", "briefkasten", 30303); // ins netzwerk einloggen




  pinMode(4, OUTPUT); // Pins für WiFi Shield
  pinMode(5, INPUT_PULLUP);

  pinMode(triggerpin, OUTPUT); 
  pinMode(echopin, INPUT);

  pinMode(BUTTON, INPUT_PULLUP); //Interner Widerstand hinzufügen durch Pullup

}
int measure() { //Messung als Funktion, abhängig vom Trigger- & Echopin 
  int duration = 0;// duration wird immer wieder zu Beginn auf 0 gesetzt

  //sending start condition
  digitalWrite(triggerpin, HIGH); //Triggerpin sendet ein Signal für 10 mircosekunden
  delayMicroseconds(10);
  digitalWrite(triggerpin, LOW);

  duration = pulseIn(echopin, HIGH, 10000); // (10ms) timeout//Zeitspanne Die das Signal bzw das Echo für den Weg vom Triggerpin zum Objekt und dann zum Echopin benötigt

  return duration;
}
void loop() {
  if ( digitalRead(BUTTON) == LOW) // im Falle dass der Button gedrückt ist, durch die verschlossene Tür

  {
    if ((measure() / speedfactor) < postkastenlaenge)
      Serial.println(1);  //Abstand kleiner als der eigentliche Abstand zur Postkastenwand  -> Post ist da
    else
      Serial.println(0); //Abstand weiterhin gleichgroß -> Postkasten ist leer
     delay (100);
  }
  else//Button nicht gedrückt beim öffnen/offen sein
  {
    Serial.println(2);
  }
  delay(100);
}
