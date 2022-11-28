void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
}
int light = 0;
void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(52) == 1) {
    Serial.print("button-");
    Serial.println(light);
    while(digitalRead(52) == 1){
      //
    }
    light++;
  }
  else {
    Serial.println(map(analogRead(A0), 0, 1023, 0, 900));
  }


}
