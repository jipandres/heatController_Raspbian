try:
  import RPi.GPIO as GPIO
except ImportError:
    raise ImportError('GPIO not available, please check installation procedure')


class GPIODriver(ChauldronRelayIf):
  PIN

  def _init_(self,pin):
    self.PIN = pin
    GPIO.setmode(GPIO.BCM)
 
  def setup(self):
    GPIO.setup(self.PIN,GPIO.OUT)

  def start(self):
    GPIO.output(self.PIN,GPIO.HIGH)

  def stop(self):
    GPIO.output(self.PIN,GPIO.LOW)
 
  def release(self):
    GPIO.cleanup(self.PIN)


  
        
