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

        payload = {"control": control}
        url = f"{domain}/control-device"
        print(url)
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            data = response.json()
            return {"message": data.get("message"), "velocity_list": data.get("velocity_list"), "acceleration_list": data.get("acceleration_list")}
        else:
            logging.error(f"Error controlling device: {response.status_code} - {response.text}")
            return {"message": "Error controlling device"}
