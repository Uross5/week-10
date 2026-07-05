products = {
    "bread": {
        "price": 100,
        "quantity": 50
    },
    "beer": {
        "price": 150,
        "quantity": 220
    }
}

# 1st exercise
# Ask the user, to enter the item that he would like to delete
# Then delete that item

option=None

while option not in ["add","delete"]:
    option=input("What would you like to do? ").lower()

if option=="delete":

    product=None
    while product not in products:
        product=input("Enter an item you would like to delete ").lower()
        print(product)

    del products[product]
    print(products)

elif option == "add":
    product=None
    while product in products or product == None:
        product=input("Enter an item you would like to add that "
                      "does not already exist ").lower()


    price=None
    while price is None or price<=0:
        price=int(input("Enter the price of the product: "))

    quantity=None
    while quantity is None or quantity <0:
        quantity = int(input("Enter the price of the quantity: "))
    products[product]={
        "price":price,
        "quantity":quantity
    }

print(products)



#Ask the user what he would like to do
#A:Delete product
#B:Add a product->"Test"

