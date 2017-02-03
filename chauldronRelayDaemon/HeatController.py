

class HeatController():
    relay
    
    def _init_ (self, ChauldronRelayIf relay):
        self.relay = relay
        
    def start():
        self.relay.setup()
        """ Here is where the logic to do advance chauldron programming can be handled"""
        self.relay.start()
        
    def stop():
        self.relay.stop()
        self.relay.cleanup()

