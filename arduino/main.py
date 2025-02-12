
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from strategies.DeviceStrategyFactory import DeviceStrategyFactory
from Device.Device import Device
import logging

app = FastAPI()
device = Device("123")

class DeviceControl(BaseModel):
    control: str


@app.get("/")
async def welcome():
    return {"message" : "Hello World!"}



@app.post("/control-device/")
async def control_device_endpoint(device_action: DeviceControl):
    try:
        print(device_action)
        response = control_device(device_action)
        message = response['message']
        metrics = response.get('metrics', {})
        print(metrics)
        if not 'velocity_list' in metrics:
            return {}
        else:
            return {"velocity_list": metrics['velocity_list'], "acceleration_list": metrics['acceleration_list']}
    except HTTPException as e:
        raise e  # Re-raises HTTP exceptions as they are
    except Exception as e:
        logging.error("Unhandled Exception", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Unchecked Exception, Debug Software {e}")


def control_device(device_action: DeviceControl):
    strategy = DeviceStrategyFactory.getStrategy(device_action.control)
    if not strategy:
        raise HTTPException(status_code=400, detail="Invalid action: Action not recognized")
    return strategy.execute(device)


if __name__ == "__main__":
    import uvicorn
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host="0.0.0.0", port=8080)
