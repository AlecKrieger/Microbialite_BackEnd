from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables from the .env file
load_dotenv(find_dotenv())
import MySQLdb
app = FastAPI()

# Connect to db
def connectToDB():
    connection = MySQLdb.connect(
        host= os.getenv("DB_HOST"),
        user=os.getenv("DB_USERNAME"),
        passwd= os.getenv("DB_PASSWORD"),
        db= os.getenv("DB_NAME"),
        autocommit = True,
        ssl_mode = "VERIFY_IDENTITY",
        ssl = {"ca": "/etc/ssl/cert.pem"}
    )
    return connection
