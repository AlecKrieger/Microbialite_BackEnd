import MySQLdb
from dao.connector import connectToDB
from dao.queries import Users, Analysts


def createTables():
    success = False
    conn = connectToDB()
    createUserTable = Users.createUserTable
    createAnalystTable = Analysts.createAnalystTable
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

def dropTables():
    dropUserTable = Users.dropUserTable
    dropAnalystTable = Analysts.dropAnalystTable
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

def addUser(userType: int, data):
    query = None
    if (userType == 'user'):
        query = Users.insertUser.format(firstName=data.get("firstName"), 
                                        lastName = data.get("lastName"))
    elif (userType == 'analyst'):
        query = Analysts.insertAnalyst.format(firstName=data.get("firstName"), 
                                        lastName = data.get("lastName"))
    else:
        return None
    conn = connectToDB()
    success = None

    try:
        cursor = conn.cursor()
        cursor.execute(query)

        success = True
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return success


def updateUser():
    pass

#Delete a single user or analyst by ID
def deleteUser(userType, userID):
    query = None
    if (userType == 'user'):
        query = Users.deleteUser.format(userID = userID)
        print(query)
    elif (userType == 'analyst'):
        query = Analysts.deleteAnalyst.format(analystID = userID)
    else:
        return None
    conn = connectToDB()
    success = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)

        success = True
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return success

#Get all users or all analysts
def getUsers(userType):
    query = None
    if (userType == 'user'):
        query = Users.getUsers
        print(query)
    elif (userType == 'analyst'):
        query = Analysts.getAnalysts
    else:
        return None
    conn = connectToDB()
    success = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        users = cursor.fetchall()
        success = users
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return success

#Get a single user or analyst by id
def getUser(userType, userID):
    query = None
    if (userType == 'user'):
        query = Users.getUserByID.format(userID = userID)
        print(query)
    elif (userType == 'analyst'):
        query = Analysts.getAnalysts.format(analystID = userID)
    else:
        return None
    conn = connectToDB()
    success = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        users = cursor.fetchall()
        success = users
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        cursor.close()
        conn.close()
    return success

def updateUser(userType: int, data):
    query = None
    if (userType == 'user'):
        # query = Users.updateUser.format(firstName=data.get("firstName"), 
        #                                 lastName = data.get("lastName"),
        #                                 userID = data.get("userID"))
        query = Users.updateUser.format(**data)
    elif (userType == 'analyst'):
        query = Analysts.updateAnalyst.format(firstName=data.get("firstName"), 
                                        lastName = data.get("lastName"),
                                        analystID = data.get("analystID"))
    else:
        return None
    conn = connectToDB()
    success = None

    try:
        cursor = conn.cursor()
        cursor.execute(query)

        success = True
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return success
