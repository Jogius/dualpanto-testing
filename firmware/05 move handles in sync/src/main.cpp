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
int16_t encoders[6] = {0,0,0,0,0,0};
int32_t encoder_zero[6];

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

  //m_values.resize(4, 0);

  m_spi.begin();
}

int32_t overflow_correction[6] = {0,0,0,0,0,0};
uint16_t new_encoder_pos[6];
uint16_t last_encoder_pos[6] = {0,0,0,0,0,0};
void loop_encoders(){
  for (int channel = 0; channel < 2; channel++){
    m_spi.beginTransaction(m_settings);
    digitalWrite(13, HIGH);
    digitalWrite(c_hspiSsPin1, HIGH);
    digitalWrite(c_hspiSsPin2, HIGH);
    if (channel == 0) {digitalWrite(c_hspiSsPin2, LOW);}
    else if(channel == 1) {digitalWrite(c_hspiSsPin1, LOW);}
    for(auto i = 0; i < 2; ++i)
    {
        buf = m_spi.transfer16(c_readAngle);
    }
    digitalWrite(c_hspiSsPin1, HIGH);
    digitalWrite(c_hspiSsPin2, HIGH);

    delayMicroseconds(1);

    if (channel == 0){
        //Serial.printf("\ndptest");
    }

    if(channel == 0) digitalWrite(c_hspiSsPin2, LOW);
    else if(channel == 1) digitalWrite(c_hspiSsPin1, LOW);
    for(auto i = 0; i < 2; ++i){
        buf = m_spi.transfer16(c_nop);
        if (channel == 0){
          new_encoder_pos[(!i) + channel*2] = buf & c_dataMask;
          //Serial.printf("%d,", encoders[(!i) + channel*2]);
        } else {
          new_encoder_pos[i + channel*2] = buf & c_dataMask;
          //Serial.printf("%d,", encoders[i + channel*2]);
        }
    }
    digitalWrite(c_hspiSsPin1, HIGH);
    digitalWrite(c_hspiSsPin2, HIGH);

    m_spi.endTransaction();

    if (channel == 1){
        for (int i = 0; i < 2; i++){
            //Serial.printf("%d,", endeffectorEncoder[i]->read());
            new_encoder_pos[4 + i] = endeffectorEncoder[i]->read();
        }
    }
  }

  for (int i = 0; i < 6; i++){
    if (i == 1 || i == 2) { new_encoder_pos[i] = 16383 - new_encoder_pos[i];}

    if (i < 4){
    // int32_t diff = new_encoder_pos[i] - last_encoder_pos[i];
    // if (abs(new_encoder_pos[i] - last_encoder_pos[i] - 16383) < abs(diff)){
    //   //diff -= 16383;
    //   overflow_correction[i] -= 16383;
    // } else if (abs(new_encoder_pos[i] - last_encoder_pos[i] + 16383) < abs(diff)){
    //   //diff += 16383;
    //   overflow_correction[i] += 16383;
    //}
    //encoders[i] += diff;
      if (encoders[i] - overflow_correction[i] - new_encoder_pos[i] > 10000){
        overflow_correction[i] += 16383;
      }
      if (encoders[i] - overflow_correction[i] - new_encoder_pos[i] < -10000){
        overflow_correction[i] -= 16383;
      }
      encoders[i] = new_encoder_pos[i] + overflow_correction[i] - encoder_zero[i];
    } else {
      encoders[i] = abs(new_encoder_pos[i] % (136 * 2));
    }
    last_encoder_pos[i] = new_encoder_pos[i];
  }
}

bool calcParity(bool flag, uint16_t data)
{
    uint16_t temp = (data & c_dataMask) | (flag << 14);
    // calculate https://en.wikipedia.org/wiki/Hamming_weight
    temp -= (temp >> 1) & 0b0101010101010101;
    temp = (temp & 0b0011001100110011) + ((temp >> 2) & 0b0011001100110011);
    temp = (temp + (temp >> 4)) & 0b0000111100001111;
    return ((temp * 0b0000000100000001) >> 8) % 2;
}

uint16_t msg(bool flag, uint16_t data){
  bool parity = calcParity(flag, data);
  return data | (flag << 14) | (parity << 15);
}

void zero_encoders(uint16_t newZero[4]){
{
  m_spi.transfer16(msg(0, 0x16)); //c_highZeroWrite

	m_spi.beginTransaction(m_settings);
	digitalWrite(c_hspiSsPin1, LOW);
    for(auto i = 0; i < 2; ++i)
    {
      m_spi.transfer16(msg(0, newZero[i] >> 6));
      //m_encoders[i].transfer(SPIPacket(0, newZero[i] >> 6).m_transmission);
    }
	digitalWrite(c_hspiSsPin1, HIGH);
	// m_spi.endTransaction();

    //lower handle
	// m_spi.beginTransaction(m_settings);
	digitalWrite(c_hspiSsPin2, LOW);
	for (auto i = 0; i < 2; ++i)
	{
    m_spi.transfer16(msg(0, newZero[i+2] >> 6));
		//m_encoders[i+2].transfer(SPIPacket(0, newZero[i+2] >> 6).m_transmission);
	}
	digitalWrite(c_hspiSsPin2, HIGH);
	m_spi.endTransaction();

  m_spi.transfer16(msg(0, 0x17)); //c_lowZeroWrite

  m_spi.beginTransaction(m_settings);
	digitalWrite(c_hspiSsPin1, LOW);
    for(auto i = 0; i < 2; ++i)
    {
      m_spi.transfer16(msg(0, newZero[i] & 0b111111));
      //m_encoders[i].transfer(SPIPacket(0, newZero[i] & 0b111111).m_transmission);
    }
	digitalWrite(c_hspiSsPin1, HIGH);
	// m_spi.endTransaction();

    //lower handle
	// m_spi.beginTransaction(m_settings);
	digitalWrite(c_hspiSsPin2, LOW);
	for (auto i = 0; i < 2; ++i)
	{
    m_spi.transfer16(msg(0, newZero[i+2] & 0b111111));
		//m_encoders[i+2].transfer(SPIPacket(0, newZero[i+2] & 0b111111).m_transmission);
	}
	digitalWrite(c_hspiSsPin2, HIGH);
	m_spi.endTransaction();

    //transfer(SPICommands::c_readAngle);
    m_spi.transfer16(msg(1, 0x3FFF));
}
}

