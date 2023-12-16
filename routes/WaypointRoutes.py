from fastapi import APIRouter, Header
from typing import Union

from models.waypoint import Waypoint
from models.user import Analyst

from controller import DataController

router = APIRouter(prefix="/wpts")

tables = {"waypoint", "thin_section", "macrostructure", "mesostructure"}

# @router.put("/", status_code=200)
# async def insertWaypoint(analyst: Analyst, waypoint: Waypoint):
#     reqItems = {"analyst": analyst, "waypoint": waypoint}
#     response = DataController.insert(analyst, waypoint)
#     return reqItems

@router.get("/hsf", status_code=200)
async def getAllWaypoint():
    response = DataController.filterWayptHSF()
    return response

@router.get("/lpah", status_code=200)
async def getAllWaypoint():
    response = DataController.filterWayptLPAH()
    return response

@router.patch("/", status_code=200)
async def updatewaypoint(analyst: Analyst, waypoint: Waypoint):
    response = DataController.update(waypoint)
    return {"Msg": response}


@router.put("/{id}", status_code=200)
async def insertWaypoint(id: int, waypoint: Waypoint):
    response = DataController.insertEntry(id, waypoint)
    return response

@router.delete("/{id}", status_code=200)
async def deleteWaypoint(id: int):
    response = DataController.deleteEntry("waypoint", id)
    return response

@router.get("/", status_code=200)
async def getAllWaypoint():
    response = DataController.getEntries("waypoint")
    return response

@router.get("/{id}", status_code=200)
async def getWaypoint(id: int):
    response = DataController.getEntryByID("waypoint", id)
    return response