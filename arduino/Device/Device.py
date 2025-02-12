import logging
from time import sleep
from random import randint


class MovementGenerator:
    def generateVel():
        return round(randint(1, 10) + randint(0, 99) / 100, 2)
    
    def generateAccel():
        return round(randint(1, 10) + randint(0, 99) / 100, 2)
    




class Cache:
    def __init__(self):
        self.newCache()

    def addToCache(self, vel, acc):
        self.velocity_list.append(vel)
        self.acceleration_list.append(acc)

    def newCache(self):
        self.velocity_list = []
        self.acceleration_list = []
    
    def getMetrics(self):
        metrics = {"velocity_list" : self.velocity_list, "acceleration_list" : self.acceleration_list}
        return metrics

class Device:
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

    def createMetrics(self):
        randomVel = MovementGenerator.generateVel()
        randomAcc = MovementGenerator.generateAccel()
        return (randomVel, randomAcc)
    
    def getMetrics(self):
        return self.cache.getMetrics()
    
    def newCache(self):
        self.cache.newCache()

    
    def run(self):
        sleepVal = 1
        while self.is_running:
            randomVel, randomAcc = self.createMetrics()
            self.cache.addToCache(randomVel, randomAcc)
            while self.is_paused and self.is_running:
                sleep(sleepVal)
            sleep(sleepVal)