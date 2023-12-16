from fastapi import APIRouter, Query
from typing import Union

from models.thinsection import Thin_Section, Thin_Section_Photo
from models.user import Analyst

from controller import DataController

router = APIRouter(prefix="/thin_section")


# @router.put("/", status_code=200)
# async def insertWaypoint(analyst: Analyst, waypoint: Waypoint):
#     reqItems = {"analyst": analyst, "waypoint": waypoint}
#     response = DataController.insert(analyst, waypoint)
#     return reqItems

@router.put("/{id}", status_code=200)
async def insert(id: int, thin_Section: Thin_Section):
    response = DataController.insertEntry(id, thin_Section)
    return response

@router.delete("/{id}", status_code=200)
async def delete(id: int):
    response = DataController.deleteEntry("thin_Section", id)
    return response

@router.get("/", status_code=200)
async def getAll():
    response = DataController.getEntries("thin_Section")
    return response

@router.get("/{id}", status_code=200)
async def get(id: int):
    response = DataController.getEntryByID("thin_Section", id)
    return response

@router.patch("/", status_code=200)
async def update(analyst: Analyst, thin_Section: Thin_Section):
    response = DataController.update(Thin_Section)
    return {"Msg": response}

@router.put("/photo/{id}", status_code=200)
async def insertPhoto(id: int, photo: Thin_Section_Photo):
    response = DataController.insertEntry(id, photo)
    return response

@router.get("/photo/{id}", status_code=200)
async def insertPhoto(id: int):
    response = DataController.getEntryByID("thin_Section_Photo", id)
    return response

@router.delete("/photo/{id}", status_code=200)
async def deletePhoto(id: int):
    response = DataController.deleteEntry("thin_Section_Photo", id)
    return response
