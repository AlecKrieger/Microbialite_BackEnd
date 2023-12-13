createTicketTable = """CREATE TABLE Ticket (
	ticketID INT UNSIGNED NOT NULL PRIMARY KEY,
    dateInputed DATE,
    ticketDescription VARCHAR(50),
    status VARCHAR(6) CHECK (status IN ("OPEN", "CLOSED")),
    userID INT,
    analystID INT,
	FOREIGN KEY (userID) REFERENCES User(userID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (analystID) REFERENCES Analyst(analystID)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);"""

createUserTicketTable = """CREATE TABLE User_Ticket (
	userID INT,
    ticketID INT,
    PRIMARY KEY (userID, ticketID),
    FOREIGN KEY (userID) REFERENCES User(userID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (ticketID) REFERENCES Ticket(ticketID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""

createAnalystTicketTable = """CREATE TABLE Analyst_Ticket (
	ticketID INT,
    analystID INT,
    PRIMARY KEY (analystID, ticketID),
    FOREIGN KEY (analystID) REFERENCES Analyst(analystID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (ticketID) REFERENCES Ticket(ticketID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""

dropTicketTable = "DROP TABLE IF EXISTS Ticket;"

dropAnalystTicketTable = "DROP TABLE IF EXISTS Analyst_Ticket;"

dropUserTicketTable = "DROP TABLE IF EXISTS User_Ticket;"

getTicketsByID = "SELECT * FROM Ticket WHERE ticketID = {ticketID};"

getTicketsByUser = "SELECT * FROM Ticket WHERE userID = {userID} AND status = 'OPEN';"

getTicketsByAnalyst = "SELECT * FROM Ticket WHERE userID = {analystID} AND status = 'OPEN';"

getTickets = "SELECT * FROM Ticket;"

deleteTicketByID = "DELETE FROM Ticket WHERE ticketID = {ticketID};"

insertTicket = "INSERT INTO Ticket VALUES (ticketDescription={ticketDescription}, status={status} userID={userID}, analystID={analystID});"

updateTicket = """UPDATE Ticket
    SET ticketDescription={ticketDescription}, status={status} userID={userID}, analystID={analystID} WHERE ticketID={ticketID};"""
