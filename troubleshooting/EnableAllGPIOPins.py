import RPi.GPIO as GPIO
import time 
 
GPIO.setmode(GPIO.BCM)
 
 
print "Start enabling GPIO pins with HIGH output value (for Model A & B -26pins) "
for i in (2,3,4,7,8,9,10,11,14,15,17,18,22,23,24,25,27):
  print "enabling %d" %i
  GPIO.setup(i, GPIO.OUT)
  GPIO.output(i, GPIO.HIGH)
  time.sleep(1)

print "Finish task. Restoring"
GPIO.cleanup() 
