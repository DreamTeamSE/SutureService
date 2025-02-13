from concurrent import futures
import logging
import requests




class DeviceRepository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DeviceRepository, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    

    def control_device(self, domain: str, control: str) -> dict:

        url = f"{domain}/control-device/{control}"
        print(url)
        response = requests.post(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 400:
            raise ValueError("Input Error")
        elif response.status_code == 500:
            raise Exception("Debug Application")
        else:
            response.raise_for_status()
