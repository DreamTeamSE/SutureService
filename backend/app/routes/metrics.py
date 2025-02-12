import logging
from fastapi import APIRouter, Depends, HTTPException
from app.services.Metrics.MetricsService import MetricsService
from app.DAOs.MetricDAO import MetricDAO
from app.db.Database import Database

router = APIRouter(prefix="/metric", tags=["metric"])

def get_db() -> Database:
    db = Database()
    return db

def get_metric_dao(db: Database = Depends(get_db)) -> MetricDAO:
    return MetricDAO(db)

def get_metrics_service(metric_dao: MetricDAO = Depends(get_metric_dao)) -> MetricsService:
    return MetricsService(metric_dao)

@router.get("/get/recent/{device_id}")
def get_latest_metric(
    device_id: str,
    metric_service: MetricsService = Depends(get_metrics_service)
):
    try:
        metrics = metric_service.get_latest_metric(device_id)
        return {"metrics": metrics}
    except ValueError as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=400, detail=f"Error Getting Latest Metric: {e}")
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")