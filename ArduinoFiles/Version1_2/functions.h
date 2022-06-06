/*
Functions.h 

This has functionsused in the main ino file. 

*/
//#include "arduino.h"
// Functions

int str_to_int(char *P);
void give_speed();
void stop();
void encoder1A();

// externs
extern unsigned long encoder1a;
extern unsigned long encoder2a;
extern bool m1,m2,fm;
extern int nums[10];
extern int nums2[10];

void fools(void)
{
  digitalWrite(12, HIGH);
  digitalWrite(13, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, HIGH);
  fm = 1;
}

void stop()
{
    m1 = 0;
    m2 = 0;
    fm = 0;
    digitalWrite(12, LOW);
    digitalWrite(8, LOW);
    digitalWrite(9, LOW);
    digitalWrite(13, LOW);     
}

void give_speed(char M , int speed, bool direction)
{
//  Serial.println(M);
  if (M == 1)
  {
    m1 = 1;
    if (direction)
    {
      digitalWrite(12, LOW);
      digitalWrite(13, HIGH);
    }
    else
    {
      digitalWrite(12, HIGH);
      digitalWrite(13, LOW);
    }
  }
  if (M == 2)
  {
    m2=1; 
    if (direction)
    {
      digitalWrite(7, HIGH);
      digitalWrite(8, LOW);
    }
    else
    {
      digitalWrite(7, LOW);
      digitalWrite(8, HIGH);
    }
  } 
}

unsigned long pastt = 0;
int timee = 0;
int _eye = 0;
int _eye2 = 0;
unsigned long pastt2 = 0;
int timee2 = 0;

void encoder1A()
{
    unsigned long noww;
    // detachInterrupt(digitalPinToInterrupt(2));
    encoder1a++;
    noww = micros();
    timee = abs(noww - pastt);
    pastt = noww;
    // Serial.println("Here 1");
    nums[_eye] = (timee);
    _eye++;
    if(_eye>=10)
      _eye = 0;
  // attachInterrupt(digitalPinToInterrupt(2), encoder1A, RISING);
    
}
void encoder2A()
{
    unsigned long noww2;
    encoder2a++;
     noww2 = micros();
    timee2 = abs(noww2 - pastt2);
    pastt2 = noww2;
    // Serial.println("Here Bitxhes");
    nums2[_eye2] = (timee2);
    _eye2++;
    if(_eye2>=10)
      _eye2 = 0;
}
