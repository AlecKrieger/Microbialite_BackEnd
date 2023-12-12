from fastapi import APIRouter
from controller.UserController import createUserTables, dropUserTables
from controller.TicketController import createTicketTables, dropTicketTables

router = APIRouter(prefix="/admin")


@router.post("/create_all", status_code=201)
async def create_tables():
    result = [createUserTables(), createTicketTables()]
    return {"response": result}

@router.delete("/drop_all", status_code=201)
async def drop_tables():
    result = [dropTicketTables(), dropUserTables()]
    return {"response": result}
