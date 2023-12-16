from pydantic import BaseModel

class Thin_Section(BaseModel):
    thinSectionID: int
    tsDescription: str
    mesostructureID: int
    primaryTexture: int
    secondaryTexture: str
    tertiaryTexture: str
    otherTexture: str
    cement1: str
    cement2: str
    porosity1: str
    porosity2: str
    mineralogy1: str
    mineralogy2: str
    porosityPercentEst: int
    cementFillPorosity: str
    clasticGrain1: str 
    clasticGrain2: str

class Thin_Section_Photo(BaseModel):
	thinSectionID: int
	thinSectionPhotoID: int
	thinSectionPhoto: str