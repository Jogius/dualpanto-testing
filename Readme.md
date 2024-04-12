# Dualpanto Testing

Goal of this repository is to provide some (semi) automatic testing for the dualpanto platform.

This involves basic functionality checks of the hardware, the firmware and potentially the unity integration

## Levels of Testing and Repository structure

### Hardware

On a hardware level we need to test that the dualpanto can

- show up as a serial device
- receive uploaded (mini) firmware
- read encoders
- actuate motors
- move two handles in sync

### Firmware

Please clone the current panto firmware into `firmware/10 panto firmware` and run `npm run script config`

On a firmware level we need to test that the dualpanto can
- perform the handshake
- keep the connection alive
- move the handles if instructed
- report the handle position
- accept obstacles
- render obstacles

### Unity

TODO


This project is currenty under developement

For questions, please reach out to martin.taraz@hpi.de