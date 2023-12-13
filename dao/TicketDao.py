import MySQLdb
from dao.connector import connectToDB
from dao.queries import Tickets

LASTINSERTQUERY = "SELECT LAST_INSERT_ID();"

def createTables():
    createTicketTable = Tickets.createTicketTable
    # createUserTicketTable = Tickets.createUserTicketTable
    # createAnalystTicketTable = Tickets.createAnalystTicketTable

    result = False
    conn = connectToDB()
    try:
        cursor = conn.cursor()

        cursor.execute(createTicketTable)
        # cursor.execute(createUserTicketTable)
        # cursor.execute(createAnalystTicketTable)

        result = True
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def dropTables():
    dropTicketTable = Tickets.dropTicketTable
    # dropUserTicketTable = Tickets.dropUserTicketTable
    # dropAnalystTicketTable = Tickets.dropAnalystTicketTable

    result = False
    conn = connectToDB()
    try:
        cursor = conn.cursor()

        # cursor.execute(dropAnalystTicketTable)
        # cursor.execute(dropUserTicketTable)
        cursor.execute(dropTicketTable)


        result = True
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def getTicket(ticketId):
    result = None
    conn = connectToDB()
    query = Tickets.getTicketsByID.format(ticketID = ticketId)
    try:
        cursor = conn.cursor()

        cursor.execute(query)

        ticket = cursor.fetchall()

        result = ticket
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def getTicketByUser(userType: str, id: int):
    query = None
    if (userType == "user"):
       query = Tickets.getTicketsByUser.format(userID = id)
    elif (userType == "analyst"):
        query = Tickets.getTicketsByAnalyst.format(analystID = id)
    else:
        return None
    
    result = None
    conn = connectToDB()

    try:
        cursor = conn.cursor()

        cursor.execute(query)

        ticket = cursor.fetchall()

        result = ticket
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def getTickets():
    result = None
    conn = connectToDB()
    query = Tickets.getTickets
    try:
        cursor = conn.cursor()

        cursor.execute(query)

        ticket = cursor.fetchall()

        result = ticket
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def insertTicket(data: dict):
    result = None
    conn = connectToDB()
    query = Tickets.insertTicket.format(**data)
    print(query)
    try:
        cursor = conn.cursor()

        cursor.execute(query)
        cursor.execute(LASTINSERTQUERY)
        ticketID = cursor.fetchall()
        print(ticketID)
        # cursor.execute(query2)
        # cursor.execute(query3)

        result = ticketID
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result


def updateTicket(data):
    result = None
    conn = connectToDB()
    query = Tickets.updateTicket.format(**data)
    try:
        cursor = conn.cursor()

        cursor.execute(query)
        
        result = True
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result


def deleteTicket(ticketId):
    result = None
    conn = connectToDB()
    query = Tickets.deleteTicketByID.format(ticketID = ticketId)
    try:
        cursor = conn.cursor()

        cursor.execute(query)

        result = True
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result