#program_name="Java"
#version=19.2
#is_new_program=False;
#print(program_name,version,is_new_program)
from os import remove

books=["Harry Potter 1", "The Great Gatsby", "Harry Potter 2"]
#print(books)

books[0]="Pragmatic programmer"
print(books)
books.pop() #-> moze pop komanda ako se ne naglasi koji index tacno
# pop ce obrisati poslednji elemnt liste, source w3 school
print(books)