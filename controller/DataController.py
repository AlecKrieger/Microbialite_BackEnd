from dao import DataDao
import sys
from models.user import User, Analyst
from models.waypoint import Waypoint
from models.macrostructure import Macrostructure, Macrostructure_Photo
from models.thinsection import Thin_Section, Thin_Section_Photo
from models.mesostructure import Mesostructure, Mesostructure_Photo

from pydantic import BaseModel


#TODO Create methods in comments:
#Create data tables
def createDataTables():
    result = DataDao.createTables()
    if (result):
        return "Data tables created"
    else:
        return "Could not create data tables"

#drop data table
def dropDataTables():
    result = DataDao.dropTables()
    if (result):
        return "Data tables dropped"
    else:
        return "Could not drop data tables"

#Get data row by ID
def getEntryByID(entryType: str, id: int):
    entry = DataDao.getEntryByID(entryType, id)
    model = getattr(sys.modules[__name__], entryType[0].upper() + entryType[1:])
    return entry

#Get all tables
def getEntries(entryType: id):
    entryList = DataDao.getEntries(entryType)
    return entryList

#Insert record
# def insertEntry(analyst: Analyst, data: BaseModel):
#     id = Analyst.analystID
#     dataType = data.__class__.__name__
#     dataKey = DataDao.addEntry(id, dataType, data.model_dump())
#     return dataKey

def insertEntry(id, data: BaseModel):
    dataType = data.__class__.__name__
    print(dataType)
    dataKey = None
    if "_Photo" in dataType:
        dataKey = DataDao.insertPhoto(dataType, data.model_dump(), id)
    else:
        dataKey = DataDao.addEntry(dataType, data.model_dump(), id)

    return dataKey

#Update record
def updateEntry(analyst: Analyst, data: BaseModel):
    id = Analyst.analystID
    dataType = data.__class__.__name__
    dataKey = DataDao.updateEntry(id, dataType, data.model_dump())
    return dataKey

#Delete record
def deleteEntry(dataType, id: int):
    result = DataDao.deleteEntry(dataType, id)
    return result

def getMacroReport():
    result = DataDao.getMacroReport(macroType)
    return result

def getMesoReport(mesoType):
    result = DataDao.getMesoReport(mesoType)
    return result

def filterWayptHSF():
    result = DataDao.filterWayptHSF()
    return result

def filterWayptLPAH():
    result = DataDao.filterWayptLPAH()
    return result