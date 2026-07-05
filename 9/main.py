
def hello_world():
    print("Hello world")

def search(location, type):
    print(f"Pretrazujemo {location} - {type}")

def calculate_delivery(city):
    if city=="Belgrade":
        price=500
        print(f"price delivery is {price}")
    elif city=="Subotica":
        price=1200
        print(f"price delivery is {price}")
    elif city=="Zagreb":
        price=500
        print(f"price delivery is {price}")
    else:
        print("City does not exist")


hello_world()
search("Beograd","2 bedroom")
search("Madrid","2 bedroom")
calculate_delivery("Belgrade")

def calculate(number1, number2):
    return number1+number2

result=calculate(22,30)
print(result)
print(result*2)
