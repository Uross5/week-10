#1st exercise :
#Make a list named products and add 3 products iPhone 14, iPhone 15, Samsung s23
#Check whether iPhone 14 is in the list

products=["iPhone 14","iPhone 15", "Samsung s23"]
target_product=input("Enter the phone you are looking for ")

if target_product in products:
    print("Phone is in the list")
else:
    print("There is no such phone")