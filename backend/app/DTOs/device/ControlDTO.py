from pydantic import BaseModel

class ControlDTO(BaseModel):
    control: str = ""
    device_id: str = ""
   