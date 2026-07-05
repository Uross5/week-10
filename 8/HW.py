#HW -> show the most expensive item


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

option = None
user_option = ["add", "delete", "list", "stop", "history", "delete_all",
               "the most expensive item"]
history = []
while option not in user_option:
    option = input(f"What would you like to do? {",".join(user_option)} \n").lower()

    if option == "delete":
        product = None

        while product not in products:
            product = input("Enter an item you would like to delete: \n").lower()

        del products[product]
        msg = f"You deleted {product}"
        print(msg)
        history.append(msg)
        option = None

    elif option == "add":
        product = None
        while product in products or product == None:
            product = input("Enter an item you would like to add that "
                            "does not already exist \n").lower()

        price = None
        while price is None or price <= 0:
            price = int(input("Enter the price of the product: \n"))

        quantity = None
        while quantity is None or quantity < 0:
            quantity = int(input("Enter the price of the quantity: \n"))
        products[product] = {
            "price": price,
            "quantity": quantity
        }

        option = None
        msg = f"You added {product}"
        print(msg)
        history.append(msg)


    elif option == "list":
        print(products)
        option = None

    elif option == "history":
        print(history)
        option = None

    elif option == "delete_all":
        products.clear()
        option = None

    elif option=="the most expensive item":
        the_most_expensive_item=None
        highest_price=0
        for product in products:
            price=products[product]["price"]
            if price>highest_price:
                highest_price=price
                the_most_expensive_item=product

        print(f"The most expensive product is {the_most_expensive_item}")
        option=None
