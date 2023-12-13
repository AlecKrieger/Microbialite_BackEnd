createWaypointTable = """CREATE TABLE Waypoint_Data(
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

createSearchesWaypointTable = """CREATE TABLE Searches_Waypoint(
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

createAddWaypointTable = """CREATE TABLE Searches_Waypoint(
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

dropWaypointTable = "DROP TABLE IF EXISTS Waypoint_Data;"

dropSearchesWaypointTable = "DROP TABLE IF EXISTS Searches_Waypoint;"

dropAddWaypointTable = "DROP TABLE IF EXISTS Add_Waypoint_Data;"