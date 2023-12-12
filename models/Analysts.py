createAnalystTable = """CREATE TABLE Analyst (
	analystID INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(20),
    lastName VARCHAR(20)
);"""

dropAnalystTable = "DROP TABLE IF EXISTS Analyst;"