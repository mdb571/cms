const int in=8,out=9;
int temp=0;
boolean prev_state=true;

void setup() {
Serial.begin(9600);
pinMode(in,INPUT);
pinMode(out,INPUT);


}

void loop() {
if(!digitalRead(in)&& prev_state)
  { 
    temp++;
    Serial.print(temp);
    delay(1000);
  }
else if(!digitalRead(out)&& prev_state)
  { 
    --temp;
    Serial.print(temp);
    delay(200);
  }
 if (digitalRead(in)){
 prev_state=true;
  delay(200);
 }
else if (digitalRead(out)){
 prev_state=true;
  delay(200);
 }
}
