import requests
import json
import time
import os
from dotenv import load_dotenv
import mysql.connector

class Heat:
    def getAllData():

        mydb = mysql.connector.connect(
            host=os.getenv('DATABASE_URL'),
            port=os.getenv('DATABASE_PORT'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            database=os.getenv('DATABASE_NAME')
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM heats")

        myresult = mycursor.fetchall()
        return myresult