createAnalystTable = """CREATE TABLE Analyst (
	analystID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(20),
    lastName VARCHAR(20),
    analystType VARCHAR(10)
);"""

dropAnalystTable = "DROP TABLE IF EXISTS Analyst;"

getAnalysts = "SELECT * FROM Analyst;"

getAnalystByID = "SELECT * FROM Analyst WHERE analystID = {analystID};"

insertAnalyst = "INSERT INTO Analyst (firstName, lastName, analystType) VALUES ('{firstName}', '{lastName}', '{analystType}');"

updateAnalyst = "UPDATE Analyst SET firstName='{firstName}', lastName = '{lastName}', analystType = '{analystType}' WHERE analystID = {analystID};"

deleteAnalyst = "DELETE FROM Analyst WHERE analystID = {analystID};"