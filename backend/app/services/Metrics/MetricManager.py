from app.db.Database import Database

class MetricManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MetricManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'db'):
            self.db = Database()

    def createMetric(self, metric):
        conn = self.db.getConnection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO metrics (email, velocity_list, acceleration_list, top_velocity, top_acceleration, average_velocity, average_acceleration) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (metric.email, metric.velocity_list, metric.acceleration_list, metric.top_velocity, metric.top_acceleration, metric.average_velocity, metric.average_acceleration)
        )
        conn.commit()
        self.db.closeConnection(conn)
        return metric
