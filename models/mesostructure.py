from pydantic import BaseModel

class Mesostructure(BaseModel):
    mesostructureID: int
    mesostructureType: str
    mesostructureTexture: str
    mesostructureDesc: str
    macrostructureID: int
    sampleSize: int
    fieldDescription: str
    rockDescription: str
    laminaThickness: float
    synopticRelief: float
    wavelength: float
    amplitude: float
    mesostructureGrains: str

class Mesostructure_Photo(BaseModel):
    mesostructureID: int
    mesoPhotoID: int
    mesoPhoto: str