import logging
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device

class PauseStrategy(DeviceStrategy):
    def execute(self, device: Device) -> None:
            if not device.is_running:
                raise ValueError("Device is Not Running")
            if device.is_paused:
                raise ValueError("Device is Already Paused")
            device.pause()
            return {"message": "Successfully Paused"}