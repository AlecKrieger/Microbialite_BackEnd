from fastapi import APIRouter, Query
from typing import Union

from models.macrostructure import Macrostructure, Macrostructure_Photo
from models.user import Analyst

from controller import DataController

router = APIRouter(prefix="/macro")

@router.put("/{id}", status_code=200)
async def insert(id: int, macrostructure: Macrostructure):
    response = DataController.insertEntry(id, macrostructure)
    return response

@router.delete("/{id}", status_code=200)
async def delete(id: int):
    response = DataController.deleteEntry("macrostructure", id)
    return response

@router.get("/", status_code=200)
async def getAll():
    response = DataController.getEntries("macrostructure")
    return response

@router.get("/{id}", status_code=200)
async def get(id: int):
    response = DataController.getEntryByID("macrostructure", id)
    return response

@router.patch("/", status_code=200)
async def update(analyst: Analyst, macrostructure: Macrostructure):
    response = DataController.update(macrostructure)
    return {"Msg": response}

@router.put("/photo/{id}/", status_code=200)
async def insertPhoto(id: int, macrostructure_Photo: Macrostructure_Photo):
    response = DataController.insertEntry(id, macrostructure_Photo)
    return "Macrostructure photo added"

@router.delete("/photo/{id}", status_code=200)
async def deletePhoto(id: int):
    response = DataController.deleteEntry("macrostructure_Photo", id)
    return response
