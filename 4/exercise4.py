#Create a list that contains different data types (for example, an integer, a string, and a float).
#Check whether the first element is a string and print a message if it is.


# products=["BMW",10,52.6]
#
# if isinstance(products[0],str):
#     print("The first element is a string")
# else:
#     print("The first element is not a string")

#----------------------------------------------------------------------

# Create a list and check:
# if the list is empty → print "The list is empty"
# if it is not → print the number of elements

# powerball_numbers=[5,12,56,75,22,44]
#
# if len(powerball_numbers)==0:
#     print("The list is empty")
# else:
#     print("The list is not empty")

#------------------------------------------------

# If the list has more than 3 elements:
# print the first and last element
# Otherwise, print a message that the list is too short

# colours=["yellow","black","green","white"]
#
# n=len(colours)#length of the list
# #print(n)
#
# if n>3:
#     print(colours[0]+","+colours[n-1])
# else:
#     print("length is less than 3")

# Create a list of ages.
# If any number is less than 18, print "Not everyone is an adult".

# ages=[35,22,56,44]
#
# if min(ages)<18:
#     print("Not everyone is an adult")
# else:
#     print("Everyone is an adult")

# Create a list of product prices.
# If the average price is greater than 1000, print "Expensive", otherwise print "Affordable".

# product_prices=[1435.3,945,744,1020.5,350,2394]
#
# total_price=sum(product_prices)#sum of all products from the list
# average=total_price/len(product_prices)
#
# if average>1000:
#     print("Expensive")
# else:
#     print("Affordable")

#If the word "Python" is in the list of strings, print "Python is in the list".

# languages=["Java","JavaScript","C#","Python"]
#
# if "Python" in languages:
#     print("Python is in the list")

# From the list of numbers, check:
#
# if there are more positive numbers than negative numbers → print "More positive numbers"

# numbers=[2,-5,4,44,-7-19,14]

# Create a list of words.
# If the longest word is longer than 8 characters, print a message.

# words=["glass", "apple","car","body","strawberry"]
# longest=max(words,key=len)
# print(longest)
#
# if len(longest)>8:
#     print("The string has more than 8 characters")

# Create a list of grades (1–5).
# If the list contains the grade 1, print "There are failing grades".

# grades=[1,2,3,4,5]
#
# if 1 in grades:
#     print("There are failing grades")

# Check whether all elements in the list are numbers.
# If they are, calculate their sum.

# From the list of numbers, check:
#
# if there is at least one even number → print "The list contains an even number"

# numbers=[5,9,11,57,2]
#
# if any (num%2==0 for num in numbers):
#     print("There is an even number")

#If the list of names has more than 5 names, print 'A large list of names'

# names=["John", "Patrick","Matt","Jake","Zac","Zion"]
#
# if len(names)>5:
#     print("A large list of names")

#If the minimum number in the list is less than 0, print 'negative number'

# numbers=[-5,4,15,111,55,69]
#
# if min(numbers)<0:
#     print("Negative number")

#If the list has exactly 10 elements, print "The list has the ideal length"

# cars=["BMW","Audi","Porsche","Honda","Mazda",
#       "Peugeot","Renault","Ferrari","Seat","Ford"]
#
# if len(cars)==10:
#     print("The list has the ideal length")


#If the last element in the list is of type float, print "Decimal number"

# random=["desk","mouse","bike",5.5]
#
# if isinstance(random[-1],float):
#     print("Decimal number")


#Ako je najveća cena u listi veća od 5000, primeni popust od 10% na tu cenu

# laptop_price=[1200,800,2000,5300]
#
# most_expensive=max(laptop_price)
#
# if most_expensive>5000:
#     new_price=most_expensive*0.9
#     print(new_price)

#If at least one sentence in the list has more than 20 characters
# print  "A long sentence was found"

# sentences = [
#     "I like Python.",
#     "This is a short sentence.",
#     "Learning programming takes time.",
#     "Today is a nice day.",
#     "Practice makes progress."
# ]

# for i in sentences:
#     if len(i)>20:
#         print("A long sentence was found")
#         break- da ne bi ispisivao svaki put kada nadje recenicu koja ima vise od 20 karaktera

#If the list contains both numbers and strings, print 'Mixed data types'

# items=["TV",42,"apple",20.3]

#If the average value of the list of numbers is between 50 and 100:
#print "The average is within the expected range"

# numbers = [45, 60, 75, 90, 80]
#
# average=sum(numbers)/len(numbers)
# #print(average)
#
# if average>50 and average<100:
#     print("The average is within the expected range")

#Create a list of temperatures
# if the maximum temperature is greater than 30 → print "Hot"
# if it is between 15 and 30 → print "Pleasant"
# otherwise → print "Cold"

# temperatures = [12, 18, 25, 31, 22]
#
# if max(temperatures)>30:
#     print("hot")
# elif temperatures>15 and temperatures<30:
#     print("pleasant")
# else:
#     print("cold")





