from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import metrics, user, device
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(user.router)
app.include_router(metrics.router)
app.include_router(device.router)