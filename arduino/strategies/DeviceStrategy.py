from abc import ABC, abstractmethod
from threading import Thread
from Device.Device import Device

class DeviceStrategy(ABC):
    @abstractmethod
    def execute(self, device: Device) -> dict:
        pass 