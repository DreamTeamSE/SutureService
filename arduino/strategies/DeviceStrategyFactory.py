from .StartStrategy import StartStrategy
from .StopStrategy import StopStrategy
from .PauseStrategy import PauseStrategy
from .ResumeStrategy import ResumeStrategy
from .DeviceStrategy import DeviceStrategy

class DeviceStrategyFactory:
    _strategies = {
        "start": StartStrategy(),
        "stop": StopStrategy(),
        "pause" : PauseStrategy(),
        "resume" : ResumeStrategy()
    }

    @classmethod
    def getStrategy(cls, control: str) -> DeviceStrategy:
        return cls._strategies.get(control) 