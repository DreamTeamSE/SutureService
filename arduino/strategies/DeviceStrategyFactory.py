from .StartStrategy import StartStrategy
from .StopStrategy import StopStrategy
from .PauseStrategy import PauseStrategy
from .ResumeStrategy import ResumeStrategy
from .DeviceStrategy import DeviceStrategy
from fastapi import HTTPException
from exceptions.device_exceptions import InvalidControlException




class DeviceStrategyFactory:
    _strategies = {
        "start": StartStrategy(),
        "stop": StopStrategy(),
        "pause": PauseStrategy(),
        "resume": ResumeStrategy()
    }

    @classmethod
    def getStrategy(cls, control: str) -> DeviceStrategy:
        if control not in cls._strategies:
            raise InvalidControlException(f"Invalid action: '{control}' is not recognized")
        
        return cls._strategies[control]