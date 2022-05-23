#include "functions.h"
/* ---------------------------------------
  USe of this INO file

  Pin 10 M1 PWM
  Pin 11 M2 PWM
  Pin 12,13 M1 Direction
  Pin  9,8  M2 Direction
  Pin  7,6  M2 Encoder
  Pin  5,4  M1 Encoder

  Commands
  MNxxx N'th Motor speed N=<1,2>

  ----------------------------------------*/
char m1a = 2;
char m2a = 3;
char m1p = 11;
char m2p = 10;
float cps1 = 0.0;

bool m1 = 0;
bool m2 = 0;

long long encoder1a = 0;
long long encoder2a = 0;

bool default_dir = 0;
int defaultSpeed = 2000; //Give Speed in cps1
int timer1_counter;
int nums[10];
int nums2[10];

//PID related
double e_speed = 0; 
double e_speed_pre = 0;  //last error of speed
double e_speed_sum = 0;  //sum error of speed
double pwm_pulse = 0;     //this value is 0~255

double e_speed2 = 0; 
double e_speed_pre2 = 0;  //last error of speed
double e_speed_sum2 = 0;  //sum error of speed
double pwm_pulse2 = 0;     //this value is 0~255

double kp_1 = 0.11;
double ki_1 = 0.08;
double kd_1 = 0.01;

double kp_2 = 0.11;
double ki_2 = 0.08;
double kd_2 = 0.01;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  // Motor Pin Map
  pinMode(m1p, OUTPUT); // M1 Power
  pinMode(m2p, OUTPUT); // M2 Power
  pinMode(12, OUTPUT); // M1 Direction
  pinMode(13, OUTPUT); // M1 Direction
  pinMode(9, OUTPUT) ; // M2 Direction
  pinMode(8, OUTPUT) ; // M2 Direction

  //Encoder
  pinMode(7, INPUT_PULLUP); // M2 encoder A
  pinMode(m2a, INPUT_PULLUP); // M2 encoder B
  pinMode(m1a, INPUT_PULLUP); // M1 encoder A
  pinMode(4, INPUT_PULLUP); // M1 encoder B
  attachInterrupt(digitalPinToInterrupt(m1a), encoder1A, RISING);
  attachInterrupt(digitalPinToInterrupt(m2a), encoder1A, RISING);
  
  noInterrupts();           // disable all interrupts
  TCCR1A = 0;
  TCCR1B = 0;
  timer1_counter = 59286;   // preload timer 65536-16MHz/256/2Hz (34286 for 0.5sec) (59286 for 0.1sec)

  
  TCNT1 = timer1_counter;   // preload timer
  TCCR1B |= (1 << CS12);    // 256 prescaler 
  TIMSK1 |= (1 << TOIE1);   // enable timer overflow interrupt
  interrupts();     

}
char q;
void loop() {

    // Serial.println(cps1);
    while (Serial.available() > 0)
    {
      q = Serial.read();
      // Serial.print(q);
      // Serial.print("\t");
      // Serial.println(m1);
      if (q == 49)
      {
        // Serial.println("I am in give speed");
        give_speed(1,defaultSpeed,default_dir);
        give_speed(2,defaultSpeed,default_dir);
        // analogWrite(11,128);
      }
      if(q == '2')
        stop();
      if(q == '3')
        defaultSpeed += 500;
      if(q == '4')
        defaultSpeed -= 500;
      if(q == '5')
        Serial.println(kp_1);
      

    }
}

// ISR

ISR(TIMER1_OVF_vect)        // interrupt service routine - tick every 0.1sec
{
  char p = 0;
  float sum = 0.0; 
  TCNT1 = timer1_counter;   // set timer
  sum = 0;
  for (p = 0;p<10;p++)
    sum += nums[p];
  sum = sum/10;
  if (sum != 0)
    cps1 = 1000000/sum;  
  else
    cps1 = 0;
  // if(m1)
  //   analogWrite(m2p,40);
  // else
  //   analogWrite(m2p,0);
    if (m1){
    e_speed = defaultSpeed - cps1;
    pwm_pulse = e_speed*kp_1 + e_speed_sum*ki_1 + (e_speed - e_speed_pre)*kd_1;
    e_speed_pre = e_speed;  //save last (previous) error
    e_speed_sum += e_speed; //sum of error
    if (e_speed_sum >4000) e_speed_sum = 4000;
    if (e_speed_sum <-4000) e_speed_sum = -4000;
  }
  else{
    e_speed = 0;
    e_speed_pre = 0;
    e_speed_sum = 0;
    pwm_pulse = 0;
  }
  
  if (m2){
    e_speed2 = defaultSpeed - cps1;
    pwm_pulse2 = e_speed2*kp_2 + e_speed_sum2*ki_2 + (e_speed2 - e_speed_pre2)*kd_2;
    e_speed_pre2 = e_speed2;  //save last (previous) error
    e_speed_sum2 += e_speed2; //sum of error
    if (e_speed_sum2 >4000) e_speed_sum2 = 4000;
    if (e_speed_sum2 <-4000) e_speed_sum2 = -4000;
  }
  else{
    e_speed2 = 0;
    e_speed_pre2 = 0;
    e_speed_sum2 = 0;
    pwm_pulse2 = 0;
  }
  
  //update new speed
  Serial.print(e_speed2);
  Serial.print("\t");
  // Serial.print(pwm_pulse);
  // Serial.print("\t");
  Serial.println(cps1);

 // Motor 2
  if (pwm_pulse2 <255 & pwm_pulse2 >0){
    analogWrite(m2p,pwm_pulse2);  //set motor speed  
  }
  else{
    if (pwm_pulse2>255)
      analogWrite(m2p,255);
    else
      analogWrite(m2p,0);
  }
  
  //Motor 1
  if (pwm_pulse <255 & pwm_pulse >0){
    analogWrite(m1p,pwm_pulse);  //set motor speed  
  }
  else{
    if (pwm_pulse>255)
      analogWrite(m1p,255);
    else
      analogWrite(m1p,0);
  }
  
}

