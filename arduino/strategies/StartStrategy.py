import logging
from threading import Thread
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device


class StartStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        try:
            if device.is_running:
                raise ValueError("Device is already running")
            device.start()
            thread = Thread(target=device.run)
            thread.daemon = True
            thread.start()
            return {"message": "Successfully Started"}
        except ValueError as e:
            logging.error(f"Error Has Occured While Starting Device: {e}")
            raise