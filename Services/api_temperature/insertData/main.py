import requests
import json
import time
import os
from dotenv import load_dotenv
import mysql.connector




def get_data():
    response_API = requests.get('https://global-warming.org/api/temperature-api')
    return json.loads(response_API.text)

def insertRow(row):
    mydb = mysql.connector.connect(
        host=os.getenv('DATABASE_URL'),
        port=os.getenv('DATABASE_PORT'),
        user=os.getenv('DATABASE_USER'),
        password=os.getenv('DATABASE_PASSWORD'),
        database=os.getenv('DATABASE_NAME')
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO heats (time, station, land) VALUES (%s, %s,%s)"
    val = (row['time'],row['station'], row['land'])
    mycursor.execute(sql, val)

    mydb.commit()

    print("record inserted.")
    mycursor.close()

def run():
    while (True):
        print("Starting")
        load_dotenv()
        data = get_data()['result']
        for row in data:
            time.sleep(1)
            insertRow(row)
        print('All data has been inserted, restarting all process :)')
        print('Waiting 5 seconds to start all the process again :)')
        time.sleep(5)

if __name__ == '__main__':
    run()