#virtual library (def)
#CRUD
#add book
#list book
#delete book


books=[]

def add_book(name,author):
    books.append({"name":name, "author":author})

def find_book_by_name(name):
    for book in books:
        if book['name']==name:
            return book

def delete_book_by_name(name):
    book=find_book_by_name(name)

    if book is None:
        print("Book does not exist")
    else:
        books.remove(book)
        print("The book is deleted")



add_book("Orlovi rano lete", "Branko Copic")
add_book("Harry Potter", "J.K. Rowling")

#book=find_book_by_name("Orlovi rano lete")
#if book is None:
    #print("Book does not exist")

delete_book_by_name("Harry Potter")


print(books)