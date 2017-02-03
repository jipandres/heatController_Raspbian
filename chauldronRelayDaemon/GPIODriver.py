import RPi.GPIO as GPIO


class GPIODriver(ChauldronRelayIf):
  PIN

  def _init_(self,pin):
    self.PIN = pin
    GPIO.setmode(GPIO.BCM)
 
  def setup(self):
    GPIO.setup(self.PIN,GPIO.OUTPUT)

  def start(self):
    GPIO.output(self.PIN,GPIO.HIGH)

  def stop(self):
    GPIO.output(self.PIN,GPIO.LOW)
 
  def release(self):
    GPIO.cleanup()


  
        
