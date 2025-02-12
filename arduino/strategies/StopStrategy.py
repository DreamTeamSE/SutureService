import logging
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device
from exceptions.device_exceptions import InvalidDeviceStateException

class StopStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if not device.is_running:
            raise InvalidDeviceStateException("Couldnt Stop Device : Device Isn't running")
        device.stop()
        metrics = device.getMetrics()
        device.newCache()
        return {"message": "Successfully Stopped", "metrics" : metrics}