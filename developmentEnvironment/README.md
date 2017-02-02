# Mapping between the name in the protoboard connector and the BCM GPIO PIN
Assuming BCM GPIO mode: GPIO.setmode(GPIO.BCM)
|Protoboard description\nColumn 1|GPIO PIN |GPIO PIN | Protoboard description\nColumn 2| 
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


GPIO.setmode(GPIO.BCM)
#Protoboard - GPIO PIN
#P0         - 17
#P1         - 18
#P2         - 27
#P3         - 22
#P4         - 23
#P5         - 24
#P6         - 25
#P7         - 4

#CE1        - 7
#CEO        - 8
#SCLK       - 11
#MISO       - 9
#MOSI       - 10
#RXD        - 15
#TXD        - 14  
#SCL        - 3
#SDA        - 2

Some information comes here: https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
The ribbon and the adapter board that I have https://www.amazon.es/gp/product/B00R76SGP6/ref=oh_aui_detailpage_o04_s00?ie=UTF8&psc=1
