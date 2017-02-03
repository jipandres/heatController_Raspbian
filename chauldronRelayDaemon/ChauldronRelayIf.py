from abc import ABCMeta, abstractmethod

class ChauldronRelayIf(metaclass=ABCMeta):
  @abstractmethod
  def setup()
    pass
  @abstractmethod
  def start()
    pass
  @abstractmethod
  def stop()
    pass
  @abstractmethod
  def release()
    pass
