createUserTable = """CREATE TABLE User (
	userID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(20),
    lastName VARCHAR(20)
);"""

dropUserTable = "DROP TABLE IF EXISTS User;"

getUsers = "SELECT * FROM User;"

getUserByID = "SELECT * FROM User WHERE userID = {userID};"

insertUser = "INSERT INTO User (firstName, lastName) VALUES ('{firstName}', '{lastName}');"

updateUser = "UPDATE User SET firstName='{firstName}', lastName = '{lastName}' WHERE userID = {userID};"

deleteUser = "DELETE FROM User WHERE userID = {userID};"