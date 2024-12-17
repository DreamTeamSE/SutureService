from fastapi import APIRouter, Depends
from app.DTOs.ControlDTO import ControlDTO
from app.services.ArduinoController.ControllerManager import ControllerManager
from app.services.ArduinoController.ControlService import ControlService
from app.db.Database import Database

router = APIRouter(prefix="/device", tags=["device"])

def get_db():
    db = Database()
    return db

def get_controller_manager(db: Database = Depends(get_db)):
    return ControllerManager(db)

@router.post("/control")
def control_action(
    control: ControlDTO,
    controller_manager: ControllerManager = Depends(get_controller_manager)
):
    controller = ControlService(control)
    return controller.execute() 