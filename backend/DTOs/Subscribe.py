from pydantic import BaseModel

class Subscribe(BaseModel):
    id: int = 0
    userID: int = 0