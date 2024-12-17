from pydantic import BaseModel

class ControlDTO(BaseModel):
    email: str = ""
    action: str = ""
    device_id: str = ""
   