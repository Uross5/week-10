
import random
from faker import Faker
faker = Faker()

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

def insert_books(con,book_name,category,author):
    cursor = con.cursor()
    query="INSERT INTO books(name,category,author) VALUES (%s,%s,%s)"
    cursor.execute(query,(book_name,category,author))
    con.commit()
    cursor.close()


def get_all_books(con):
    cursor = con.cursor()
    query="SELECT * FROM books"
    cursor.execute(query)
    rows=cursor.fetchall()
    cursor.close()
    return rows

def get_book_by_id(con,book_id):
    cursor = con.cursor()
    query="SELECT * FROM books WHERE id=%s"
    cursor.execute(query,(book_id,))
    result=cursor.fetchone()
    cursor.close()
    return result

def delete_book(con,book_id):
    cursor=con.cursor()
    query="DELETE FROM books WHERE id=%s"
    cursor.execute(query,(book_id,))
    con.commit()
    cursor.close()

