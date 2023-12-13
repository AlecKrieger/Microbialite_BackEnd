import MySQLdb
from connector import connectToDB
from queries import Waypoints as w
from queries import Macrostructures as ma
from queries import Mesostructures as me
from queries import ThinSection as th

createTableQueries = [w.createWaypointTable, w.createSearchesWaypointTable, w.createAddWaypointTable, 
                      ma.createMacroTable, ma.createAddMacroTable, ma.createSearchesMacroTable, ma.createPhotoTable,
                      me.createMesoTable, me.createAddMesoTable, me.createSearchesMesoTable, me.createPhotoTable,
                      th.createTSTable, th.createAddTSTable, th.createSearchesTSTable, th.createPhotoTable]

dropTableQueries = [w.dropSearchesWaypointTable, w.dropAddWaypointTable, w.dropWaypointTable, 
                    ma.dropAddDataTable, ma.dropSearchesTable, ma.dropPhotoTable, ma.dropDataTable,
                    me.dropAddDataTable, me.dropSearchesTable, me.dropPhotoTable, me.dropDataTable,
                    th.dropAddDataTable, th.dropSearchesTable, th.dropPhotoTable, th.dropDataTable]

getEntryByIDQueries = {}

getEntriesQueries = {}

searchEntriesQueries = {}

searchBySearcherQueries = {}

searchByAdder = {}

insertQueries = {}

deleteQueries = {}

dataTables = {}

LASTINSERTQUERY = "SELECT LAST_INSERT_ID();"

#TODO 

# createTableQueries
def createWaypointTables():
    result = False
    conn = connectToDB()
    try:
        cursor = conn.cursor()

        for query in createTableQueries:
            cursor.execute(query)

        result = True
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def dropWaypointTables():
    result = False
    conn = connectToDB()
    try:
        cursor = conn.cursor()

        for query in createTableQueries:
            cursor.execute(query)

        result = True
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def getEntryByID(entryType: str, entryID: int):
    query = None
    if (entryType in dataTables):
        idName = entryType[0].lower() + entryType[1:] + "ID"
        query = getEntryByIDQueries.get(entryType).format(idName = entryID)
    else:
        return None
    conn = connectToDB()
    result = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        entry = cursor.fetchall()
        result = entry
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        cursor.close()
        conn.close()
    return result

def getEntries(entryType: str):
    query = None
    if (entryType in dataTables):
        query = getEntriesQueries.get(entryType)
    else:
        return None
    conn = connectToDB()
    result = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        entry = cursor.fetchall()
        result = entry
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        cursor.close()
        conn.close()
    return result

def addEntry(entryType, data):
    query = None
    if (entryType in dataTables):
        query = getEntryByIDQueries.get(entryType).format(**data)
    else:
        return None
    conn = connectToDB()
    result = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.execute(LASTINSERTQUERY)

        key = cursor.fetchall()

        result = key
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def deleteEntry(entryType: str, entryID: int):
    query = None
    if (entryType in dataTables):
        idName = entryType[0].lower() + entryType[1:] + "ID"
        query = deleteQueries.get(entryType).format(idName = entryID)
    else:
        return None
    conn = connectToDB()
    result = None
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