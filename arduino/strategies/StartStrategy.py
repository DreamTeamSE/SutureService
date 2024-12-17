from threading import Thread
from .DeviceStrategy import DeviceStrategy, Response
from Device.Device import Device


class StartStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if not device.is_running:
            device.start()
            thread = Thread(target=device.run)
            thread.daemon = True
            thread.start()
            return Response.success("Device started successfully", device.getData())
        return Response.error("Device is already running") 