from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from strategies.DeviceStrategyFactory import DeviceStrategyFactory
from exceptions.device_exceptions import InvalidDeviceStateException, InvalidControlException
from Device.Device import Device
import logging

app = FastAPI()
device = Device("123")

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logging.error("Unhandled Exception", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error, Debug Application"},
    )

def get_device() -> Device:
    return device

@app.get("/")
async def welcome():
    return {"message": "Hello World!"}

@app.post("/control-device/{action}", 
          summary="Control the Device", 
          description="Performs the specified action on the device based on the action provided in the URL")
async def control_device(action: str):
    try:
        strategy = DeviceStrategyFactory.get_strategy(action)
        device = get_device()
        return strategy.execute(device)
    except InvalidDeviceStateException as e:
        logging.warning(f"Invalid Device State: {e}")
        raise HTTPException(status_code=400, detail=f"Invalid Device State: {e}")
    except InvalidControlException as e:
        logging.warning(f"Invalid Action: {e}")
        raise HTTPException(status_code=400, detail=f"Invalid Device State: {e}")

if __name__ == "__main__":
    import uvicorn
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host="0.0.0.0", port=8080)