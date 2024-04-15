#include "Arduino.h"
#include <SPI.h>
#include <vector>

static const uint32_t c_hspiSsPin1 = 15;
static const uint32_t c_hspiSsPin2 = 5;
static const uint16_t c_nop = 0x0;
static const uint16_t c_clearError = 0x4001;
static const uint16_t c_readAngle = 0xFFFF;
static const uint16_t c_dataMask = 0x3FFF;
std::vector<uint16_t> m_values;

int incomingByte = 0;    // for incoming serial data
SPIClass m_spi;
SPISettings m_settings;

int channel = 0;

void setup()
{
    Serial.begin(9600);    // opens serial port, sets data rate to 9600 bps
    SPI.begin ();
    SPI.setClockDivider(SPI_CLOCK_DIV128);

    pinMode(13, OUTPUT);
    pinMode(c_hspiSsPin1, OUTPUT);
    pinMode(c_hspiSsPin2, OUTPUT);
    m_values.resize(4, 0);
}

void loop(){
  // send data only when you receive data:
  // if (Serial.available() > 0) {
  //   // read the incoming byte:
  //   incomingByte = Serial.read();
  //   // say what you got:
  //   Serial.write(incomingByte);
  // }

    uint16_t buf = 0;
    m_spi.beginTransaction(m_settings);
    digitalWrite(13, HIGH);

    if (channel == 0) {digitalWrite(c_hspiSsPin1, LOW);}
    else if(channel == 1) {digitalWrite(c_hspiSsPin2, LOW);}
    for(auto i = 0; i < m_values.size()/2; ++i)
    {
        buf = m_spi.transfer16(c_readAngle);
        Serial.printf("%d", buf);
        Serial.println();
    }
    digitalWrite(c_hspiSsPin1, HIGH);
    digitalWrite(c_hspiSsPin2, HIGH);

    delayMicroseconds(1);

    if(channel == 0) digitalWrite(c_hspiSsPin1, LOW);
    else if(channel == 1) digitalWrite(c_hspiSsPin2, LOW);
    for(auto i = 0; i < m_values.size()/2; ++i)
    {
        buf = m_spi.transfer16(c_nop);
        Serial.printf("%d", buf);
        Serial.println();
        m_values[i + channel*2] = buf & c_dataMask;
        Serial.printf("m_values%d\t%d\n", i, m_values[i + channel*2]);
        Serial.println();
    }
    digitalWrite(c_hspiSsPin1, HIGH);
    digitalWrite(c_hspiSsPin2, HIGH);

    m_spi.endTransaction();

    // for(int i=0; i < 4; i++){
    //     m_encoders[i].m_lastValidAngle = m_values[i];
    //     // DPSerial::sendQueuedDebugLog("zero %u reported=%u", m_zeros[i], m_encoders[i].m_lastValidAngle);
    // }

  
}