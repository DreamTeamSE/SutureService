from pydantic import BaseModel

class ControlDTO(BaseModel):
    email: str = ""
    action: str = ""
    deviceID: str = ""
   