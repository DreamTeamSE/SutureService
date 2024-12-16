from pydantic import BaseModel

class Control(BaseModel):
    email: str = ""
    action: str = ""
    deviceID: str = ""
   