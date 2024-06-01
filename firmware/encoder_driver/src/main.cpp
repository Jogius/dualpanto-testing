#include "Arduino.h"
#include <SPI.h>
#include <vector>

static const uint32_t c_hspiCsPin = 15;
static const uint32_t c_encoderOn = 13;
static const uint16_t c_nop = 0x0;
static const uint16_t c_clearError = 0x4001;
static const uint16_t c_readAngle = 0xFFFF;
static const uint16_t c_dataMask = 0x3FFF;

std::vector<uint16_t> m_values;

int incomingByte = 0;    // for incoming serial data
SPIClass m_spi(HSPI);
SPISettings m_settings(10000000, SPI_MSBFIRST, SPI_MODE1);

int channel = 0;
int c_i = 0;
uint16_t buf = 0;

void setup()
{
    Serial.begin(9600);

    pinMode(c_encoderOn, OUTPUT);
    digitalWrite(c_encoderOn, HIGH);

    pinMode(c_hspiCsPin, OUTPUT);

    m_values.resize(2, 0);

    m_spi.begin();
}

void loop(){
    m_spi.beginTransaction(m_settings);
    digitalWrite(c_hspiCsPin, HIGH);

    // TODO begin the transaction by settings the chipselect to LOW

    for(auto i = 0; i < m_values.size(); ++i)
    {
        // TODO then send the message to read the angle to the two encoders
        buf = m_spi.transfer16(/* TODO INSERT COMMAND BYTES HERE*/);
    }


    // TODO then trigger the evaluation of the current command by raising the the chipselect to high
    // TODO wait for a microsecond
    // TODO and set it to low again

    // start reading from the encoders one by one
    for(auto i = 0; i < m_values.size(); ++i)
    {
        // TODO send a noop instruction
        buf = m_spi.transfer16(/* TODO INSERT NOOP INSTUCTION HERE */);
        // ignore the leading bit as our encoder only uses 7 bit
        m_values[i + channel*2] = buf & c_dataMask;
        // and print
        Serial.printf("%d,", m_values[i]);
    }
    // TODO terminate the transmission by raising the chipselect to HIGH

    m_spi.endTransaction();
}