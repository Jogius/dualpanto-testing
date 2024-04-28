#include "Arduino.h"
#include <Encoder.h>
#include <SPI.h>
#include <vector>


// encoder
static const uint32_t c_hspiSsPin1 = 15;
static const uint32_t c_hspiSsPin2 = 5;
static const uint16_t c_nop = 0x0;
static const uint16_t c_clearError = 0x4001;
static const uint16_t c_readAngle = 0xFFFF; //0xFFFF
static const uint16_t c_dataMask = 0x3FFF;

static const uint16_t endeffectorEncoderPin[2] = {35, 36};
static const uint16_t endeffectorEncoderPin2[2] = {34, 39};
Encoder* endeffectorEncoder[2];

SPIClass m_spi(HSPI);
SPISettings m_settings(10000000, SPI_MSBFIRST, SPI_MODE1);

uint16_t buf = 0;

// motors

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

// #####

//int incomingByte = 0;    // for incoming serial data


std::vector<uint16_t> m_values;
void setup_encoders(){
  pinMode(13, OUTPUT);
  pinMode(c_hspiSsPin1, OUTPUT);
  pinMode(c_hspiSsPin2, OUTPUT);

  for (int i = 0; i < 2; i++){
      pinMode(endeffectorEncoderPin[i], INPUT);
      pinMode(endeffectorEncoderPin2[i], INPUT);
      endeffectorEncoder[i] = new Encoder(
          endeffectorEncoderPin[i], endeffectorEncoderPin2[i]);
  }

  m_values.resize(4, 0);

  m_spi.begin();
}

void setup_motors(){
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

void reset_motors(){
  for (int i = 0; i < 8; i++){
    ledcWrite(i, 0.175*PWM_MAX);
    delay(10);
    ledcWrite(i, 0);
  }

  for (int i = 0; i < 2; i++){
    digitalWrite(endeffectorDirectionPin[i], 1);
    ledcWrite(i + 8, 0.175*PWM_MAX);
    delay(10);
    digitalWrite(endeffectorDirectionPin[i], 0);
    ledcWrite(i+8, 0);
  }
}

int channel = 0;
int c_i = 0;
void loop_encoders(){
  m_spi.beginTransaction(m_settings);
  digitalWrite(13, HIGH);
  digitalWrite(c_hspiSsPin1, HIGH);
  digitalWrite(c_hspiSsPin2, HIGH);
  if (channel == 0) {digitalWrite(c_hspiSsPin1, LOW);}
    else if(channel == 1) {digitalWrite(c_hspiSsPin2, LOW);}
    for(auto i = 0; i < m_values.size()/2; ++i)
    {
        buf = m_spi.transfer16(c_readAngle);
        //Serial.printf("%d", buf);
        //Serial.println();
    }
    digitalWrite(c_hspiSsPin1, HIGH);
    digitalWrite(c_hspiSsPin2, HIGH);

    delayMicroseconds(1);

    if (channel == 0){
        Serial.printf("\ndptest");
    }

    if(channel == 0) digitalWrite(c_hspiSsPin1, LOW);
    else if(channel == 1) digitalWrite(c_hspiSsPin2, LOW);
    for(auto i = 0; i < m_values.size()/2; ++i)
    {
        buf = m_spi.transfer16(c_nop);
        m_values[i + channel*2] = buf & c_dataMask;
        Serial.printf("%d,", m_values[i + channel*2]);
    }
    digitalWrite(c_hspiSsPin1, HIGH);
    digitalWrite(c_hspiSsPin2, HIGH);

    m_spi.endTransaction();

    if (channel == 1){
        for (int i = 0; i < 2; i++){
            Serial.printf("%d,", endeffectorEncoder[i]->read());
        }
    }

    c_i++;
    channel = c_i % 2;
}

void loop_motors(){
  char* buf2 = new char[64];
  if (Serial.available() > 0){
    if (Serial.findUntil("dpmotor", "")){
      Serial.readBytesUntil(';', buf2, 64);
    }
    buf2[63] = '\0';
    Serial.printf("--> %s\n", buf2);
    if (std::equal(buf2, buf2 + 7, "dpmotor")){
      Serial.printf("%s\n", buf2 + 6);
      
      ledcWrite(0, 0.175*PWM_MAX);
      delay(100);
      ledcWrite(0, 0);
      delay(200);
    }
  }

  


  //Serial.printf("ok\n");
  
  // ledcWrite(4, 0.175*PWM_MAX);
  // delay(100);
  // ledcWrite(4, 0);
  // delay(1000);

  // if (!std::equal(buf2, buf2 + 7, "dpmotor")){
  //   Serial.printf("no dpmotor");
  //   return;
  //   }
  
  delete[] buf2;
}

void setup(){
  Serial.begin(9600);    // opens serial port, sets data rate to 9600 bps
  //setup_encoders();
  setup_motors();
  reset_motors();
}

void loop(){  
  loop_motors();
}
