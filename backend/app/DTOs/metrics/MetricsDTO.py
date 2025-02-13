from typing import List
from pydantic import BaseModel
from app.DTOs.metrics.CalculatedMetricsDTO import CalculatedMetricsDTO

class MetricsDTO(BaseModel):
    device_id: str = ""
    velocity_list: List[float] = []
    acceleration_list: List[float] = []
    calculated_metrics: CalculatedMetricsDTO = CalculatedMetricsDTO()