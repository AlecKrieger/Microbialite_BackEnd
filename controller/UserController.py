from dao import UserDao
from models.user import User, Analyst


def createUserTables():
    result = UserDao.createTables()
    if (result):
        return {"Msg": "User and Analyst tables Created"}
    else:
        return {"Msg": "Could not create User and Analyst tables"}
    
    
def dropUserTables():
    result = UserDao.dropTables()

    if (result):
        return {"Msg": "User and Analyst tables dropped"}
    else:
        return {"Msg": "Could not drop User and Analyst tables"}
    
def insertUser(userType: str, data):
    result = UserDao.addUser(userType, data.model_dump())
    message = "Could not insert " + userType
    if (result):
        message = "Inserted " + userType
    return {"Msg": message}
    
def deleteUser(userType, userID):
    result = UserDao.deleteUser(userType, userID)
    message = "Could not delete " + userType
    if (result):
        message = "Deleted " + userType
    return {"Msg": message}

def getUsers(userType):
    result = UserDao.getUsers(userType)
    return result

def getUser(userType, userID):
    result = UserDao.getUser(userType, userID)
    return result

def updateUser(userType: str, data : User or Analyst):
    print(getColumnNames("User"))
    result = UserDao.updateUser(userType, data.model_dump())
    message = "Could not update " + userType
    if (result):
        message = "Updated " + userType
    return {"Msg": message}
