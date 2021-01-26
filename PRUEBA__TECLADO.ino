#include <Servo.h>


Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

char tecla;

void setup ()
{
  servo1.attach(2);
  servo2.attach(4); 
  servo3.attach(7);
  servo4.attach(8);
  servo5.attach(12);

  Serial.begin(9600);
}

void loop ()
{
  if (Serial.available())
  {
    tecla = Serial.read();
    
  }
  if (tecla=='q'||tecla=='Q')
  {
  servo1.write(180);
  servo2.write(180);
  servo3.write(180);
  servo4.write(180);
  servo5.write(180);
  Serial.print("DERECHA");
  }
  if (tecla=='w'||tecla=='W')
  {
  servo1.write(90);
  servo2.write(90);
  servo3.write(90);
  servo4.write(90);
  servo5.write(90);
  Serial.print("IZQUIERDA"); 
  }
  if (tecla=='e'||tecla=='E')
  {
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0); 
  servo5.write(0);
  Serial.print("CENTRO");
  }
  if (tecla=='t'||tecla=='T')
  {
  servo1.write(180);
  Serial.print("PULGAR_DERECHA");
  }
  if (tecla=='y'||tecla=='Y')
  {
  servo1.write(90);
  Serial.print("PULGAR_IZQUIEDA");
  }
  if (tecla=='u'||tecla=='U')
  {
  servo1.write(0);
  Serial.print("PULGAR_CENTRO");
  }
  if (tecla=='A'||tecla=='a')
  {
  servo2.write(200);
  Serial.print("INDICE/MEDIO_DERECHA");
  }
  if (tecla=='S'||tecla=='s')
  {
  servo2.write(90);
  Serial.print("INDICE/MEDIO_IZQUIEDA");
  }
  if (tecla=='d'||tecla=='D')
  {
  servo2.write(0);
  Serial.print("INDICE/MEDIO_CENTRO");
  }
  if (tecla=='g'||tecla=='G')
  {
  servo3.write(180);
  Serial.print("ANULAR_DERECHA");
  }
  if (tecla=='h'||tecla=='H')
  {
  servo3.write(90);
  Serial.print("ANULAR_IZQUIEDA");
  }
  if (tecla=='j'||tecla=='J')
  {
  servo3.write(0);
  Serial.print("ANULAR_CENTRO");
  }
  if (tecla=='z'||tecla=='Z')
  {
  servo4.write(180);
  Serial.print("DEDO_DERECHA");
  }
  if (tecla=='x'||tecla=='X')
  {
  servo4.write(90);
  Serial.print("DEDO_IZQUIEDA");
  }
  if (tecla=='c'||tecla=='C')
  {
  servo4.write(0);
  Serial.print("DEDO_CENTRO");
  }
  if (tecla=='b'||tecla=='B')
  {
  servo5.write(180);
  Serial.print("PULGAR_DERECHA");
  }
  if (tecla=='n'||tecla=='N')
  {
  servo5.write(90);
  Serial.print("PULGAR_IZQUIEDA");
  }
  if (tecla=='m'||tecla=='M')
  {
  servo5.write(0);
  Serial.print("PULGAR_CENTRO");
  }
  else if (tecla=='P'||tecla=='p')
  {
  servo1.write(180);
  servo3.write(180);
  servo4.write(180);
  servo5.write(180);
  Serial.print("4 DEDOS");
  }
}
