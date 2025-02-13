import logging
import httpx
from fastapi import HTTPException
from app.exceptions.device_exceptions import InternalServerError


class DeviceRepository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DeviceRepository, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def control_device(self, domain: str, control: str) -> dict:
        url = f"{domain}/control-device/{control}"
        logging.info(f"{url} has been requested with {control} action")
        try:
            response = httpx.post(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            logging.error(f"HTTP error occurred: {exc.response.status_code} - {exc.response.text}")
            raise HTTPException(status_code=exc.response.status_code, detail=exc.response.text)
        except httpx.RequestError as exc:
            logging.error(f"An error occurred while requesting {exc.request.url!r}: {exc}")
            raise InternalServerError("Application has an internal server error: Please debug the application manually")
        except Exception as exc:
            logging.error(f"An unexpected error occurred: {exc}")
            raise InternalServerError("Application has an internal server error: Please debug the application manually")
