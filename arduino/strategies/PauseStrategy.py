import logging
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device
from exceptions.device_exceptions import InvalidDeviceStateException


class PauseStrategy(DeviceStrategy):
    def execute(self, device: Device) -> None:
            if not device.is_running:
                raise InvalidDeviceStateException("Device is Not Running")
            if device.is_paused:
                raise InvalidDeviceStateException("Device is Already Paused")
            device.pause()
            return