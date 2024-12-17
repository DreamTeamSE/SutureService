from .DeviceStrategy import DeviceStrategy, Response
from Device.Device import Device


class StopStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if device.is_running:
            device.stop()
            output = device.getData()
            device.newCache()
            return Response.success("Training stopped", output)
        return Response.error("Device is not running") 