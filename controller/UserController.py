from dao import UserDao
from models.user import User, Analyst
import json
import sys


def createUserTables():
    result = UserDao.createTables()
    if (result):
        return {"Msg": "Ticket Tables Created"}
    else:
        return {"Msg": "Could not create tables"}
    
    
def dropUserTables():
    result = UserDao.dropTables()

    if (result):
        return {"Msg": "Ticket Tables dropped"}
    else:
        return {"Msg": "Could not drop tables"}
    
def insertUser(userType: str, data):
    result = UserDao.addUser(userType, data.model_dump())
    if (result):
        return {"Msg": "Created user"}
    else:
        return {"Msg": "Could not create user"}
    
def deleteUser(userType, userID):
    result = UserDao.deleteUser(userType, userID)
    if (result):
        return {"Msg": "Deleted user"}
    else:
        return {"Msg": "Could not delete user"}

def getUsers(userType):
    result = UserDao.getUsers(userType)
    return result

def getUser(userType, userID):
    result = UserDao.getUser(userType, userID)
    return result

def updateUser(userType: str, data : User or Analyst):
    print(getColumnNames("User"))
    result = UserDao.updateUser(userType, data.model_dump())
    if (result):
        return {"Msg": "updated user"}
    else:
        return {"Msg": "Could not update user"}