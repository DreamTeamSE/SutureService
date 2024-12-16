from pydantic import BaseModel

class Control(BaseModel):
    userID: str = ""
    action: str = ""
    deviceID: str = ""
   