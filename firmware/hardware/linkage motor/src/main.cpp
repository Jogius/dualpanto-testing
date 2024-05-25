#include "Arduino.h"

static const uint16_t c_ledcFrequency = 20000;
static const uint16_t c_ledcResolution = 12;
static const uint16_t PWM_MAX = 4095;


// PWM pins for the main linkage actuators
//upper left, upper right, lower left, lower right
static const uint16_t pwmPinForwards[4] = {16, 17, 22, 18};
static const uint16_t pwmPinBackwards[4] = {4, 2, 21, 19};

//Digital signal pins for endeffector motors
static const uint16_t endeffectorDirectionPin[2] = {32, 26};
//PWM pins for the endeffector motors
static const uint16_t endeffectorPWMPin[2] = {25, 23};

int loop_round = 0;

void setup()
{
  Serial.begin(9600);    // opens serial port, sets data rate to 9600 bps

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

  for (int i = 0; i < 2; i++){
    pinMode(endeffectorDirectionPin[i], OUTPUT);
    pinMode(endeffectorPWMPin[i], OUTPUT);
    ledcSetup(i + 8, c_ledcFrequency, c_ledcResolution);
    ledcAttachPin(endeffectorPWMPin[i], i + 8);
  }
}

void loop()
{
  Serial.printf("%d\n", loop_round++);
  for (int i = 0; i < 4; i++){
    ledcWrite(i, 0.175*PWM_MAX);
    delay(150);
    ledcWrite(i, 0);
    ledcWrite(i+4, 0.175*PWM_MAX);
    delay(180);
    ledcWrite(i+4, 0);
    delay(1000);
  }

  for (int i = 0; i < 2; i++){
    digitalWrite(endeffectorDirectionPin[i], 1);
    ledcWrite(i + 8, 0.175*PWM_MAX);
    delay(150);
    digitalWrite(endeffectorDirectionPin[i], 0);
    ledcWrite(i+8, 0);
    delay(1000);
  }
}