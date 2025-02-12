import logging
from threading import Thread
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device
from exceptions.device_exceptions import InvalidDeviceStateException


class StartStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if device.is_running:
            raise InvalidDeviceStateException("Device is already running")
        device.start()
        thread = Thread(target=device.run)
        thread.daemon = True
        thread.start()
        return {"status": "Device started"}