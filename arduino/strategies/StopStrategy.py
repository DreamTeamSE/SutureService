from .DeviceStrategy import DeviceStrategy
from Device.Device import Device

class StopStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if device.is_running:

            device.stop()
            output = device.getData()
            device.clearCache()
            return {"status": "Trainning stopped", "data": output}
        return {"status": "Device is not running"} 