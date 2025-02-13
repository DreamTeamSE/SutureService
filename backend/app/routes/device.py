import logging
from fastapi import APIRouter, Depends, HTTPException
from app.DTOs.device.ControlDTO import ControlDTO
from app.services.ArduinoController.ControlService import ControlService
from app.services.ArduinoController.ControllerManager import ControllerManager
from app.DAOs.MetricDAO import MetricDAO
from app.services.Metrics.MetricsService import MetricsService
from app.db.Database import Database
from app.repository.DeviceRepository import DeviceRepository
import httpx
router = APIRouter(prefix="/device", tags=["device"])



def get_db():
    return Database()

def get_metric_dao(db: Database = Depends(get_db)):
    return MetricDAO(db)

def get_metrics_service(metric_dao: MetricDAO = Depends(get_metric_dao)):
    return MetricsService(metric_dao)


def get_device_repository():
    return DeviceRepository()


def get_control_manager(device_repo : DeviceRepository = Depends(get_device_repository)):
    return ControllerManager(device_repo)

def get_control_service(control_manager: ControllerManager = Depends(get_control_manager), metric_service: MetricsService = Depends(get_metrics_service)):
    return ControlService(control_manager, metric_service)

@router.post("/control")
def control_action(
    control: ControlDTO,
    control_service: ControlService = Depends(get_control_service)
):
    try:
        logging.info(f"Performing Action '{control.control}' on '{control.device_id}'")
        control_service.execute_control_action(control)
        logging.info(f"Finished Action '{control.control}' on '{control.device_id}'")
    except ValueError as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=e.response.status_code, detail=f"Error Controlling Device: {str(e)}")
    except httpx.HTTPStatusError as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=e.response.status_code, detail=f"Error Accessing Arduino at provided Address: {e.response.text}")
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}, Debug Application Manually")
