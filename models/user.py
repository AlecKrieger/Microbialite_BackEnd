from pydantic import BaseModel

class User(BaseModel):
    userID: int
    firstName: str
    lastName: str

class Analyst(BaseModel):
    userID: int
    firstName: str
    lastName: str