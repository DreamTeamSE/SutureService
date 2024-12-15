from .DeviceStrategy import DeviceStrategy
from Device.Device import Device

class StopStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if device.is_running:
            output = device.stop()
            print(output)
            return {"status": "Trainning stopped"}
        return {"status": "Device is not running"} 