import logging
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device
from exceptions.device_exceptions import InvalidDeviceStateException



class ResumeStrategy(DeviceStrategy):
        
    """
    ResumeStrategy resumes the device.

    This strategy is used to resume a device that is currently paused. It checks the current state of the device and raises an exception if the device is not running or if it is not paused.
    """


    def execute(self, device: Device) -> dict:
        if not device.is_running:
            raise InvalidDeviceStateException("Couldn't unpause the device: Device is not running")
        if not device.is_paused:
            raise InvalidDeviceStateException("Couldn't unpause the device: Device is not paused")
        device.resume()