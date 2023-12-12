from fastapi import APIRouter
# from controller.UserController import 

userRouter = APIRouter(prefix="/user")
analystRouter = APIRouter(prefix="/analyst")

@userRouter.get("/", status_code=201)
async def test():
    return {"msg": "Just testings"}