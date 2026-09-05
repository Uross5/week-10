
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

connection = pymysql.connect(
    host='localhost',
    user='root',
    password=os.environ['db_password'],
    database='library',
    port=8888
)
if connection.open:print("connection established")
else:
    print("connection failed")
