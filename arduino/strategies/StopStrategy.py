import logging
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device


class StopStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        try:
            if not device.is_running:
                raise ValueError("Device is not running")
            device.stop()
            output = device.getData()
            device.newCache()
            return {"message": "Successfully Stopped", "metrics" : output}
        except ValueError as e:
            logging.error(f"Error has occured while stoping device: {e}")
            raise