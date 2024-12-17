from threading import Thread
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device

class StartStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if not device.is_running:
            device.start()
            thread = Thread(target=device.run)
            thread.daemon = True
            thread.start()
            return {
                "message": "Device started successfully",
                "metrics": device.getData(),
                "status": "success"
            }
        return {
            "message": "Device is already running",
            "status": "error"
        } 