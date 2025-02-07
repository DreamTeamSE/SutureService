from pydantic import BaseModel

class CalculatedMetricsDTO(BaseModel):
    top_velocity: float
    top_acceleration: float
    average_velocity: float
    average_acceleration: float