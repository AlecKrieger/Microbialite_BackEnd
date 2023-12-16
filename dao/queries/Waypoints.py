# Waypoint_Data
createDataTable = """CREATE TABLE Waypoint_Data(
	waypointID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	dateCollected DATE,
	waypointName VARCHAR(50),
	projectName VARCHAR(50),
    latitude INT,
    longitude INT,
    northing DECIMAL(10,4),
    easting DECIMAL(10,4),
    utmZone1 TINYINT DEFAULT 11,
    utmZone2 TINYINT,
    datum VARCHAR(5) ,
    projection VARCHAR(10) DEFAULT "UTM",
    fieldBook VARCHAR(30),
    fieldBookPage TINYINT,
    formation VARCHAR(10) DEFAULT 'ThI',
    siteName VARCHAR(20),
    elevation SMALLINT,
    measuredSection boolean,
    sectionName VARCHAR(30),
    commments VARCHAR(255)
);"""
dropDataTable = "DROP TABLE IF EXISTS Waypoint_Data;"
getData = "SELECT * FROM Waypoint_Data;"
getDataByID = "SELECT * FROM Waypoint_Data WHERE waypointID = {waypointID};"
insertData = """INSERT INTO Waypoint_Data (
                dateCollected, 
                waypointName, 
                projectName, 
                latitude, 
                longitude, 
                northing, 
                easting, 
                utmZone1, 
                utmZone2, 
                datum, 
                projection, 
                fieldBook, 
                fieldBookPage, 
                formation, 
                siteName, 
                elevation, 
                measuredSection, 
                sectionName, 
                commments
                ) VALUES (
                '{dateCollected}', 
                '{waypointName}', 
                '{projectName}', 
                {latitude}, 
                {longitude}, 
                {northing}, 
                {easting}, 
                {utmZone1}, 
                {utmZone2}, 
                '{datum}', 
                '{projection}', 
                '{fieldBook}', 
                {fieldBookPage}, 
                '{formation}', 
                '{siteName}', 
                {elevation}, 
                {measuredSection}, 
                '{sectionName}', 
                '{commments}');"""
updateData = """UPDATE Waypoint_Data 
                SET 
                dateCollected='{dateCollected}', 
                waypointName='{waypointName}', 
                projectName='{projectName}', 
                latitude={latitude}, 
                longitude={longitude}, 
                northing={northing}, 
                easting={easting}, 
                utmZone1={utmZone1}, 
                utmZone2={utmZone2}, 
                datum='{datum}', 
                projection='{projection}', 
                fieldBook='{fieldBook}', 
                fieldBookPage={fieldBookPage}, 
                formation='{formation}', 
                siteName='{siteName}', 
                elevation={elevation}, 
                measuredSection={measuredSection}, 
                sectionName='{sectionName}', 
                commments='{commments}'
                WHERE 
                waypointID = {waypointID};"""
deleteData = "DELETE FROM Waypoint_Data WHERE waypointID = {waypointID};"

# Searches_Waypoint
createSearchesTable = """CREATE TABLE Searches_Waypoint(
	userID INT UNSIGNED NOT NULL,
	waypointID INT UNSIGNED NOT NULL,
	PRIMARY KEY(userID, waypointID),
	FOREIGN KEY (userID) REFERENCES User(userID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (waypointID) REFERENCES Waypoint_Data(waypointID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""
dropSearchesTable = "DROP TABLE IF EXISTS Searches_Waypoint;"
getSearches = "SELECT * FROM Searches_Waypoint;"
getSearchesByID = """SELECT * FROM Searches_Waypoint 
                    WHERE 
                    userID = {userID} 
                    AND 
                    waypointID = {waypointID};"""
insertSearches = """INSERT INTO Searches_Waypoint (userID, waypointID) 
                    VALUES 
                    ({userID}, {waypointID});"""
updateSearches = """UPDATE Searches_Waypoint 
                    SET 
                    userID = {newUserID} 
                    WHERE 
                    userID = {currentUserID} 
                    AND 
                    waypointID = {waypointID};"""
deleteSearches = """DELETE FROM Searches_Waypoint 
                    WHERE 
                    userID = {userID} 
                    AND 
                    waypointID = {waypointID};"""


# Add_Waypoint
createAddTable = """CREATE TABLE Add_Waypoint(
	userID INT UNSIGNED NOT NULL,
	waypointID INT UNSIGNED NOT NULL,
	PRIMARY KEY(analystID, waypointID),
	FOREIGN KEY (analystID) REFERENCES Analyst(analystID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (waypointID) REFERENCES Waypoint_Data(waypointID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""
dropAddTable = "DROP TABLE IF EXISTS Add_Waypoint;"
getAdd = "SELECT * FROM Add_Waypoint;"
getAddByID = """SELECT * FROM Add_Waypoint 
                WHERE 
                userID = {userID} 
                AND 
                waypointID = {waypointID};"""
insertAdd = """INSERT INTO Add_Waypoint (userID, waypointID) 
                VALUES 
                ({userID}, {waypointID});"""
updateAdd = """UPDATE Add_Waypoint 
                SET 
                serID = {newUserID} 
                WHERE 
                userID = {currentUserID} 
                AND 
                waypointID = {waypointID};"""
deleteAdd = """DELETE FROM Add_Waypoint 
                WHERE 
                userID = {userID} 
                AND 
                waypointID = {waypointID};"""

filterWayptHSF = "SELECT * FROM Waypoint_Data WHERE projectName = 'HSF';"

filterWayptLPAH = "SELECT * FROM Waypoint_Data WHERE projectName = 'LPAH';"