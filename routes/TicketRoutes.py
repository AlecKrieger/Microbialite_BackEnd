from fastapi import APIRouter
# from controller.TicketController import 

router = APIRouter(prefix="/tickets")

@router.get("/", status_code=201)
async def test():
    return {"msg": "Just testings"}