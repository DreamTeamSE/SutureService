from abc import ABC, abstractmethod
from Device.Device import Device

class Response:
    @staticmethod
    def success(message: str, metrics=None):
        response = {
            "message": message,
            "status": "success"
        }
        if metrics is not None:
            response["metrics"] = metrics
        return response

    @staticmethod
    def error(message: str):
        return {
            "message": message,
            "status": "error"
        }

class DeviceStrategy(ABC):
    @abstractmethod
    def execute(self, device: Device) -> dict:
        pass