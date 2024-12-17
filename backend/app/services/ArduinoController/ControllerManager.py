class ControllerManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ControllerManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'deviceMap'):
            self.deviceMap = dict({"123" : "http://host.docker.internal:8080"})

    def getAddr(self, id):
        if id in self.deviceMap:
            return self.deviceMap[id]
        else:
            return ""
    
    def register(self, id, address):
        self.deviceMap[id] = address
    
    def deleteDevice(self, id):
        if id in self.deviceMap:
            del self.deviceMap[id]