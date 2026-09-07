def insert_users(con,name,date_of_birth):
    cursor = con.cursor()
    query="INSERT INTO users(name,dob) VALUES (%s,%s)"
    cursor.execute(query,(name,date_of_birth))
    last_id=cursor.lastrowid
    con.commit()
    # print(f"Successfully inserted row. ID: {last_id}")
    cursor.close()
    return last_id