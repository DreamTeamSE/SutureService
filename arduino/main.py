import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from strategies.DeviceStrategyFactory import DeviceStrategyFactory
from Device.Device import Device
import uvicorn

app = FastAPI()
device = Device("123")

class DeviceControl(BaseModel):
    action: str

@app.post("/device/control")
def controlDevice(control: DeviceControl):
    try:
        strategy = DeviceStrategyFactory.getStrategy(control.action)
        if not strategy:
            raise HTTPException(status_code=400, detail="Invalid action: Action not recognized")
        return strategy.execute(device)
    except ValueError as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="172.16.227.89", port=8080)
