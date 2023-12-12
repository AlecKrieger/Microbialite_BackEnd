from fastapi import APIRouter
from controller.UserController import createTables, dropTables

userRouter = APIRouter(prefix="/user")
analystRouter = APIRouter(prefix="/analyst")

@userRouter.post("/create/", status_code=201)
async def create_tables():
    result = createTables()
    return {"response": result}

@userRouter.delete("/drop/", status_code=201)
async def drop_tables():
    result = dropTables()
    return {"response": result}

@userRouter.get("/", status_code=201)
async def test():
    return {"msg": "Just testings"}