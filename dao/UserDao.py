import MySQLdb
from .connector import connectToDB

def createTables(createUserTable, createAnalystTable):
    success = False
    conn = connectToDB()
    try:
        # Create a cursor to interact with the database
        cursor = conn.cursor()

        # Create relevant tables
        cursor.execute(createUserTable)
        cursor.execute(createAnalystTable)

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

def dropTables(dropUserTable, dropAnalystTable):
    success = False
    conn = connectToDB()
    try:
        cursor = conn.cursor()

        cursor.execute(dropUserTable)
        cursor.execute(dropAnalystTable)

        success = True
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return success

def addUser():
    pass

def updateUser():
    pass

def deleteUser(ticketId):
    pass

def getUsers(ticketId):
    pass

def getUser():
    pass
