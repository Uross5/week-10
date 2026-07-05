price_of_cart=int (input("Enter the price of your cart: "))
#print(price_of_cart)

sale_10_percent=price_of_cart*0.1

if price_of_cart>=1000:
    print(f"You got 10% which is {sale_10_percent}e" )
else:
    print("Your cart is 1000")