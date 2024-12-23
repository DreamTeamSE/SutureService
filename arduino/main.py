import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from strategies.DeviceStrategyFactory import DeviceStrategyFactory
from Device.Device import Device

import grpc
from  control_device_pb2 import ControlResponse
from control_device_pb2_grpc import ControlDeviceServicer, add_ControlDeviceServicer_to_server
from concurrent import futures
import logging

app = FastAPI()
device = Device("123")

class DeviceControl(BaseModel):
    control: str


class ControlDevice(ControlDeviceServicer):
    def Control(self, request, context):
        response = control_device(request)
        message = response['message']

        metrics = None
        print(response)
        if 'metrics' in response:
            metrics = response['metrics']
            return ControlResponse(message=message, metrics=metrics)
        return ControlResponse(message=message)

    




def serve():
    try:
        port = "50051"
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_ControlDeviceServicer_to_server(ControlDevice(), server)
        server.add_insecure_port("[::]:" + port)
        server.start()
        print("Server started, listening on " + port)
        server.wait_for_termination()
    except ValueError as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))




def control_device(deviceAction: DeviceControl):
    strategy = DeviceStrategyFactory.getStrategy(deviceAction.control)
    if not strategy:
        raise HTTPException(status_code=400, detail="Invalid action: Action not recognized")
    

    return strategy.execute(device)

    
if __name__ == "__main__":
    logging.basicConfig()
    serve()
