import logging


class ControllerManager:
    _instance = None

    def __new__(cls, *args, **kwargs) -> 'ControllerManager':
        if not cls._instance:
            cls._instance = super(ControllerManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, 'deviceMap'):
            self.deviceMap = dict({"123" : "http://host.docker.internal:8080"})

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