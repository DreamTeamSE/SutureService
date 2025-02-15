import logging
from time import sleep
import requests
import math
from random import randint
import csv
from io import StringIO


class DeviceMetrics:
    def __init__(self, time, x_vel, y_vel, z_vel):
        self.time = time
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.z_vel = z_vel
    
class MovementGenerator:

    """
    This class is responsible for generating random movement data for the device. 
    It provides methods to generate random velocity and acceleration values, which can be used to simulate device movement.
    """

    @staticmethod
    def generate_vel():
        return round(randint(1, 10) + randint(0, 99) / 100, 2)
    
    @staticmethod
    def generate_accel():
        return round(randint(1, 10) + randint(0, 99) / 100, 2)
    

    @staticmethod
    def generate_dummy_velocity_list() -> list:
        velocity_list = []
        for t in range(0, 10001, 100):
            time = t / 1000.0
            x_vel = MovementGenerator.generate_vel()
            y_vel = MovementGenerator.generate_vel()
            z_vel = MovementGenerator.generate_vel()
            velocity_list.append([time, x_vel, y_vel, z_vel])
        return velocity_list
    
    @staticmethod
    def handle_resposne(response) -> list:
            response_text = response["text"]
            csv_file = StringIO(response_text)
            reader = csv.reader(csv_file)
            return list(reader)
    
    @staticmethod
    def fixed_velocity() -> list:
        address = f"htp://172.20.10.1:80/start"
        try:
            response = requests.get(address)
            response.raise_for_status()
            csv_file = MovementGenerator.handle_resposne(response)
            return csv_file

        except requests.HTTPError as e:
            logging.error(f"HTTP error occurred: {e.response.text}")
            return MovementGenerator.generate_dummy_velocity_list()
        except Exception as e:
            logging.error(f"Debug Application: {str(e)}")
            return MovementGenerator.generate_dummy_velocity_list()
    
class Cache:

    """
    The Cache class serves as a temporary storage for velocity and acceleration data. 
    It allows adding new data points and resetting the stored data to its initial state. 
    This class is essential for managing session data during device operation.
    """

    def __init__(self):
        #  self.velocity_list = []
        #  self.acceleration_list = []
        self.new_cache()

    def add_to_cache(self, vel, acc):
        self.velocity_list.append(vel)
        self.acceleration_list.append(acc)

    def new_cache(self):
        self.velocity_list = []
        self.acceleration_list = []
    
    def get_metrics(self):
        metrics = {"velocity_list" : self.velocity_list, "acceleration_list" : self.acceleration_list}
        return metrics

class Device:

    """
    The Device class models a device capable of collecting movement data. 
    It can start, stop, pause, and resume data collection, and it uses a Cache to store the collected metrics. 
    This class integrates various components to simulate a device in operation.
    """
       
    def __init__(self, id):
        self.is_running = False
        self.is_paused = False
        self.cache = Cache()
        self.id = id
        
    def start(self):
        self.is_running = True

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    def stop(self):
        self.is_running = False

    def create_metrics(self):
        random_vel = MovementGenerator.generate_vel()
        random_acc = MovementGenerator.generate_accel()
        return (random_vel, random_acc)
    
    def create_fixed_metrics(self) -> tuple:
        fixed_velocity_list = MovementGenerator.fixed_velocity()
        velocity_magnitude_list = [(v[0], math.sqrt(v[1]**2 + v[2]**2 + v[3]**2)) for v in fixed_velocity_list]

        return (velocity_magnitude_list, velocity_magnitude_list)
    
    def get_metrics(self):
        return self.cache.get_metrics()
    
    def new_cache(self):
        self.cache.new_cache()

    def run(self):
        sleep_val = 1
        while self.is_running:
            random_vel, random_acc = self.create_metrics()
            self.cache.add_to_cache(random_vel, random_acc)
            while self.is_paused and self.is_running:
                sleep(sleep_val)
            sleep(sleep_val)
