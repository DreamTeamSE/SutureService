from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from DTOs.Metrics import Metrics
from DTOs.Subscribe import Subscribe
import random

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://suture-pads.com.s3-website.us-east-2.amazonaws.com"],  # Allow your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}

@app.post("/subscribe")
def subscribe(subscribe: Subscribe):
    # TODO: Start stroing this units data in a database with start time and consider endtime when unsubscribing
    return "Subscribed"

@app.post("/unsubscribe")
def unsubscribe(subscribe: Subscribe):
    print(subscribe)
    acceleration = Metrics(
        top=random.randint(1, 10),
        average=random.randint(0, 10),
        errors=random.randint(0, 5),
        points=[random.randint(0, 10) for _ in range(random.randint(6, 50))]
    )

    velocity = Metrics(
        top=random.randint(1, 10),
        average=random.randint(0, 10),
        errors=random.randint(0, 5),
        points=[random.randint(0, 10) for _ in range(random.randint(6, 50))]
    )

    return {"acceleration" : acceleration, "velocity" : velocity}

@app.get("/recent/velocity")
def get_velocity():
    metrics = Metrics(
        top=random.randint(1, 10),
        average=random.randint(0, 10),
        errors=random.randint(0, 5),
        points=[random.randint(0, 10) for _ in range(random.randint(6, 50))]
    )
    return metrics

@app.get("/recent/acceleration")
def get_acceleration():
    metrics = Metrics(
        top=random.randint(1, 15),
        average=random.randint(0, 10),
        errors=random.randint(0, 5),
        points=[random.randint(0, 10) for _ in range(random.randint(1, 10))]
    )
    return metrics
