from typing import List
from pydantic import BaseModel

class User(BaseModel):
    name: str = ""