from app.DTOs.MetricsDTO import MetricsDTO
from app.DTOs.DeviceMetricsDTO import DeviceMetricsDTO

class Response:
    def __init__(self, status, message, metrics=None):
        self.status = status
        self.message = message
        self.metrics = metrics

    def to_dict(self):
        return {
            "status": self.status,
            "message": self.message,
            "metrics": self.metrics
        }

class MetricManager:
    def __init__(self, db):
        self.db = db

    def save_metric(self, metric: MetricsDTO):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO metrics (email, velocity_list, acceleration_list, top_velocity, top_acceleration, average_velocity, average_acceleration) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (metric.email, metric.velocity_list, metric.acceleration_list, metric.top_velocity, metric.top_acceleration, metric.average_velocity, metric.average_acceleration)
            )
            conn.commit()
            return Response("success", "Metric saved successfully", metric)
        except Exception as e:
            print(f"Error occurred while saving metric: {e}")
            return Response("error", str(e))
        finally:
            if conn:
                self.db.close_connection(conn)

    def create_metric(self, email, device_metric: DeviceMetricsDTO):
        try:
            top_velocity = max(device_metric.velocity_list)
            top_acceleration = max(device_metric.acceleration_list)
            average_velocity = round(sum(device_metric.velocity_list) / len(device_metric.velocity_list), 2)
            average_acceleration = round(sum(device_metric.acceleration_list) / len(device_metric.acceleration_list), 2)
            metric = MetricsDTO(
                email=email,
                velocity_list=device_metric.velocity_list,
                acceleration_list=device_metric.acceleration_list,
                top_velocity=top_velocity,
                top_acceleration=top_acceleration,
                average_velocity=average_velocity,
                average_acceleration=average_acceleration
            )
            return metric
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error occurred while creating metric: {e}")
            return None

    def get_latest_metric(self, email: str):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT email, velocity_list, acceleration_list, top_velocity, top_acceleration, average_velocity, average_acceleration FROM metrics WHERE email = %s ORDER BY timestamp DESC LIMIT 1",
                (email,)
            )
            row = cursor.fetchone()
            if row:
                metric = MetricsDTO(
                    email=row[0],
                    velocity_list=row[1],
                    acceleration_list=row[2],
                    top_velocity=row[3],
                    top_acceleration=row[4],
                    average_velocity=row[5],
                    average_acceleration=row[6]
                )
                return metric
            else:
                return None
        except Exception as e:
            print(f"Error occurred while retrieving metric: {e}")
            return None
        finally:
            if conn:
                self.db.close_connection(conn)

    def get_all_metrics(self, email: str):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT email, velocity_list, acceleration_list, top_velocity, top_acceleration, average_velocity, average_acceleration FROM metrics WHERE email = %s", (email,))
            rows = cursor.fetchall()
            metrics = [MetricsDTO(
                email=row[0],
                velocity_list=row[1],
                acceleration_list=row[2],
                top_velocity=row[3],
                top_acceleration=row[4],
                average_velocity=row[5],
                average_acceleration=row[6]
            ) for row in rows]
            return metrics
        except Exception as e:
            print(f"Error occurred while retrieving metrics: {e}")
            return None
        finally:
            if conn:
                self.db.close_connection(conn)
