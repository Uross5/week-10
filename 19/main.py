import random


from db import connection


from faker import Faker

faker=Faker()

genres=["Mystery","Adventure","Fantasy"]
adjectives=["Dark","Forbidden","Mysterious","Hidden","Eternal"]
nouns=["Secrets","Kingdom","Journey","Love","Shadow"]

def generate_author_name():
    author_name = faker.name()
    return author_name

def generate_genre():
    genre = random.choice(genres)
    return genre

def generate_date_of_birth():
    dob = faker.date_of_birth()
    return dob

def generate_book_title(book_genre,book_author):
    noun=random.choice(nouns)
    adjective=random.choice(adjectives)
    book_name=f"{adjective} {noun}:A {book_genre} story by {book_author}"
    return book_name

    #print(book_name)


def insert_users(con,name,date_of_birth):
    cursor = con.cursor()
    query="INSERT INTO users(name,dob) VALUES (%s,%s)"
    cursor.execute(query,(name,date_of_birth))
    con.commit()
    cursor.close()

def insert_books(con,book_name,category,author):
    cursor = con.cursor()
    query="INSERT INTO books(name,category,author) VALUES (%s,%s,%s)"
    cursor.execute(query,(book_name,category,author))
    con.commit()
    cursor.close()

genre=generate_genre()
dob=generate_date_of_birth()
author_name=generate_author_name()
book_title=generate_book_title(genre,author_name)
insert_users(connection,author_name,dob)
insert_books(connection,book_title,genre,author_name)
print(genre,dob,book_title)




# generate_book_title(connection)
# insert_users(connection,"Uros","2001-11-12")
# insert_books(connection,"Orlovi rano lete","Roman","Branko Copic")

