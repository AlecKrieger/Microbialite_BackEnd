from pydantic import BaseModel

class Waypoint(BaseModel):
    waypointID: int
    dateCollected: str
    waypointName: str
    projectName: str
    latitude: int
    longitude: int
    northing: float
    easting: float
    utmZone1: int
    utmZone2: int
    datum: str
    projection: str
    fieldBook: str
    fieldBookPage: int
    formation: str
    siteName: str
    elevation: int
    measuredSection: int
    sectionName : str
    commments : str