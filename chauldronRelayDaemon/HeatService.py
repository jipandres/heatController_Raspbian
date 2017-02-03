"""App designed to be controlled by an start-stop-daemon"""
import HeatController
import GPIODriver
import signal

heatController = 0

#STOP call: The program should be alive until the stop signal (SIGTERM) is received
def terminationSignalHandler(signum, frame)
    if signum == signal.SIGTERM:
        print 'Signal to stop service received'
        heatController.stop()
    else:
        """LOG: Abnormal termination"""
        print 'Abnormal termination. Controller not stopped'
        
signal.signal(signal.SIGTERM, terminationSignalHandler)

#START call. Expects one parameter with the GPIO PIN number
# TODO: Main program that receives as input parameters the GPIO port (BCM) and the configuration file (2nd step)
if __name__ == "__main__":
    relayDriver = GPIODriver() """ pass PIN number """
    heatController =HeatController(relayDriver)
    heatController.start()

