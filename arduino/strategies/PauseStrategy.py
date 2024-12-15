from .DeviceStrategy import DeviceStrategy
from Device.Device import Device

class PauseStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if device.is_running:
            device.pause()
            return {"status": "Trainning paused"}
        return {"status": "Device is not running"} 