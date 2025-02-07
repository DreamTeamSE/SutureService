from concurrent import futures
import logging

import grpc

from app.repository.control_device_pb2 import ControlRequest
from app.repository.control_device_pb2_grpc import ControlDeviceStub



class DeviceRepository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DeviceRepository, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    

    def control_device(self, domain: str, control: str) -> dict:
        print(domain)
        with grpc.insecure_channel(domain) as channel:
            stub = ControlDeviceStub(channel)
            response = stub.Control(ControlRequest(control=control))
            return {"message": response.message, "velocity_list": response.metrics.velocity_list, "acceleration_list": response.metrics.acceleration_list}
