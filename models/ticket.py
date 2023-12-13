from pydantic import BaseModel

class Ticket(BaseModel):
    ticketID : int
    dateInputed: str
    ticketDescription : str
    status : str
    userID : int
    analystID : int