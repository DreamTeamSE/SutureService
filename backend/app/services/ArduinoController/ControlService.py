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

    def handle_device_stopped(self, email : str, device_metrics : DeviceMetricsDTO):
        extracted_metrics = self._extract_device_metrics(device_metrics)
        user_metrics = self.metrics_service.create_metrics(email, extracted_metrics)
        self.metrics_service.save_metrics(user_metrics)
        return {"message": "Metrics were Collected and Saved", "metrics": user_metrics}
    
       
    def execute_control_action(self, control: ControlDTO) -> DeviceMetricsDTO:
        device_domain = self._create_domain(control.device_id)
        device_response = self.execute_given_device_domain(device_domain, control.action)

        if not device_response or not device_response["metrics"]:
            raise ValueError(f"While preforming this action {control.action}, An error occured while executing the action")
        
        device_metrics = device_response["metrics"]

        if control.action == "stop":
            return self.handle_device_stopped(control.email, device_metrics)
        return device_metrics

    

    def execute_given_device_domain(self, domain : str, action : str) -> dict:
        try:
            response = httpx.post(domain, json={"action": action})
            return response.json()
        except httpx.HTTPStatusError as http_err:
            raise ValueError("Failed to Reach Device Address")

    def _create_domain(self, device_id : str) -> str:
        address = self.controller_manager.getAddr(device_id)
        return f"{address}/device/control"

    def _extract_device_metrics(self, device_metrics : DeviceMetricsDTO) -> DeviceMetricsDTO:
        if not device_metrics["velocity_list"]:
            raise ValueError("Device Velocity List Is Empty")
        if not device_metrics["acceleration_list"]:
            raise ValueError("Device Acceleration List Is Empty")
        
        velocity_list = device_metrics["velocity_list"]
        acceleration_list = device_metrics["acceleration_list"]
        return DeviceMetricsDTO(velocity_list=velocity_list, acceleration_list=acceleration_list)
