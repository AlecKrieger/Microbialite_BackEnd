from dao import TicketDao
from models import Tickets

def createTicketTables():
    createTicketTable = Tickets.createTicketTable
    createUserTicketTable = Tickets.createUserTicketTable
    createAnalystTicketTable = Tickets.createAnalystTicketTable

    success = TicketDao.createTables(createTicketTable, createUserTicketTable, createAnalystTicketTable)
    if (success):
        return {"Msg": "Ticket Tables Created", "status_code":200}
    else:
        return {"Msg": "Could not create tables", "status_code":400}
    
    
def dropTicketTables():
    dropTicketTable = Tickets.dropTicketTable
    dropUserTicketTable = Tickets.dropUserTicketTable
    dropAnalystTicketTable = Tickets.dropAnalystTicketTable

    success = TicketDao.dropTables(dropTicketTable, dropUserTicketTable, dropAnalystTicketTable)

    if (success):
        return {"Msg": "Ticket Tables dropped", "status_code":200}
    else:
        return {"Msg": "Could not drop tables", "status_code":400}