import logging
from .DeviceStrategy import DeviceStrategy
from Device.Device import Device

class ResumeStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        try:
            if not device.is_running:
                raise ValueError("Device is Not Running")
            if not device.is_paused:
                raise ValueError("Device is Not Paused")
            device.resume()
            return {"message": "Successfully Resumed"}
        except:
            logging.error(f"Error has occured while trying to unpause the device: {e}")
            raise