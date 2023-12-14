# Thin_Section_Data
createDataTable = """CREATE TABLE Thin_Section_Data(
	thinSectionID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	tsDescription VARCHAR(255),
    mesostructureID INT UNSIGNED NOT NULL,
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
dropDataTable = "DROP TABLE IF EXISTS Thin_Section_Data;"
getData = "SELECT * FROM Thin_Section_Data;"
getDataByID = "SELECT * FROM Thin_Section_Data WHERE thinSectionID = {thinSectionID};"
insertData = """INSERT INTO Thin_Section_Data (
                tsDescription, 
                mesostructureID, 
                primaryTexture, 
                secondaryTexture, 
                tertiaryTexture, 
                otherTexture, 
                cement1, 
                cement2, 
                porosity1, 
                porosity2, 
                mineralogy1, 
                mineralogy2, 
                porosityPercentEst, 
                cementFillPorosity, 
                clasticGrain1, 
                clasticGrain2
                ) VALUES (
                '{tsDescription}', 
                {mesostructureID}, 
                '{primaryTexture}', 
                '{secondaryTexture}', 
                '{tertiaryTexture}', 
                '{otherTexture}', 
                '{cement1}', 
                '{cement2}', 
                '{porosity1}', 
                '{porosity2}', 
                '{mineralogy1}', 
                '{mineralogy2}', 
                {porosityPercentEst}, 
                '{cementFillPorosity}', 
                '{clasticGrain1}', 
                '{clasticGrain2}');"""
updateData = """UPDATE Thin_Section_Data SET 
                tsDescription='{tsDescription}', 
                mesostructureID={mesostructureID}, 
                primaryTexture='{primaryTexture}', 
                secondaryTexture='{secondaryTexture}', 
                tertiaryTexture='{tertiaryTexture}', 
                otherTexture='{otherTexture}', 
                cement1='{cement1}', 
                cement2='{cement2}', 
                porosity1='{porosity1}', 
                porosity2='{porosity2}', 
                mineralogy1='{mineralogy1}', 
                mineralogy2='{mineralogy2}', 
                porosityPercentEst={porosityPercentEst}, 
                cementFillPorosity='{cementFillPorosity}', 
                clasticGrain1='{clasticGrain1}', 
                clasticGrain2='{clasticGrain2}' 
                WHERE 
                thinSectionID = {thinSectionID};"""
deleteData = """DELETE FROM Thin_Section_Data 
                WHERE 
                thinSectionID = {thinSectionID};"""


createSearchesTSTable = """CREATE TABLE Searches_Thin(
	userID INT UNSIGNED NOT NULL,
	thinSectionID INT UNSIGNED NOT NULL,
	PRIMARY KEY(userID, thinSectionID),
	FOREIGN KEY (userID) REFERENCES User(userID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
	FOREIGN KEY (thinSectionID) REFERENCES Thin_Section_Data(thinSectionID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""

createAddTSTable = """CREATE TABLE Add_Thin_Data(
	analystID INT UNSIGNED NOT NULL,
	thinSectionID INT UNSIGNED NOT NULL,
	PRIMARY KEY(analystID, thinSectionID),
	FOREIGN KEY (analystID) REFERENCES Analyst(analystID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
	FOREIGN KEY (thinSectionID) REFERENCES Thin_Section_Data(thinSectionID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""

createPhotoTable = """CREATE TABLE THIN_SECTION_PHOTO(
	thinSectionID INT UNSIGNED NOT NULL,
	thinSectionPhotoID INT,
	thinSectionPhoto VARCHAR(255),
	PRIMARY KEY(thinSectionID, thinSectionPhotoID),
    FOREIGN KEY (thinSectionID) REFERENCES Thin_Section_Data(thinSectionID)
    ON UPDATE CASCADE
    ON DELETE CASCADE);"""


dropSearchesTable = "DROP TABLE IF EXISTS Searches_Thin;"

dropAddDataTable = "DROP TABLE IF EXISTS Add_Thin_Data;"

dropPhotoTable = "DROP TABLE IF EXISTS THIN_SECTION_PHOTO;"