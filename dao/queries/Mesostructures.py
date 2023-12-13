createMesoTable = """CREATE TABLE Mesostructure_Data(
	mesostructureID INT AUTO_INCREMENT PRIMARY KEY,
	mesostructureType VARCHAR(50),
    mesostructureTexture VARCHAR(50),
    mesostructureDesc VARCHAR(255),
    macrostructureID INT,
    sampleSize VARCHAR(20),
    fieldDescription VARCHAR(255),
    rockDescription VARCHAR(255),
    laminaThickness DECIMAL(2,2),
    synopticRelief DECIMAL(2,2),
    wavelength DECIMAL(2,2),
    amplitude DECIMAL(2,2),
    mesostructureGrains VARCHAR(50),
	FOREIGN KEY (macrostructureID) REFERENCES Macrostructure_Data(macrostructureID)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);"""

createSearchesMesoTable = """CREATE TABLE Searches_Meso(
	userID INT,
	mesostructureID INT,
	PRIMARY KEY(userID, mesostructureID),
	FOREIGN KEY (userID) REFERENCES User(userID)       
	ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (mesostructureID) REFERENCES Waypoint_Data(waypointID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""

createAddMesoTable = """CREATE TABLE Add_Meso_Data(
	analystID INT,
	mesostructureID INT,
	PRIMARY KEY(analystID, mesostructureID),
	FOREIGN KEY (analystID) REFERENCES Analyst(analystID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (mesostructureID) REFERENCES Waypoint_Data(waypointID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""

createPhotoTable = """CREATE TABLE Mesostructure_Photo(
	mesostructureID INT,
	mesoPhotoID INT,
	mesoPhoto VARCHAR(255),
	PRIMARY KEY(mesostructureID, mesoPhotoID),
    FOREIGN KEY (mesostructureID) REFERENCES Mesostructure_Data(mesostructureID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""

dropDataTable = "DROP TABLE IF EXISTS Mesostructure_Data;"

dropSearchesTable = "DROP TABLE IF EXISTS Searches_Meso;"

dropAddDataTable = "DROP TABLE IF EXISTS Add_Meso_Data;"

dropPhotoTable = "DROP TABLE IF EXISTS Mesostructure_Photo;"