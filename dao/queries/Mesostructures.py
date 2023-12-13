createMesoTable = """CREATE TABLE Mesostructure_Data(
	mesostructureID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	mesostructureType VARCHAR(50),
    mesostructureTexture VARCHAR(50),
    mesostructureDesc VARCHAR(255),
    macrostructureID INT UNSIGNED NOT NULL,
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
	userID INT UNSIGNED NOT NULL,
	mesostructureID INT UNSIGNED NOT NULL,
	PRIMARY KEY(userID, mesostructureID),
	FOREIGN KEY (userID) REFERENCES User(userID)       
	ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (mesostructureID) REFERENCES Waypoint_Data(waypointID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""

createAddMesoTable = """CREATE TABLE Add_Meso_Data(
	analystID INT UNSIGNED NOT NULL,
	mesostructureID INT UNSIGNED NOT NULL,
	PRIMARY KEY(analystID, mesostructureID),
	FOREIGN KEY (analystID) REFERENCES Analyst(analystID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (mesostructureID) REFERENCES Waypoint_Data(waypointID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""

createPhotoTable = """CREATE TABLE Mesostructure_Photo(
	mesostructureID INT UNSIGNED NOT NULL,
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