from fastapi import APIRouter, Depends, HTTPException
from app.DTOs.device.ControlDTO import ControlDTO
from app.services.ArduinoController.ControlService import ControlService
from app.services.ArduinoController.ControllerManager import ControllerManager
from app.DAOs.MetricDAO import MetricDAO
from app.services.Metrics.MetricsService import MetricsService
from app.db.Database import Database

router = APIRouter(prefix="/device", tags=["device"])

def get_db():
    return Database()

def get_metric_dao(db: Database = Depends(get_db)):
    return MetricDAO(db)

def get_metrics_service(metric_dao: MetricDAO = Depends(get_metric_dao)):
    return MetricsService(metric_dao)

def get_control_manager():
    return ControllerManager()


def get_control_service(control_manager: ControllerManager = Depends(get_control_manager), metric_service: MetricsService = Depends(get_metrics_service)):
    return ControlService(control_manager, metric_service)

@router.post("/control")
def control_action(
    control: ControlDTO,
    control_service: ControlService = Depends(get_control_service)
):
    try:
        return control_service.execute_control_action(control)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error Controlling Device : {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error : {e}")
