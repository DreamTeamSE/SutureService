import logging
from app.services.ArduinoController.ControllerManager import ControllerManager
from app.services.Metrics.MetricsService import MetricsService
from app.DTOs.device.DeviceMetricsDTO import DeviceMetricsDTO
from app.DTOs.device.ControlDTO import ControlDTO
import httpx

class ControlService:
    def __init__(self, controller_manager: ControllerManager, metrics_service: MetricsService):
        self.controller_manager = controller_manager
        self.metrics_service = metrics_service

    def handle_device_stopped(self, device_id : str, device_metrics : DeviceMetricsDTO):
        extracted_metrics = self._extract_device_metrics(device_metrics)
        user_metrics = self.metrics_service.create_metrics(device_id, extracted_metrics)
        self.metrics_service.save_metrics(user_metrics)
        return {"message": "Metrics were Collected and Saved"}
    
       
    def execute_control_action(self, control: ControlDTO) -> dict:
        device_domain = self._create_domain(control.device_id)
        device_response = self.execute_given_device_domain(device_domain, control.control)
        if control.control != "stop":
            return device_response.json()
        return self.handle_device_stopped(control.device_id, device_response)
   

    

    def execute_given_device_domain(self, domain: str, control: str) -> dict:
        try:
            response = self.controller_manager.control_device(domain, control)
            return response
        except httpx.HTTPStatusError as e:
            raise ValueError(f"Failed to Reach Device Address: {e.response.text}")

    def _create_domain(self, device_id : str) -> str:
        address = self.controller_manager.getAddr(device_id)
        return f"{address}"

    def _extract_device_metrics(self, device_response : dict) -> DeviceMetricsDTO:
        metrics = device_response.json()["metrics"]
        velocity_list = metrics["velocity_list"]
        acceleration_list = metrics["acceleration_list"]
        return DeviceMetricsDTO(velocity_list=velocity_list, acceleration_list=acceleration_list)
