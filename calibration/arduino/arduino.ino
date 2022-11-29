#include <FastLED.h>
#define NUM_LEDS 100
#define DATA_PIN 5
CRGB leds[NUM_LEDS];

void setup() {
  Serial.begin(9600);
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);  // GRB ordering is assumed
  leds[0] = CRGB::Blue;
  FastLED.show();
}
int light = 0;
void loop() {
  
  delay(50);
  if (digitalRead(52) == 1) {
    Serial.print("button-");
    Serial.println(light);
    while(digitalRead(52) == 1){
      //
    }
    light++;
    leds[light-1] = CRGB::Black;
    leds[light] = CRGB::Blue;
    FastLED.show();
  }
  else {
    Serial.println(map(analogRead(A0), 0, 1023, 0, 900));
  }


}
