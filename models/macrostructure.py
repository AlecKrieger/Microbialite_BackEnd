from pydantic import BaseModel

class Macrostructure(BaseModel):
    macrostructureID: int
    macrostructureType: str
    sectionHeight: float
    comments: str
    waypointID: int
    megastructureType: str
    megastructureShape: str
    megastructureSize: str
    substrate: str
    initiation: str
    planView: str
    linkage: str
    spacing: str
    shape: str
    shapelayering: str
    shapeDome: str
    shape3d: str
    aspectRation: str
    growthVariability: str
    attitude: str
    branchingStyle: str
    branchingMode: str
    branchingAngle: str
    columnShape: str

class Macrostructure_Photo(BaseModel):
    macrostructureID: int
    macroPhotoID: int
    macroPhoto: str