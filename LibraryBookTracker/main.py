
books = [
    {
        "title": "Python Programming",
        "author": "John Doe",
        "year": 2020,
        "status": {
            "borrowed": False,
            "borrower": None
        }
    },
    {
        "title": "Data Structures",
        "author": "Jane Smith",
        "year": 2019,
        "status": {
            "borrowed": True,
            "borrower": "Marko"
        }
    },
    {
        "title": "Algorithms in Depth",
        "author": "Ana Petrovic",
        "year": 2021,
        "status": {
            "borrowed": False,
            "borrower": None
        }
    }
]

def list_books(books):
    for book in books:
        if not check_availability(book):
            print(f'{book["title"]} — borrowed by '
                f'{book["status"]["borrower"]}')

        else:
            print(f'{book["title"]} — available')


def check_availability(book):
    if book["status"]["borrowed"]==False:
        return True
    else:
        return False

def borrow_book(book,borrower_name):
    if check_availability(book):
        book["status"]["borrowed"]=True
        book["status"]["borrower"]=borrower_name
        print(f"Book was borrowed successfully by {borrower_name}")
    else:
        print(f"Book is already borrowed by {book["status"]["borrower"]}")


def return_book(book):
    if check_availability(book)==False:
        book["status"]["borrowed"]=False
        print(f'{book["title"]} was returned successfully')
    else:
        print(f'{book["title"]} is already available')

def add_book(books,title,author,year):
    new_book={
        "title":title,
        "author":author,
        "year":year,
        "status":{
            "borrowed":False,
            "borrower": None
        }

    }
    books.append(new_book)
    print(f"{title} book is added")

list_books(books)



