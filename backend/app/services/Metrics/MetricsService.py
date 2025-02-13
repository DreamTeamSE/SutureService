import logging

from fastapi import HTTPException
from app.DTOs.device.DeviceMetricsDTO import DeviceMetricsDTO
from app.DTOs.metrics.CalculatedMetricsDTO import CalculatedMetricsDTO
from app.DTOs.metrics.MetricsDTO import MetricsDTO
from app.DAOs.MetricDAO import MetricDAO

class MetricsService():
        def __init__(self, metric_dao : MetricDAO) -> None:
             self.metric_dao = metric_dao
             
        def calculate_metrics(self, device_metric: DeviceMetricsDTO) -> CalculatedMetricsDTO:
            if not device_metric.velocity_list or not device_metric.acceleration_list:
                raise ValueError("Velocity list or acceleration list is empty")
            
            top_velocity = max(device_metric.velocity_list)
            top_acceleration = max(device_metric.acceleration_list)
            average_velocity = round(sum(device_metric.velocity_list) / len(device_metric.velocity_list), 2)
            average_acceleration = round(sum(device_metric.acceleration_list) / len(device_metric.acceleration_list), 2)
        
            calculated_metrics = CalculatedMetricsDTO(
                top_velocity=top_velocity,
                top_acceleration=top_acceleration,
                average_velocity=average_velocity,
                average_acceleration=average_acceleration
            )

            return calculated_metrics
           

        def create_metrics(self, device_id : str, device_metric: DeviceMetricsDTO) -> MetricsDTO:
            calculated_metrics = self.calculate_metrics(device_metric)
            metric = MetricsDTO(
                device_id=device_id,
                velocity_list=device_metric.velocity_list,
                acceleration_list=device_metric.acceleration_list,
                calculated_metrics=calculated_metrics
            )
            return metric
            
        def get_latest_metric(self, device_id : str) -> MetricsDTO:
            metrics = self.metric_dao.get_latest_metric(device_id)
            return metrics
            
        def get_all_metrics(self, device_id : str) -> list[MetricsDTO]:
            rows = MetricDAO.get_all_metrics(device_id)
            return rows    
            
            
        def save_metrics(self, user_metrics : MetricsDTO) -> None:
            self.metric_dao.insert_metric_into_db(user_metrics)
            logging.info("Metrics were Saved")