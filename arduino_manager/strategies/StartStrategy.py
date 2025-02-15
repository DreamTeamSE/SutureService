import logging
from threading import Thread
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device
from exceptions.device_exceptions import InvalidDeviceStateException




class StartStrategy(DeviceStrategy):
    """
    StartStrategy starts the device.

    This strategy is used to start a device that is currently not running. It checks the current state of the device and raises an exception if the device is already running. 
    Once the device is started, it runs in a separate thread to continuously generate and cache metrics until it is stopped or paused.
    """

    def execute(self, device: Device) -> dict:
        if device.is_running:
            raise InvalidDeviceStateException("Device is already running")
        device.start()
        thread = Thread(target=device.run)
        thread.daemon = True
        thread.start()
        return