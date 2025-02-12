from typing import Any
from app.DTOs.metrics.MetricsDTO import MetricsDTO
from app.DTOs.metrics.CalculatedMetricsDTO import CalculatedMetricsDTO
import logging

class MetricDAO:
    _instance = None

    def __new__(cls, db):
        if cls._instance is None:
            cls._instance = super(MetricDAO, cls).__new__(cls)
            cls._instance.db = db
        return cls._instance

    def insert_metric_into_db(self, metric: MetricsDTO):
        calculated_metrics = metric.calculated_metrics
        if not calculated_metrics:
            raise ValueError("Empty Calculated Metrics")
        
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO metrics (device_id, velocity_list, acceleration_list, top_velocity, top_acceleration, average_velocity, average_acceleration) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        params = (
            metric.device_id,
            metric.velocity_list,
            metric.acceleration_list,
            calculated_metrics.top_velocity,
            calculated_metrics.top_acceleration,
            calculated_metrics.average_velocity,
            calculated_metrics.average_acceleration
        )
        
        cursor.execute(query, params)
        conn.commit()
        self.db.close_connection(conn)
        
       

    def create_metric(self, row):
            calculated_metrics = CalculatedMetricsDTO(top_velocity=row[4], top_acceleration=row[4], average_velocity=row[5], average_acceleration=row[6]) 
            metric = MetricsDTO(
                        device_id=row[0],
                        velocity_list=row[1],
                        acceleration_list=row[2],
                        calculated_metrics=calculated_metrics
                    )
            return metric

    def get_latest_metric(self, device_id: str) -> MetricsDTO:
        row = self.extract_latest_metric_from_db(device_id)
        if not row:
            raise ValueError("Metrics Does Not Exist at Device ID")
        return self.create_metric(row)

           
        

    def extract_latest_metric_from_db(self, device_id : str) -> list:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query =  "SELECT device_id, velocity_list, acceleration_list, top_velocity, top_acceleration, average_velocity, average_acceleration FROM metrics WHERE device_id = %s ORDER BY timestamp DESC LIMIT 1"
        params = (device_id,)
        cursor.execute(query, params)
        row = cursor.fetchone()
        self.db.close_connection(conn)
        return row
          
        
        

    def build_metrics_list(self, rows : list[Any]) -> list[MetricsDTO]:
        metrics_list = []
        for row in rows:
            metrics = self.create_metric(row)
            metrics_list.append(metrics)
        return metrics_list
    
    def get_all_metrics(self, device_id: str) -> list[MetricsDTO]:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = "SELECT device_id, velocity_list, acceleration_list, top_velocity, top_acceleration, average_velocity, average_acceleration FROM metrics WHERE device_id = %s"
            params = (device_id,)
            cursor.execute(query, params)
            rows = cursor.fetchall()
            self.db.close_connection(conn)
            metrics_list = self.build_metrics_list(rows)
            return metrics_list
