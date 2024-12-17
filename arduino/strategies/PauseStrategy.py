from .DeviceStrategy import DeviceStrategy, Response
from Device.Device import Device

class PauseStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if device.is_running and not device.is_paused:
            device.pause()
            return Response.success("Device paused successfully", device.getData())
        return Response.error("Device is not running or already paused") 