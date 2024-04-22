#include "Arduino.h"

static const uint16_t c_ledcFrequency = 20000;
static const uint16_t c_ledcResolution = 12;
static const uint16_t PWM_MAX = 4095;

//upper left, upper right, lower left, lower right
static const uint16_t pwmPinForwards[4] = {16, 17, 22, 18};
static const uint16_t pwmPinBackwards[4] = {4, 2, 21, 19};

// float forceFactor = 0.0085;
// float pidFactor[6][3] = {
//   {6, 0, 600}, {6, 0, 600}, {0.5, 0, 30}, {6, 0, 600}, {6, 0, 600}, {0.5, 0, 30}
// };

int incomingByte = 0;    // for incoming serial data

int loop_round = 0;

void setup()
{
  Serial.begin(9600);    // opens serial port, sets data rate to 9600 bps

  //pinMode(40, OUTPUT);
  //delay(10);
  //digitalWrite(40, 0);

  for (int i = 0; i < 4; i++){
    pinMode(pwmPinForwards[i], OUTPUT);
    ledcSetup(i, c_ledcFrequency, c_ledcResolution);
    ledcAttachPin(pwmPinForwards[i], i);
  }

  for (int i = 0; i < 4; i++){
    pinMode(pwmPinBackwards[i], OUTPUT);
    ledcSetup(i + 4, c_ledcFrequency, c_ledcResolution);
    ledcAttachPin(pwmPinBackwards[i], i + 4);
  }

  //pinMode(pwmPinForwards[2], OUTPUT);
  //pinMode(pwmPinBackwards[0], OUTPUT);
  //ledcSetup(0, c_ledcFrequency, c_ledcResolution);
  //ledcAttachPin(pwmPinForwards[2], 0);
  //ledcAttachPin(pwmPinBackwards[0], 0);

  //pinMode(encoderIndexPin[globalIndex], INPUT);
  // pinMode(motorDirAPin[globalIndex], OUTPUT);
  // pinMode(motorDirBPin[globalIndex], OUTPUT);

  // pinMode(motorPwmPinForwards[globalIndex], OUTPUT);
  // pinMode(motorPwmPinBackwards[globalIndex], OUTPUT);

  // ledcSetup(globalIndex, c_ledcFrequency, c_ledcResolution);
  // ledcSetup(globalIndex+6, c_ledcFrequency, c_ledcResolution);

  // ledcAttachPin(motorPwmPinForwards[globalIndex], globalIndex);
  // ledcAttachPin(motorPwmPinBackwards[globalIndex], globalIndex+6);
  // ledcWrite(globalIndex, 0.1*PWM_MAX);
  
      
}

void loop()
{
  Serial.printf("%d\n", loop_round++);
  for (int i = 0; i < 4; i++){
    ledcWrite(i, 0.075*PWM_MAX);
    delay(100);
    ledcWrite(i, 0);
    ledcWrite(i+4, 0.075*PWM_MAX);
    delay(130);
    ledcWrite(i+4, 0);
    delay(1000);
  }

  // // send data only when you receive data:
  // if (Serial.available() > 0) {
  //   // read the incoming byte:
  //   incomingByte = Serial.read();
  //   // say what you got:
  //   Serial.write(incomingByte);
  // }
}