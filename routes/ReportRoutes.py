from fastapi import APIRouter, Query
from typing import Union

from controller import DataController

router = APIRouter(prefix="/reports")

@router.get("/mesoPhoto/{:mesoType}", status_code=200)
async def mesoPhoto(mesoType : str):
    response = DataController.getMacroReport(mesoType)
    return response

@router.get("/macroPhoto/{:macroType}", status_code=200)
async def macroPhoto(macroType: str):
    print(macroType)
    response = DataController.getMacroReport(macroType)
    return response

@router.get("/", status_code=200)
async def macroPhoto():
    return "Hello"