from pydantic import BaseModel

class CalculatedMetricsDTO(BaseModel):
    top_velocity: float = 0.0
    top_acceleration: float = 0.0
    average_velocity: float = 0.0
    average_acceleration: float = 0.0