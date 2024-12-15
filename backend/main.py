from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from DTOs.Metrics import Metrics
from DTOs.Control import Control
from services.ControllerManager import ControllerManager
import random
import httpx

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://suture-pads.com.s3-website.us-east-2.amazonaws.com"],  # Allow your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

manager = ControllerManager()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}

@app.post("/control")
def controlAction(control: Control):
    addr = manager.getAddr(control.deviceID)
    path = "device/control"
    print(addr)

    

    try:
        response = httpx.post(addr + "/" + path, json={"action" : control.action}) 
        response.raise_for_status()  
        res = response.json()  
    except httpx.HTTPStatusError as e:
        return {"message": "Failed", "error": str(e)}
    except Exception as e:
        return {"message": "Failed", "error": str(e)}
    if "data" in res:
        return {"message": "Success", "res": res["data"]}
    else:
        return {"message": "Success"}