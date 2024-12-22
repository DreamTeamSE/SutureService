import logging
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device


class StopStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if not device.is_running:
            raise ValueError("Couldnt Stop Device : Device Isn't running")
        device.stop()
        output = device.getData()
        device.newCache()
        return {"message": "Successfully Stopped", "metrics" : output}