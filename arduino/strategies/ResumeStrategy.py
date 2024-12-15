from threading import Thread
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device

class ResumeStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if device.is_running:
            device.resume()
            return {"status": "Trainning Resumed"}
        return {"status": "Device is already running"} 