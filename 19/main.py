from models.book import *
from models.db import connection
from models.user import *


option=None

while option is None or option== '':
    option=input("Enter your choice: \n 1. Create a random book \n 2. Show books \n 3. Show book by ID "
                 "\n 4. Delete a book"  ).strip()
    if option == "":
        print("Choice cannot be empty")
        continue
    option=int(option)

    if option==1:
        genre=generate_genre()
        author=generate_author_name()
        title=generate_book_title(genre,author)
        dob=generate_date_of_birth()

        user=insert_users(connection,author,dob)
        insert_books(connection,title,genre,user)
        print(f"Created a random book and title is {title} ")

    elif option==2:
        books = get_all_books(connection)
        print(books)

    elif option==3:
        book=None
        while book is None:
            book_id=int(input("Enter your book id: "))
            book=get_book_by_id(connection,book_id)
            if book is None:
                print("Book does not exist")
            else:
                print(book)
    elif option==4:
        book_id=int(input("Enter your book id: "))
        delete_book(connection,book_id)
    else:
        option=None
connection.close()





