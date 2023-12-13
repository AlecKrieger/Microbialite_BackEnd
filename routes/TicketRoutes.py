from fastapi import APIRouter
from controller import TicketController
from models.ticket import Ticket

router = APIRouter(prefix="/tickets")

@router.get("/{ticketId}", status_code=201)
async def getTicketById(ticketId: int):
    response = TicketController.getTicketById(ticketId)
    return response

@router.get("/users/{id}", status_code=201)
async def getTicketByUserID(ticketId: int):
    response = TicketController.getTicketsByUserId("user", ticketId)
    return response

@router.get("/", status_code=201)
async def getTicket():
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
async def deleteTicket(ticketID: str):
    response = TicketController.deleteTicket(ticketID)
    return response