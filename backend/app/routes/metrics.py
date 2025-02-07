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


@router.get("/get/recent")
def get_latest_metric(
    email: str,
    metric_service: MetricsService = Depends(get_metrics_service)
):
    try:
        metric = metric_service.get_latest_metric(email)
        if not metric:
            return {"message": "Metric was empty", "metrics": metric}
        return {"message": "Metric retrieved successfully", "metrics": metric}
    except ValueError as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=400, detail=f"Error Getting Latest Metric: {e}")
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")

@router.get("/get/all")
def get_all_metrics(
    email: str,
    metric_service: MetricsService = Depends(get_metrics_service)
):
    try:
        metrics = metric_service.get_all_metrics(email)
        if not metrics:
            logging.warning("Metrics were empty")
            return {"message": "Metrics were empty", "metrics_list": metrics}
        return {"message": "Metrics retrieved successfully", "metrics_list": metrics}
    except ValueError as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=404, detail=f"Error Retrieving All Metrics : {e}")
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal Server Error : {e}")
