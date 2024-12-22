import logging
from threading import Thread
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device


class StartStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if device.is_running:
            raise ValueError("Couldn't Start Device: Device Is Already Running")
        device.start()
        thread = Thread(target=device.run)
        thread.daemon = True
        thread.start()
        return {"message": "Successfully Started"}