class ControllerManager:
    def init(self):
        self.deviceMap = dict({"123" : "http://localhost:8000"})
    
    def register(self, id, address):
        self.deviceMap[id] = address
    
    def deleteDevice(self, id):
        if id in self.deviceMap:
            del self.deviceMap[id]