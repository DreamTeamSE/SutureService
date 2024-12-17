from .DeviceStrategy import DeviceStrategy
from Device.Device import Device


class StopStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if device.is_running:
            device.stop()
            output = device.getData()
            device.newCache()
            return {
                "message": "Training stopped",
                "metrics": output,
                "status": "success"
            }
        return {
            "message": "Device is not running",
            "status": "error"
        } 