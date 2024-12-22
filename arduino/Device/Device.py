import logging
from time import sleep
from random import randint

class Device:
    def __init__(self, id):
        self.is_running = False
        self.is_paused = False
        self.data = self.newCache()
        self.id = id
        
    def start(self):
        self.is_running = True

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    def stop(self):
        self.is_running = False

    def addToCache(self, vel, acc):
        self.data["velocity_list"].append(vel)
        self.data["acceleration_list"].append(acc)
    
    def getData(self):
        return self.data
        

    def newCache(self):
        return {"velocity_list": [], "acceleration_list": []}
    

    
    def run(self):
        sleepVal = 1
        while self.is_running:
            randomVel = round(randint(1, 10) + randint(0, 99) / 100, 2)
            randomAcc = round(randint(1, 10) + randint(0, 99) / 100, 2)
            self.addToCache(randomVel, randomAcc)
            while self.is_paused and self.is_running:
                sleep(sleepVal)
            sleep(sleepVal)