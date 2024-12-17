from app.services.ArduinoController.ControllerManager import ControllerManager
from app.services.Metrics.MetricManager import MetricManager
from app.DTOs.DeviceMetricsDTO import DeviceMetricsDTO
from app.DTOs.ControlDTO import ControlDTO
import httpx

class ControlService:
    def __init__(self, controller_manager: ControllerManager, metric_manager: MetricManager):
        self.controller_manager = controller_manager
        self.metric_manager = metric_manager

    def execute(self, control: ControlDTO):
        domain = self._create_domain(control.device_id)
        try:
            response = self.execute_action(domain, control.action)
            return self._handle_response(response, control)
        except httpx.HTTPStatusError as http_err:
            return Response("error", "HTTP error occurred", error=str(http_err))
        except Exception as e:
            return Response("error", "An error occurred", error=str(e))

    def _handle_response(self, response, control):
        if response.get("status") != "success":
            return Response(response.get("status", "error"), "Error in response", error=response.get("error", "Unknown error"))
        
        if control.action != "stop":
            return Response("success", "No metric data")
        
        device_metric = self._extract_device_metrics(response)
        metric = self.metric_manager.create_metric(control.email, device_metric)
        self.metric_manager.save_metric(metric)
        
        return Response("success", "Metric processed successfully", metrics=metric)

    def execute_action(self, domain, action):
        try:
            response = httpx.post(domain, json={"action": action})
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as http_err:
            return Response("error", "HTTP error occurred", error=str(http_err))
        except Exception as e:
            return Response("error", "An error occurred", error=str(e))

    def _create_domain(self, device_id):
        address = self.controller_manager.getAddr(device_id)
        return f"{address}/device/control"

    def _extract_device_metrics(self, response):
        velocity_list = response["metrics"]["velocity_list"]
        acceleration_list = response["metrics"]["acceleration_list"]
        return DeviceMetricsDTO(velocity_list=velocity_list, acceleration_list=acceleration_list)

class Response:
    def __init__(self, status="error", message="An error occurred", metrics=None, error=None):
        self.status = status
        self.message = message
        self.metrics = metrics
        self.error = error

    def to_dict(self):
        return {
            "status": self.status,
            "message": self.message,
            "metrics": self.metrics,
            "error": self.error
        }