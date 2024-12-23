import logging
from app.repository.DeviceRepository import DeviceRepository

class ControllerManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ControllerManager, cls).__new__(cls)

        return cls._instance

    def __init__(self, device_repo : DeviceRepository) -> None:
        if not hasattr(self, 'deviceMap'):
            self.deviceMap = dict({"123" : "host.docker.internal:50051"})
        self.device_repo = device_repo

    def control_device(self, domain : str, action : str):
        return self.device_repo.control_device(domain, action)
        
    

    def getAddr(self, id) -> str:
        if id in self.deviceMap:
            return self.deviceMap[id]
        logging.warning(f"ID {id} not registered")
        return ""
        
    
    def register(self, id, address) -> None:
        self.deviceMap[id] = address
    
    def deleteDevice(self, id) -> None:
        if id in self.deviceMap:
            del self.deviceMap[id]
        else:
            logging.warning(f"Device with ID {id} not found in registry")