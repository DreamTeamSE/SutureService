import logging
from threading import Thread
from time import sleep
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device
from exceptions.device_exceptions import InvalidDeviceStateException


class FixedStrategy(DeviceStrategy):
    """
    FixedStrategy runs the device for a fixed duration of 10 seconds.

    This strategy is used to run a device for a fixed period. It checks the current state of the device and raises an exception if the device is already running. 
    Once the device is started, it runs in a separate thread to continuously generate and cache metrics for 10 seconds.
    """

    def execute(self, device: Device) -> tuple:
        if device.is_running:
            raise InvalidDeviceStateException("Device is already running")
        return device.create_fixed_metrics()