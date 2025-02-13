import logging
from time import sleep
from random import randint


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