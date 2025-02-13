import logging
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device
from exceptions.device_exceptions import InvalidDeviceStateException

class StopStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if not device.is_running:
            raise InvalidDeviceStateException("Couldn't stop device: Device isn't running")
        device.stop()
        metrics = device.get_metrics()
        device.new_cache()
        return {"metrics": metrics}