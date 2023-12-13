createAnalystTable = """CREATE TABLE Analyst (
	analystID INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(20),
    lastName VARCHAR(20)
);"""

dropAnalystTable = "DROP TABLE IF EXISTS Analyst;"

getAnalysts = "SELECT * FROM TABLE Analyst;"

getAnalystByID = "SELECT * FROM TABLE Analyst WHERE analystID = {analystID};"

insertAnalyst = "INSERT INTO Analyst (firstName, lastName) VALUES ('{firstName}', '{lastName}');"

updateAnalyst = "UPDATE Analyst SET firstName='{firstName}', lastName = '{lastName}' WHERE analystID = {analystID};"

deleteAnalyst = "DELETE FROM Analyst WHERE analystID = {analystID};"