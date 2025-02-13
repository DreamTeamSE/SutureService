from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import metrics, user, device
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174", "http://suture-pads.com.s3-website.us-east-2.amazonaws.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(user.router)
app.include_router(metrics.router)
app.include_router(device.router)