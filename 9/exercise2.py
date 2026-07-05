def calculate_delivery(city):
    if city=="Belgrade" or "Zagreb":
        return 500
    elif city=="Subotica":
        return 1200
    elif city=="Novi Sad":
        return 700
    else:
        return -1

belgrade_delivery=calculate_delivery("Belgrade")
print(belgrade_delivery)

product_price=200
total_price=belgrade_delivery+product_price
print(f"Your order costs {product_price}, and delivery is {belgrade_delivery}"
      f", and your total is {total_price}")
