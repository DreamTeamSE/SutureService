from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlRequest(_message.Message):
    __slots__ = ("control",)
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    control: str
    def __init__(self, control: _Optional[str] = ...) -> None: ...

class ControlResponse(_message.Message):
    __slots__ = ("message", "metrics")
    class Metrics(_message.Message):
        __slots__ = ("velocity_list", "acceleration_list")
        VELOCITY_LIST_FIELD_NUMBER: _ClassVar[int]
        ACCELERATION_LIST_FIELD_NUMBER: _ClassVar[int]
        velocity_list: _containers.RepeatedScalarFieldContainer[float]
        acceleration_list: _containers.RepeatedScalarFieldContainer[float]
        def __init__(self, velocity_list: _Optional[_Iterable[float]] = ..., acceleration_list: _Optional[_Iterable[float]] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    message: str
    metrics: ControlResponse.Metrics
    def __init__(self, message: _Optional[str] = ..., metrics: _Optional[_Union[ControlResponse.Metrics, _Mapping]] = ...) -> None: ...
