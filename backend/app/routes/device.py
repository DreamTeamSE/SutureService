from fastapi import APIRouter, Depends
from app.DTOs.device.ControlDTO import ControlDTO
from app.services.ArduinoController.ControlService import ControlService
from app.services.ArduinoController.ControllerManager import ControllerManager
from app.services.Metrics.MetricManager import MetricManager
from app.db.Database import Database

router = APIRouter(prefix="/device", tags=["device"])

def get_db():
    return Database()

def get_metric_manager(db: Database = Depends(get_db)):
    return MetricManager(db)

def get_control_manager():
    return ControllerManager()


def get_control_service(control_manager: ControllerManager = Depends(get_control_manager), metric_manager: MetricManager = Depends(get_metric_manager)):
    return ControlService(control_manager, metric_manager)

@router.post("/control")
def control_action(
    control: ControlDTO,
    control_service: ControlService = Depends(get_control_service)
):
    response = control_service.execute(control)
    return response
