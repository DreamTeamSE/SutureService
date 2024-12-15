from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from strategies.DeviceStrategyFactory import DeviceStrategyFactory
from Device.Device import Device

app = FastAPI()
device = Device("123")

class DeviceControl(BaseModel):
    action: str

@app.post("/device/control")
def controlDevice(control: DeviceControl):
    strategy = DeviceStrategyFactory.getStrategy(control.action)
    
    if not strategy:
        raise HTTPException(status_code=400, detail="Invalid action")
    
    return strategy.execute(device)

