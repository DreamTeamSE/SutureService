from pydantic import BaseModel

class ControlDTO(BaseModel):
    email: str = ""
    control: str = ""
    device_id: str = ""
   