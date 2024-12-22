import logging
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device

class ResumeStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
            if not device.is_running:
                raise ValueError("Couldn't Unpaused the Device : Device is Not Running")
            if not device.is_paused:
                raise ValueError("Couldn't Unpaused the Device : Device is Not Paused")
            device.resume()
            return {"message": "Successfully Resumed"}