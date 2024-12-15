from time import sleep
from random import randint

class Device:
    def __init__(self, id):
        self.is_running = False
        self.is_paused = False
        self.velocity = []
        self.id = id
        
    def start(self):
        self.is_running = True

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    def stop(self):
        self.is_running = False
        return self.velocity

    def addToCache(self, val):
        self.velocity.append(val)
        

    def clearCache(self):
        self.data = []
    

    
    def run(self):
        print(f"Device {self.id} started running")
        while self.is_running:
            try:
                val = randint(1, 10)
                self.addToCache(val)
                print(self.velocity)
                while self.is_paused and self.is_running:
                    sleep(.5)
                sleep(.5)
               
            except Exception as e:
                print(f"Error in device {self.id}: {str(e)}")
                self.stop()
        self.clearCache()