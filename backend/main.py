from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from DTOs.Metrics import Metrics

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}

@app.get("/recent/velocity")
def get_velocity():
    metrics = Metrics(5, 0, 1, [1, 2, 3, 4, 5])
    return metrics

@app.get("/recent/acceleration")
def get_acceleration():
    metrics = Metrics(10, 0, 1, [1, 2, 3, 4, 4, 0, 0, 0])
    return metrics
