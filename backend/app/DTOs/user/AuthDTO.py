from typing import List
from pydantic import BaseModel

class AuthDTO(BaseModel):
    email: str = ""
    password: str = ""