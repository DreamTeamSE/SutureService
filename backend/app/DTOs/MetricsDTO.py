from typing import List
from pydantic import BaseModel

class MetricsDTO(BaseModel):
    email: str
    velocity_list: List[float]
    acceleration_list: List[float]
    top_velocity: float
    top_acceleration: float
    average_velocity: float
    average_acceleration: float