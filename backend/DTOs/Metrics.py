from typing import List

class Metrics:
    def __init__(self, top: int = 0, average: float = 0, errors: int = 0, points: List[int] = None):
        self.top = top
        self.average = average
        self.errors = errors
        self.points = points if points is not None else []

    def __repr__(self):
        return f"MetricDTO(top={self.top}, average={self.average}, errors={self.errors}, points={self.points})"
