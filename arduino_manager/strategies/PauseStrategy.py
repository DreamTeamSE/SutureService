import logging
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device
from exceptions.device_exceptions import InvalidDeviceStateException



class PauseStrategy(DeviceStrategy):
    """
    
    PauseStrategy pauses the device.

    This strategy is used to pause a device that is currently running. It checks the current state of the device and raises an exception if the device is not running or if it is already paused.

    """
    def execute(self, device: Device) -> None:
        if not device.is_running:
            raise InvalidDeviceStateException("Device is not running")
        if device.is_paused:
            raise InvalidDeviceStateException("Device is already paused")
        device.pause()