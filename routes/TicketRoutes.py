from fastapi import APIRouter, Header
from typing import Union

from typing_extensions import Annotated
from controller import TicketController
from models.ticket import Ticket

router = APIRouter(prefix="/tickets")

@router.get("/closed/", status_code=201)
async def getClosedTicket():
    response = TicketController.getClosedTickets()
    return response

@router.get("/names", status_code=201)
async def getTicketNames():
    response = TicketController.getTicketNames()
    return response

@router.get("/{ticketId}", status_code=201)
async def getTicketById(ticketId: int, user_agent: Union[str, None] = Header(default=None)):
    if (user_agent not in {"Intern", "Researcher"}):
        return "Not authorized"
    response = TicketController.getTicketById(ticketId)
    return response

@router.get("/users/{id}", status_code=201)
async def getTicketByUserID(id: int):
    response = TicketController.getTicketsByUserId("user", id)
    return response

@router.get("/analysts/{id}", status_code=201)
async def getTicketByUserID(id: int):
    response = TicketController.getTicketsByUserId("analyst", id)
    return response

@router.get("/", status_code=201)
async def getTicket(user_agent: Union[str, None] = Header(default=None)):
    if (user_agent in {"User", None}):
        return "Not authorized"
    
    response = TicketController.getTickets()
    return response

@router.put("/", status_code=200)
async def insertTicket(ticket: Ticket):
    response = TicketController.insertTicket(ticket)
    return response

@router.patch("/", status_code=200)
async def updateTicket(request: Ticket):
    response = TicketController.updateTicket(request)
    return response

@router.delete("/{ticketID}", status_code=200)
async def deleteTicket(ticketID: str, user_agent: Union[str, None] = Header(default=None)):
    if (user_agent not in {"Intern", "Researcher"}):
        return "Not authorized"
    response = TicketController.deleteTicket(ticketID)
    return response

@router.get("/closed/", status_code=201)
async def getClosedTicket():
    response = TicketController.getClosedTickets()
    return response

@router.get("/names", status_code=201)
async def getTicketNames():
    response = TicketController.getTicketNames()
    return response