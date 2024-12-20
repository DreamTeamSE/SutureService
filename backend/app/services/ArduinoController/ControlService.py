from app.services.ArduinoController.ControllerManager import ControllerManager
from app.services.Metrics.MetricManager import MetricManager
from app.DTOs.device.DeviceMetricsDTO import DeviceMetricsDTO
from app.DTOs.device.ControlDTO import ControlDTO
import httpx

class ControlService:
    def __init__(self, controller_manager: ControllerManager, metric_manager: MetricManager):
        self.controller_manager = controller_manager
        self.metric_manager = metric_manager

    def execute_control_action(self, control: ControlDTO):
        try:
            device_domain = self._create_domain(control.device_id)
            response_data = self.execute_given_device_domain(device_domain, control.action)
            extraced_metrics = self._extract_device_metrics(response_data)
            user_metrics = self.metric_manager.create_metric(control.email, extraced_metrics)
            self.metric_manager.save_metric(user_metrics)
        except Exception as e:
            error_details = f"An error occurred: {str(e)}"
            return {"message": error_details, "error": str(e)}


    def execute_given_device_domain(self, domain, action):
        try:
            response = httpx.post(domain, json={"action": action})
            return response.json()
        except httpx.HTTPStatusError as http_err:
            return {"message": "HTTP error occurred", "error": str(http_err)}
        except Exception as e:
            error_details = f"An error occurred: {str(e)}"
            return {"message": error_details, "error": str(e)}

    def _create_domain(self, device_id):
        address = self.controller_manager.getAddr(device_id)
        return f"{address}/device/control"

    def _extract_device_metrics(self, response):
        velocity_list = response["metrics"]["velocity_list"]
        acceleration_list = response["metrics"]["acceleration_list"]
        return DeviceMetricsDTO(velocity_list=velocity_list, acceleration_list=acceleration_list)