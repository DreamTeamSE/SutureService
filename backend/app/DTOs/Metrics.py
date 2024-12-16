from typing import List
from pydantic import BaseModel

class Metrics(BaseModel):
    top: int = 0
    average: float = 0
    errors: int = 0
    points: List[int] = []