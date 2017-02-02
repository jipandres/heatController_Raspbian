# Test Environment

## Hardware
It is composed of a Raspberry Pi 1 Model B connected to a breadboard with a 26 specific ribbon.

A single relay
Leds
Resistors

<TODO: add picture>

### GPIO schema
It can be found in the web, for example in https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins

### The ribbon adapter to breadboard
https://www.youtube.com/watch?v=3TWUp_TFWBE

Available at amazon.es https://www.amazon.es/gp/product/B00R76SGP6/ref=oh_aui_detailpage_o04_s00?ie=UTF8&psc=1


### Mapping between the name in the protoboard connector and the BCM GPIO PIN

Assuming BCM GPIO mode 
"GPIO.setmode(GPIO.BCM)"

|Column 1 | GPIO PIN | GPIO PIN | Column 2|
| --- | --- | --- | --- |
| CE1  |  7 | 17 | P0 | 
| CE0  |  8 | 18 | P1 |
| SCLK | 11 | 27 | P2 | 
| MISO |  9 | 22 | P3 | 
| MOSI | 10 | 23 | P4 | 
| RXD  | 15 | 24 | P5 | 
| TXD  | 14 | 25 | P6 | 
| SCL  | 3  |  4 | P7 |
| SCA  | 2  | GND| GND|

