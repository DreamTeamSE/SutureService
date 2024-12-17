from app.services.Controller.ControllerManager import ControllerManager
from app.services.Metrics.MetricManager import MetricManager
from app.DTOs.DeviceMetricsDTO import DeviceMetrics

import httpx

class ControlService:

    def __init__(self, control):
        self.control = control
        self.controllerManager = ControllerManager()
        self.metricManager = MetricManager()

    def execute(self):
        domain = self.__createDomain(self.control.deviceID)
        try:
            res = self.executeAction(domain, self.control.action)
            return self.__handleResponse(res)
        except httpx.HTTPStatusError as http_err:
            return self.__errorResponse(500, "HTTP error occurred", str(http_err))
        except Exception as e:
            return self.__errorResponse(500, "An error occurred", str(e))

    def __handleResponse(self, res):
        print(res)
        if res.get("status_code") != 200:
            return self.__errorResponse(res.get("status_code", 500), "Error in response", res.get("error", "Unknown error"))
        if self.control.action != "stop":
            return {"status_code": 200, "message": "No metric data", "metric": None}
        velocityList = res["metrics"]["velocityList"]
        accelerationList = res["metrics"]["accelerationList"]
        print(velocityList, accelerationList)
        deviceMetric = DeviceMetrics(velocityList=velocityList, accelerationList=accelerationList)
        print(velocityList, accelerationList)
        metric = self.metricManager.createMetric(self.control.email, deviceMetric)
        print(metric)
        self.metricManager.saveMetric(metric)
        return {"status_code": 200, "message": "Metric processed successfully", "metric": metric}
    
    def executeAction(self, domain, action):
        try:
            response = httpx.post(domain, json={"action": action})
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return self.__errorResponse(500, "HTTP error occurred", str(http_err))
        except Exception as e:
            print(f"An error occurred: {e}")
            return self.__errorResponse(500, "An error occurred", str(e))

    def __createDomain(self, deviceID):
        addr = self.controllerManager.getAddr(deviceID)
        path = "device/control"
        return addr + "/" + path

    def __errorResponse(self, status_code, message, error):
        return {"status_code": status_code, "message": message, "metric": None, "error": error}