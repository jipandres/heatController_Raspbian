# TODO: Main program that receives as input parameters the GPIO port (BCM) and the configuration file (2nd step)
#The program should be alive until the stop signal is received (not needed in the first phase but mandatory in the second in order to stop the chauldron during nights
SIGTERM (by default) is received in that case 

# The program could be handle by a start-stop-daemon if stop sends a signal to the program that allows to cleanup the GPIO pin


##cookbook

## Signal handling

import signal, os

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Disable the alarm

##-----------------------
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
    
GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)

#to add a list of channels (11 and 12 are the pin numbers)
chan_list = [11,12]    
GPIO.setup(chan_list, GPIO.OUT)

# to change the status
chan_list = [11,12]                             # also works with tuples
GPIO.output(chan_list, GPIO.LOW)                # sets all to GPIO.LOW
GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))   # sets first HIGH and second LOW


GPIO.cleanup(channel)
GPIO.cleanup( (channel1, channel2) )
GPIO.cleanup( [channel1, channel2] )

# To handle the input of GPIO such as buttons:
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/

#to change the GPIO value after pression a button.
GPIO.output(12, not GPIO.input(12))



###############################Another example

#EJEMPLO DE BLINKING CON RASPBERRY PI
#Escrito por Gl4r3
import RPi.GPIO as GPIO #importamos la libreria y cambiamos su nombre por "GPIO"
import time #necesario para los delays
 
#establecemos el sistema de numeracion que queramos, en mi caso BCM
GPIO.setmode(GPIO.BCM)
 
#configuramos el pin GPIO17 como una salida
GPIO.setup(17, GPIO.OUT)
 
#encendemos y apagamos el led 5 veces
for i in range(0,5):
    GPIO.output(17, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17, GPIO.LOW)
    time.sleep(1)
 
GPIO.cleanup()  #devuelve los pines a su estado inicial
