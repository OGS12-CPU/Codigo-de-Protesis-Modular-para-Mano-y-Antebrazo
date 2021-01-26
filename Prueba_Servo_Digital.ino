 # include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3; 

int Pinservo1 = 7;
int Pinservo2 = 4;
int Pinservo3 = 2;
int pulsomin = 600;
int pulsomax = 2400;

void setup (){
  servo1.attach(Pinservo1, pulsomin, pulsomax);
  servo2.attach(Pinservo2, pulsomin, pulsomax);
  servo3.attach(Pinservo3, pulsomin, pulsomax);
} 

void loop(){
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  delay(2000);
  servo1.write(180);
  servo2.write(180);
  servo3.write(180);
  delay(2000);
}
