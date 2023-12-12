from dao import UserDao
from models import Users
from models import Analysts

def createUserTables():
    createUserTable = Users.createUserTable
    createAnalystTable = Analysts.createAnalystTable

    success = UserDao.createTables(createUserTable, createAnalystTable)
    if (success):
        return {"Msg": "Ticket Tables Created", "status_code":200}
    else:
        return {"Msg": "Could not create tables", "status_code":400}
    
    
def dropUserTables():
    dropUserTable = Users.dropUserTable
    dropAnalystTable = Analysts.dropAnalystTable

    success = UserDao.dropTables(dropUserTable, dropAnalystTable)

    if (success):
        return {"Msg": "Ticket Tables dropped", "status_code":200}
    else:
        return {"Msg": "Could not drop tables", "status_code":400}