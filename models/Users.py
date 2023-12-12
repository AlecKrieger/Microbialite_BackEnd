createUserTable = """CREATE TABLE User (
	userID INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(20),
    lastName VARCHAR(20)
);"""

dropUserTable = "DROP TABLE IF EXISTS User;"