from typing import List
from pydantic import BaseModel

class DeviceMetrics(BaseModel):
    velocityList: List[float]
    accelerationList: List[float]