from abc import ABC, abstractmethod
from Device.Device import Device


class DeviceStrategy(ABC):
    """Abstract base class for device strategies.

    This class serves as a template for all device strategies, ensuring that they implement the execute method.
    """

    @abstractmethod
    def execute(self, device: Device) -> dict:
        pass