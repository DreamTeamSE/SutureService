class ControllerService:
    def __init__(self, deviceID: int, userID: int):
        self.deviceID = deviceID
        self.userID = userID

    def startCollection(self) -> bool:
        # hit endpoint in respective controller to start collecting
        return True

    def stopCollection(self):
        # hit endpoint in respective controller to stop collecting
        return True


