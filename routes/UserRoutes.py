from fastapi import APIRouter
from models.user import User, Analyst
from controller import UserController

userRouter = APIRouter(prefix="/user")
analystRouter = APIRouter(prefix="/analyst")

@userRouter.put("/", status_code=200)
async def insertUser(user: User):
    response = UserController.insertUser("user", user)
    return {"Msg": response}

@userRouter.delete("/{id}", status_code=200)
async def deleteUser(id: int):
    response = UserController.deleteUser("user", id)
    return {"Msg": response}

@userRouter.get("/", status_code=200)
async def getAllUsers():
    response = UserController.getUsers("user")
    return {"Users": response}

@userRouter.get("/{id}", status_code=200)
async def getAllUsers(id: int):
    response = UserController.getUser("user", id)
    return {"User": response}

@userRouter.patch("/", status_code=200)
async def updateUser(user: User):
    response = UserController.updateUser("user", user)
    return {"Msg": response}

@analystRouter.put("/", status_code=200)
async def insertAnalyst(analyst: Analyst):
    response = UserController.insertUser("analyst", analyst)
    return {"Msg": response}

@analystRouter.delete("/{id}", status_code=200)
async def deleteAnalyst(id: int):
    response = UserController.deleteUser("analyst", id)
    return {"Msg": response}

@analystRouter.get("/", status_code=200)
async def getAllAnalysts():
    response = UserController.getUsers("analyst")
    return {"Analyst": response}

@analystRouter.get("/{id}", status_code=200)
async def getAnalyst(id: int):
    response = UserController.getUser("analyst", id)
    return {"Analyst": response}

@userRouter.patch("/", status_code=200)
async def updateAnalyst(analyst: Analyst):
    response = UserController.updateUser("analyst", analyst)
    return {"Msg": response}