import MySQLdb
from dao.connector import connectToDB
from dao.queries import Waypoints as w
from dao.queries import Macrostructures as ma
from dao.queries import Mesostructures as me
from dao.queries import ThinSection as th
from dao.queries import ReportQueries as r

createTableQueries = [w.createDataTable, w.createSearchesTable, w.createAddTable, 
                      ma.createDataTable, ma.createSearchesTable, ma.createAddTable, ma.createPhotoTable,
                      me.createDataTable, me.createSearchesTable, me.createAddTable, me.createPhotoTable,
                      th.createDataTable, th.createSearchesTable, th.createAddTable, th.createPhotoTable]

dropTableQueries = [w.dropDataTable, ma.dropDataTable, me.dropDataTable, th.dropDataTable,
                    w.dropAddTable, ma.dropAddTable, me.dropAddTable, th.dropAddTable,
                    w.dropSearchesTable, ma.dropSearchesTable, me.dropSearchesTable, th.dropSearchesTable,
                    ma.dropPhotoTable, me.dropPhotoTable, th.dropPhotoTable]

insertQueries = {"waypoint": w.insertData, "thin_Section": th.insertData, 
                    "macrostructure": ma.insertData, "mesostructure": me.insertData}

insertPhotoQueries = {"thin_Section_Photo": th.insertPhoto, "macrostructure_Photo": ma.insertPhoto, "mesostructure_Photo": me.insertPhoto}

updateQueries = {"waypoint": w.updateData, "thin_Section": th.updateData, 
                    "macrostructure": ma.updateData, "mesostructure": me.updateData}

LASTINSERTQUERY = "SELECT LAST_INSERT_ID();"

#TODO Create insert and update functions, create get photo and delete for photofunctions

# createTableQueries
def createTables():
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

def dropTables():
    result = False
    conn = connectToDB()
    try:
        cursor = conn.cursor()

        for query in dropTableQueries:
            cursor.execute(query)

        result = True
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def getEntryByID(entryType: str, entryID: int):
    tableName = ""
    key = entryType[0].lower() + entryType[1:] + "ID"
    if "Photo" in entryType:
        tableName = entryType[0].upper() + entryType[1:]
    else:
        tableName = entryType[0].upper() + entryType[1:] + "_Data"
    query = f"SELECT * FROM {tableName} WHERE {key} = {entryID};"
    conn = connectToDB()
    result = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
        result = r[0] if r else None
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        cursor.close()
        conn.close()
    return result


def getEntries(entryType: str) -> list:
    tableName = ""
    if "Photo" in entryType:
        tableName = entryType[0].upper() + entryType[1:]
    else:
        tableName = entryType[0].upper() + entryType[1:] + "_Data"
    query = f"SELECT * FROM {tableName};"
    conn = connectToDB()
    result = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
        result = r
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        cursor.close()
        conn.close()
    return result

def insertPhoto(entryType, data, analystID):
    tableName = entryType[0].lower() + entryType[1:]
    key = tableName.split("_Photo")[0] + "ID"
    print(tableName)
    query = insertPhotoQueries.get(tableName).format(**data)
    print(query)
    conn = connectToDB()
    result = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.execute(LASTINSERTQUERY)
        key = cursor.fetchall()
        key = key[0][0]
        addToAddData = f"INSERT INTO Add_{entryType}_Data  VALUES ({analystID}, {key}, );"
        cursor.execute(addToAddData)
        result = key
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def addEntry(entryType, data, analystID) -> bool:
    tableName = entryType[0].lower() + entryType[1:]
    print(tableName)
    print(tableName in insertQueries)
    query = insertQueries.get(tableName).format(**data)
    conn = connectToDB()
    result = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.execute(LASTINSERTQUERY)
        key = cursor.fetchall()
        key = key[0][0]
        addToAddData = f"INSERT INTO Add_{entryType}_Data  VALUES ({analystID}, {key});"
        cursor.execute(addToAddData)
        result = key
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def deleteEntry(entryType: str, entryID: int) -> bool:
    key = entryType + "ID"
    if "Photo" in entryType:
        tableName = entryType[0].upper() + entryType[1:]
    else:
        tableName = entryType[0].upper() + entryType[1:] + "_Data"
    query = f"DELETE FROM {tableName} WHERE {key} = {entryID};"
    print(query)
    conn = connectToDB()
    result = False
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

def updateEntry(entryType, data, analystID) -> bool:
    tableName = entryType[0].upper() + entryType[1:]
    query = updateEntry.get(entryType).format(**data)
    key = entryType[0].lower() + entryType[1:] + "ID"
    entryID = data.get(key)
    ifInAddDataQuery = f"SELECT * FROM Add_{entryType}_Data WHERE analystID = {analystID} AND {key} = {entryID};"
    addToAddData = f"INSERT INTO Add_{entryType}_Data  VALUES ({analystID}, {entryID});"
    conn = connectToDB()
    result = True
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.execute(ifInAddDataQuery)
        row = cursor.fetchall()
        if row:
            cursor.execute(addToAddData)
        result = True
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def getAnalystContributions(entryType, analystID) -> list:
    query = f"SELECT * FROM Add_{entryType}_Data WHERE analystID = {analystID};"
    conn = connectToDB()
    result = None
    try:
        cursor = conn.cursor()
        r = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        result = r
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def getContributionsByEntry(entryType, entryID) -> list:
    key = entryType[0].lower() + entryType[1:] + "ID"
    query = f"SELECT * FROM Add_{entryType}_Data WHERE {key} = {entryID};"    
    conn = connectToDB()
    result = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)

        r = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        result = r
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def searchByKeyword(entryType, column, keyword):
    query = f"SELECT * FROM Add_{entryType}_Data WHERE {column} LIKE %{keyword}%;"
    conn = connectToDB()
    result = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()

        result = rows
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        cursor.close()
        conn.close()
    return result    
    
def getMacroReport(macroType):
    query = r.macroPhotosByMacroType.format(macroType = macroType)
    conn = connectToDB()
    result = False
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        r = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        result = r
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def getMacroReport(mesoType):
    query = r.mesoPhotosByMesoType.format(mesoType = mesoType)
    conn = connectToDB()
    result = False
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        r = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        result = r
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def filterWayptHSF():
    query = w.filterWayptHSF
    conn = connectToDB()
    result = False
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        r = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        result = r
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result

def filterWayptLPAH():
    query = w.filterWayptLPAH
    conn = connectToDB()
    result = False
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        r = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        result = r
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        conn.close()
    return result
