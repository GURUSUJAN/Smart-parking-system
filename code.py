const int buzzer = 8;

int echopin = 6;
int trigpin = 7;
int red=10;
int green=3;
int yellow=4;
int mesafe;
int sure;


void setup()
{
  Serial.begin(9600); 
 
  pinMode(buzzer, OUTPUT);
  pinMode(trigpin, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(echopin, INPUT);
}

void loop()
{
 digitalWrite(trigpin,LOW);
 delayMicroseconds(2);
 digitalWrite(trigpin,HIGH);
 delayMicroseconds(10);
 digitalWrite(trigpin,LOW);
 sure = pulseIn(echopin,HIGH);
 mesafe = (sure/2)/29.0;
  
 if(mesafe <= 100)
 {
  digitalWrite(red,HIGH);
  delay(20);
  digitalWrite(red,0);
  delay(20);
  digitalWrite(buzzer,HIGH);
  delay(250);
  digitalWrite(buzzer,LOW);
  delay(125);
 }
 else if(mesafe <= 150)
 {
  digitalWrite(yellow,HIGH);
  delay(20);
  digitalWrite(yellow,0);
  delay(20);
  digitalWrite(buzzer,HIGH);
  delay(500);
  digitalWrite(buzzer,LOW);
  delay(250);
 }
 else if(mesafe <= 200)
 {
  digitalWrite(green,HIGH);
  delay(20);
  digitalWrite(green,0);
  delay(20);
  digitalWrite(buzzer,HIGH);
  delay(1000); 
  digitalWrite(buzzer,LOW);
  delay(1000);  
 }
 else
 {
  digitalWrite(green,HIGH);
  digitalWrite(buzzer,LOW);
 }
  Serial.print("uzaklik = ");
  Serial.print(mesafe);
  Serial.println("cm");
  delay(500);
}
