import logging
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device
from exceptions.device_exceptions import InvalidDeviceStateException


class ResumeStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if not device.is_running:
            raise InvalidDeviceStateException("Couldn't unpause the device: Device is not running")
        if not device.is_paused:
            raise InvalidDeviceStateException("Couldn't unpause the device: Device is not paused")
        device.resume()