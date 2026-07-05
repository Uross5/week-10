# Write a program that asks the user to enter the name of a product than print its price
# If the product does not exist, print 'Product not found'

products={"iphone 14":999, "iphone 15":1200, "samsung s23":1200}

user_input=input("Enter the phone that you would like ").lower()

if user_input in products:
    print(products[user_input])
else:
    print("Product not found")
