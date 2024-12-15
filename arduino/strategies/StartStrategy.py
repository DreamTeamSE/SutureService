from threading import Thread
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device

class StartStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if not device.is_running:
            device.start()
            thread = Thread(target=device.run)
            thread.start()
            return {"status": "Trainning started"}
        return {"status": "Device is already running"} 