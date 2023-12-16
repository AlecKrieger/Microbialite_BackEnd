from fastapi import APIRouter
from controller.UserController import createUserTables, dropUserTables
from controller.TicketController import createTicketTables, dropTicketTables
from controller.DataController import createDataTables, dropDataTables

router = APIRouter(prefix="/admin")


@router.post("/create_all", status_code=201)
async def create_tables():
    result = [createUserTables(), createTicketTables(), createDataTables()]
    return result

@router.delete("/drop_all", status_code=201)
async def drop_tables():
    result = [dropDataTables(), dropTicketTables(), dropUserTables()]
    return result
