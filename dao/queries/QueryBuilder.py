getRecordQuery = "{ACTION} {COLUMNS} FROM {TABLE}{WHERE}{ORDERBY};"


def buildQuery(action, table, where=None, orderBy = None, columns=None):
    #Create Where Clause
    whereString = AND.join([WhereEquals.get(condition) for condition in where if condition]) #Join multiple conditions with " AND "
    if len(whereString == 0):
        whereString = WHERE + whereString #Add WHERE to beginning of where clause
    #Create list of columns
    columnString = ""
    if columns is None:
        columnString = ALL
    return getRecordQuery.format(ACTION = Actions.get(action), COLUMNS = columnString, TABLE = Tables.get(table), WHERE = whereString, ORDERBY = orderBy) 

#Query Actions
Actions = {"SELECT": "SELECT", "DELETE": "DELETE"}

#Query Subcomponents
WHERE = " WHERE "
AND = " AND "
ORDERBY = " ORDER BY"
ALL = "*"
DESCENDING = " DESC"

#Table Names
Tables = {
    "TICKET" : "Ticket",
    "USERTICKET" : "User_Ticket",
    "ANALYSTTICKET" : "Analyst_Ticket"
    }


#Where clause
WhereEquals = {
    "ticketIDEquals" : "ticketID = {ticketID}",
    "userIDEquals" : "userID = {userID}",
    "analystIDEquals" : "analystID = {analystID}",
    "statusEquals" : "status = {status}"}



