from typing import List
from pydantic import BaseModel

class DeviceMetricsDTO(BaseModel):
    velocity_list: List[float] = []
    acceleration_list: List[float] = []