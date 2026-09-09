class Product:

    allowed_types=("iOS","android")
    number_of_products=0
    number_of_types={
        "android":0,
        "iOS":0
    }


    def __init__(self,name,price,amount,type):
        if amount<1:
            raise ValueError("amount must be greater than 0")
        self.name=name
        self.price=price
        if type not in Product.allowed_types:
            raise ValueError("Invalid type")
        self.name=name
        self.price=price
        self.amount=amount
        self.type=type
        Product.number_of_products+=1
        if type=="iOS":
            Product.number_of_types["iOS"]+=amount
        elif type=="android":
            Product.number_of_types["android"]+=amount



