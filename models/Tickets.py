createTicketTable = """CREATE TABLE Ticket (
	ticketID INT PRIMARY KEY,
    dateInputed DATE,
    ticketDescription VARCHAR(50),
    status VARCHAR(6) CHECK (status IN ("OPEN", "CLOSED")),
    userID INT,
    analystID INT,
	FOREIGN KEY (userID) REFERENCES User(userID),
    FOREIGN KEY (analystID) REFERENCES Analyst(analystID)
);"""

createUserTicketTable = """CREATE TABLE User_Ticket (
	userID INT,
    ticketID INT,
    PRIMARY KEY (userID, ticketID),
    FOREIGN KEY (userID) REFERENCES User(userID),
    FOREIGN KEY (ticketID) REFERENCES Ticket(ticketID)
);"""

createAnalystTicketTable = """CREATE TABLE Analyst_Ticket (
	ticketID INT,
    analystID INT,
    PRIMARY KEY (analystID, ticketID),
    FOREIGN KEY (analystID) REFERENCES Analyst(analystID),
    FOREIGN KEY (ticketID) REFERENCES Ticket(ticketID)
);"""

dropTicketTable = "DROP TABLE IF EXISTS Ticket;"

dropAnalystTicketTable = "DROP TABLE IF EXISTS Analyst_Ticket;"

dropUserTicketTable = "DROP TABLE IF EXISTS User_Ticket;"
