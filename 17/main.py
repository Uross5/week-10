import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

connection=pymysql.connect(
    host="localhost",
    user="root",
    password=os.environ["DB_PASSWORD"],
    database="python17",
    port=8888

)

def create_user(con,username,password,age):
    cursor=con.cursor()
    cursor.execute(
        "INSERT INTO users(username,password,age) VALUES (%s,%s,%s)",
        (username,password,age))
    con.commit()
    cursor.close()

create_user(connection,"Nemanja","1111",55)
