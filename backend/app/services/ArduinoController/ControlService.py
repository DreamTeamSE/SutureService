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
            return self._error_response(500, "HTTP error occurred", str(http_err))
        except Exception as e:
            return self._error_response(500, "An error occurred", str(e))

    def _handle_response(self, response, control):
        print(response)
        if response.get("status_code") != 200:
            return self._error_response(response.get("status_code", 500), "Error in response", response.get("error", "Unknown error"))
        if control.action != "stop":
            return {"status_code": 200, "message": "No metric data", "metric": None}
        
        velocity_list = response["metrics"]["velocity_list"]
        acceleration_list = response["metrics"]["acceleration_list"]

        print(velocity_list, acceleration_list)
        device_metric = DeviceMetricsDTO(velocity_list=velocity_list, acceleration_list=acceleration_list)
        print(velocity_list, acceleration_list)
        metric = self.metric_manager.create_metric(control.email, device_metric)
        print(metric)
        self.metric_manager.save_metric(metric)
        return {"status_code": 200, "message": "Metric processed successfully", "metric": metric}
    
    def execute_action(self, domain, action):
        try:
            response = httpx.post(domain, json={"action": action})
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return self._error_response(500, "HTTP error occurred", str(http_err))
        except Exception as e:
            print(f"An error occurred: {e}")
            return self._error_response(500, "An error occurred", str(e))

    def _create_domain(self, device_id):
        address = self.controller_manager.getAddr(device_id)
        path = "device/control"
        domain = address + "/" + path
        print(domain)
        return domain

    def _error_response(self, status_code, message, error):
        return {"status_code": status_code, "message": message, "metric": None, "error": error}