void send_encoders(){
  // for (int i = 0; i < 6; i++){
  //   Serial.printf("%d,", encoders[i] - encoder_zero[i]);
  // }
  // Serial.print(" -- ");
  for (int i = 0; i < 6; i++){
    Serial.printf("%d,", encoders[i]);
  }
  Serial.println("");
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

void move_to_end(uint16_t pid){
  loop_encoders();
  int last_pos = encoders[pid % 4] - 4;
  while ((abs(last_pos - encoders[pid % 4]) > 3)){ 
    int new_speed = (100 + abs(last_pos - encoders[pid % 4])) / 100;
    ledcWrite(pid, (1 / new_speed) * 0.3*PWM_MAX);
    delay(10);
    ledcWrite(pid, 0);
    //delay(10);
    last_pos = encoders[pid % 4];
    loop_encoders();
  }
}

void move_to(int32_t pos[6]){
  reset_motors();
  loop_encoders();
  int32_t last_encoders[6];
  for (int i = 0; i < 6; i++){last_encoders[i] = encoders[i];}
  int moving = 4;
  while (moving > 0){
    moving = 4;

    for (int i = 0; i < 4; i++){
      // forwards
      if (pos[i] - encoders[i] > 100){
        ledcWrite(i+4, 0);
        //Serial.printf("%d forward", i);
        int new_speed = (1 + abs(pos[i] - encoders[i])) / 1;
        ledcWrite(i, 0.1*PWM_MAX - ((1 / new_speed) * 0.1*PWM_MAX));
        
        //ledcWrite(i, 0.1*PWM_MAX);
      } else if (pos[i] - encoders[i] < -100){
        ledcWrite(i, 0);
        //Serial.printf("%d bacjward", i);
        int new_speed = (1 + abs(pos[i] - encoders[i])) / 1;
        ledcWrite(i + 4, 0.1*PWM_MAX - ((1 / new_speed) * 0.1*PWM_MAX));
        
        //ledcWrite(i + 4, 0.1*PWM_MAX);
      }
      else{
        //Serial.printf("%d none", i);
        ledcWrite(i, 0);
        ledcWrite(i + 4, 0);
        moving -= 1;
      }
      loop_encoders();
    }
    delay(1);

    for (int i = 0; i < 6; i++){last_encoders[i] = encoders[i];}
    loop_encoders();
    send_encoders();
  }
}

void align_motors(){
  reset_motors();
  // find zero position
  // move shorter handle to max
  loop_encoders();

  // upper handle
  move_to_end(5);
  ledcWrite(5, 0.4*PWM_MAX);
  move_to_end(4);
  ledcWrite(5, 0);
  for (int i = 0; i < 2; i++){ encoder_zero[i] = encoders[i];}
  //lower handle
  move_to_end(6);
  ledcWrite(6, 0.4*PWM_MAX);
  move_to_end(7);
  ledcWrite(6, 0);
  for (int i = 2; i < 4; i++){ encoder_zero[i] = encoders[i];}
  int correction[4] = {3700, -4000, -4000, 3700};
  for (int i = 0; i < 4; i++){ encoder_zero[i] -= correction[i];}


  // while ((encoders[0] - encoder_zero[0]) > -3700){
  //   ledcWrite(4, 0.4*PWM_MAX);
  //   delay(5);
  //   ledcWrite(4, 0);
  //   delay(25);
  //   loop_encoders();
  // }

  // while ((encoders[2] - encoder_zero[2]) > -3700){
  //   ledcWrite(7, 0.4*PWM_MAX);
  //   delay(5);
  //   ledcWrite(7, 0);
  //   delay(25);
  //   loop_encoders();
  // }
  //for (int i = 0; i < 4; i++){ encoder_zero[i] = encoders[i];}
}

void loop_motors(){
  
}

void setup(){
  Serial.begin(9600);    // opens serial port, sets data rate to 9600 bps
  setup_encoders();
  loop_encoders();
  // uint16_t newZero[4];
  // for (int i = 0; i < 4; i++ ){
  //   newZero[i] = encoders[i];
  // }
  // zero_encoders(newZero);
  // setup_motors();
  // reset_motors();
  // delay(100);
  // align_motors();
  
  // loop_encoders();
  // zero_encoders();
  // loop_encoders();
  // int32_t new_encoders[6];
  // for (int i = 0; i < 6; i++){new_encoders[i] = encoders[i];}
  // new_encoders[0] += 1000;
  //move_to(new_encoders);
}

void loop(){  
  delay(10);
  //loop_motors();
  loop_encoders();
  send_encoders();
}
