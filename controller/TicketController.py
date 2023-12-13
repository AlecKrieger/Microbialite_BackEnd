from dao import TicketDao
from models.ticket import Ticket

#TODO Update response statements

def createTicketTables():
    result = TicketDao.createTables()
    if (result):
        return {"Msg": "Ticket tables Created"}
    else:
        return {"Msg": "Could not create Ticket tables"}
    
def dropTicketTables():
    result = TicketDao.dropTables()
    if (result):
        return {"Msg": "Ticket tables dropped"}
    else:
        return {"Msg": "Could not drop Ticket tables"}
    
def getTicketById(ticketID: int):
    result = TicketDao.getTicket(ticketID)
    return {"ticketID": ticketID, "Ticket": result}

def getTickets():
    result = TicketDao.getTickets()
    return {"Tickets" : result}

def getTicketsByUserId(userType, id):
    result = TicketDao.getTicketByUser(userType, id)
    return {"UserType": userType, "ID": id, "Tickets" : result}

def deleteTicket(ticketID: int):
    result = TicketDao.deleteTicket(ticketID)
    if (result):
        return {"Msg": f"Ticket #{ticketID} deleted"}
    else:
        return {"Msg": "Could not drop tables"}
    
def updateTicket(data: Ticket):
    result = TicketDao.updateTicket(data.model_dump())
    if (result):
        return {"Msg": f'Ticket #{data.ticketID} updated'}
    else:
        return {"Msg": "Could not update ticket"}
    
def insertTicket(data : Ticket):
    result = TicketDao.insertTicket(data.model_dump())
    if (result):
        return {"Msg": f'Ticket #{result} created'}
    else:
        return {"Msg": "Could not insert ticket"}
