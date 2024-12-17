from fastapi import APIRouter, Depends
from app.services.Metrics.MetricManager import MetricManager
from app.db.Database import Database

router = APIRouter(prefix="/metric", tags=["metric"])

def get_db():
    db = Database()
    return db

def get_metric_manager(db: Database = Depends(get_db)):
    return MetricManager(db)

@router.get("/get/recent")
def get_latest_metric(
    email: str,
    metric_manager: MetricManager = Depends(get_metric_manager)
):
    metric = metric_manager.get_latest_metric(email)
    if metric:
        return {"message": "Metric retrieved successfully", "metrics": metric}
    else:
        return {"message": "Metric not found"}

@router.get("/get/all")
def get_all_metrics(
    email: str,
    metric_manager: MetricManager = Depends(get_metric_manager)
):
    metrics = metric_manager.get_all_metrics(email)
    if metrics:
        return {"message": "Metrics retrieved successfully", "metrics_list": metrics}
    else:
        return {"message": "Metrics not found"} 