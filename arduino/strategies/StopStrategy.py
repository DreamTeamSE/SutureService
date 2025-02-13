import logging
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device
from exceptions.device_exceptions import InvalidDeviceStateException



class StopStrategy(DeviceStrategy):

    """
    StopStrategy stops the device.

    This strategy is used to stop a device that is currently running. It checks the current state of the device and raises an exception if the device is not running. 
    Once the device is stopped, it retrieves the metrics from the device, clears the cache, and returns the metrics.
    
    """

    def execute(self, device: Device) -> dict:
        if not device.is_running:
            raise InvalidDeviceStateException("Couldn't stop device: Device isn't running")
        device.stop()
        metrics = device.get_metrics()
        device.new_cache()
        return {"metrics": metrics}