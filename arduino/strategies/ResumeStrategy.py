from .DeviceStrategy import DeviceStrategy, Response
from Device.Device import Device

class ResumeStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if device.is_running and device.is_paused:
            device.resume()
            return Response.success("Device resumed successfully", device.getData())
        return Response.error("Device is not running or not paused") 