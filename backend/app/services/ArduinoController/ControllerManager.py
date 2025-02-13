import logging
from app.repository.DeviceRepository import DeviceRepository

class ControllerManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ControllerManager, cls).__new__(cls)

        return cls._instance

    def __init__(self, device_repo : DeviceRepository) -> None:
        if not hasattr(self, 'device_map'):
            self.device_map = dict({"123" : "http://host.docker.internal:8080"})
        self.device_repo = device_repo

    def control_device(self, domain : str, control : str):
        return self.device_repo.control_device(domain, control)
        
    

    def get_addr(self, id) -> str:
        if id not in self.device_map:
            raise ValueError(f"ID {id} not registered")
        return self.device_map[id]
        
    
    def register(self, id, address) -> None:
        self.device_map[id] = address
    
    def delete_device(self, id) -> None:
        if id in self.device_map:
            del self.device_map[id]
        else:
            logging.warning(f"Device with ID {id} not found in registry")