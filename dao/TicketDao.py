import MySQLdb
from .connector import connectToDB

def createTables(createTicketTable, createUserTicketTable, createAnalystTicketTable):
    success = False
    conn = connectToDB()
    try:
        # Create a cursor to interact with the database
        cursor = conn.cursor()

        # Create relevant tables
        cursor.execute(createTicketTable)
        cursor.execute(createUserTicketTable)
        cursor.execute(createAnalystTicketTable)

        success = True

        # # Execute "SHOW TABLES" query
        # cursor.execute("SHOW TABLES")

        # # Fetch all the rows
        # tables = cursor.fetchall()

        # # Print out the tables
        # print("Tables in the database:")
        # for table in tables:
        #     print(table[0])

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
    return success

def dropTables(dropTicketTable, dropAnalystTicketTable, dropUserTicketTable):
    success = False
    conn = connectToDB()
    try:
        cursor = conn.cursor()

        cursor.execute(dropAnalystTicketTable)
        cursor.execute(dropUserTicketTable)
        cursor.execute(dropTicketTable)


        success = True
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return success

def addTicket():
    pass

def updateTicket():
    pass

def deleteTicket(ticketId):
    pass

def getTickets(ticketId):
    pass

def getTicket():
    pass
