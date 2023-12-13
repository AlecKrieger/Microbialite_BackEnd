createTSTable = """CREATE TABLE Thin_Section_Data(
	thinSectionID INT AUTO_INCREMENT PRIMARY KEY,
	tsDescription VARCHAR(255),
    mesostructureID INT,
	primaryTexture VARCHAR(50),
	secondaryTexture VARCHAR(50),
    tertiaryTexture VARCHAR(50),
    otherTexture VARCHAR(50),
	cement1 VARCHAR(50),
	cement2 VARCHAR(50),
	porosity1 VARCHAR(50),
	porosity2 VARCHAR(50),
	mineralogy1 VARCHAR(50),
	mineralogy2 VARCHAR(50),
	porosityPercentEst INT,
	cementFillPorosity VARCHAR(3),
    clasticGrain1 VARCHAR(20),
	clasticGrain2 VARCHAR(20),
	FOREIGN KEY (mesostructureID) REFERENCES Mesostructure_Data(mesostructureID)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);"""

createSearchesTSTable = """CREATE TABLE Searches_Thin(
	userID INT,
	thinSectionID INT,
	PRIMARY KEY(userID, thinSectionID),
	FOREIGN KEY (userID) REFERENCES User(userID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
	FOREIGN KEY (thinSectionID) REFERENCES Thin_Section_Data(thinSectionID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""

createAddTSTable = """CREATE TABLE Add_Thin_Data(
	analystID INT,
	thinSectionID INT,
	PRIMARY KEY(analystID, thinSectionID),
	FOREIGN KEY (analystID) REFERENCES Analyst(analystID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
	FOREIGN KEY (thinSectionID) REFERENCES Thin_Section_Data(thinSectionID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""

createPhotoTable = """CREATE TABLE THIN_SECTION_PHOTO(
	thinSectionID INT,
	thinSectionPhotoID INT,
	thinSectionPhoto VARCHAR(255),
	PRIMARY KEY(thinSectionID, thinSectionPhotoID),
    FOREIGN KEY (thinSectionID) REFERENCES Thin_Section_Data(thinSectionID)
    ON UPDATE CASCADE
    ON DELETE CASCADE);"""

dropDataTable = "DROP TABLE IF EXISTS Thin_Section_Data;"

dropSearchesTable = "DROP TABLE IF EXISTS Searches_Thin;"

dropAddDataTable = "DROP TABLE IF EXISTS Add_Thin_Data;"

dropPhotoTable = "DROP TABLE IF EXISTS THIN_SECTION_PHOTO;"