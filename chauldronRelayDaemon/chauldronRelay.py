##cookbook

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
