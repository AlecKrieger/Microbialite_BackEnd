from dao import TicketDao
from models.ticket import Ticket

#TODO Standardize response 

def createTicketTables():
    result = TicketDao.createTables()
    if (result):
        return "Ticket tables Created"
    else:
        return "Could not create Ticket tables"
    
def dropTicketTables():
    result = TicketDao.dropTables()
    if (result):
        return "Ticket tables dropped"
    else:
        return "Could not drop Ticket tables"
    
def getTicketById(ticketID: int):
    result = TicketDao.getTicket(ticketID)
    return result

def getTickets():
    result = TicketDao.getTickets()
    return result

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

def getClosedTickets():
    result = TicketDao.getClosedTickets()
    return result
    
def getTicketNames():
    result = TicketDao.getNamedTickets()
    return result
    