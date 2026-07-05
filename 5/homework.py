# enter the name of a product
#once the product is entered, add it to register
#user must enter 3 products in total

count=0
cash_register=[]

while not count==3:
    product=input("Enter the products ")
    cash_register.append(product)
    count+=1

    print(cash_register)