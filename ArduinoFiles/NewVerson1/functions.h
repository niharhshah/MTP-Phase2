/*
Functions.h 

This has functionsused in the main ino file. 

*/
#include "arduino.h"
// Functions

int str_to_int(char *P);
void give_speed();
void stop();
void encoder1A();

// externs
extern long long encoder1a;
extern long long encoder2a;
extern bool m1,m2;
extern int nums[10];
extern int nums2[10];
extern float cps;


void stop()
{
    m1 = 0;
    m2 = 0;
    for(int pee = 0 ; pee < 10 ; pee++)
      nums[pee] = 0;
}

void give_speed(char M , int speed, bool direction)
{
  Serial.println(M);
  if (M == 1)
  {
    m1 = 1;
    if (direction)
    {
      digitalWrite(12, HIGH);
      digitalWrite(13, LOW);
    }
    else
    {
      digitalWrite(13, LOW);
      digitalWrite(12, HIGH);
    }
  }
  if (M == 2)
  {
    m2=1; 
    if (direction)
    {
      digitalWrite(9, HIGH);
      digitalWrite(8, LOW);
    }
    else
    {
      digitalWrite(9, LOW);
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
    // Serial.println(timee);
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
    timee2 = abs(noww2 - pastt);
    pastt2 = noww2;
    // Serial.println(timee);
    nums2[_eye2] = (timee);
    _eye2++;
    if(_eye2>=10)
      _eye2 = 0;
}