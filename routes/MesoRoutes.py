from fastapi import APIRouter, Query
from typing import Union

from models.mesostructure import Mesostructure, Mesostructure_Photo
from models.user import Analyst

from controller import DataController

router = APIRouter(prefix="/meso")


# @router.put("/", status_code=200)
# async def insertWaypoint(analyst: Analyst, waypoint: Waypoint):
#     reqItems = {"analyst": analyst, "waypoint": waypoint}
#     response = DataController.insert(analyst, waypoint)
#     return reqItems

@router.put("/{id}", status_code=200)
async def insert(id: int, mesostructure: Mesostructure):
    print(mesostructure)
    response = DataController.insertEntry(id, mesostructure)
    return response

@router.delete("/{id}", status_code=200)
async def delete(id: int):
    response = DataController.deleteEntry("mesostructure", id)
    return response

@router.get("/", status_code=200)
async def getAll():
    response = DataController.getEntries("mesostructure")
    return response

@router.get("/{id}", status_code=200)
async def get(id: int):
    response = DataController.getEntryByID("mesostructure", id)
    return response

@router.patch("/", status_code=200)
async def update(analyst: Analyst, mesostructure: Mesostructure):
    response = DataController.update(mesostructure)
    return {"Msg": response}

@router.put("/photo/{id}", status_code=200)
async def insertPhoto(id: int, mesostructure_Photo: Mesostructure_Photo):
    response = DataController.insertEntry(id, mesostructure_Photo)
    return response

@router.get("/photo/{id}", status_code=200)
async def getPhoto(id: int):
    response = DataController.getEntryByID("mesostructure_Photo", id)
    return response

@router.delete("/photo/{id}", status_code=200)
async def deletePhoto(id: int):
    response = DataController.deleteEntry("mesostructure_Photo", id)
    return response
