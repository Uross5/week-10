#Ask user for age
#If the user is 18 or older print 'you are of legal age'
#If user is younger than 18 print 'you are underage'
import sys

#user_age=int (input("What's your age? "))
#print(user_age)

#if user_age<18:
    #print("You are underage")
#else:
   # print("You are of legal age")

# New exercise:
# If user is 12 or younger print 'You are a child'
#If user is 13 and younger than 18 print 'You are a teenager'
#if user is 18 and younger than 65 pring 'You are an adult'
#if user is 65 or older print 'You are a pensioner'


age= int (input("What's your age "))

if age <0:
    print("Error")
    sys.exit()

if age<=12:
    print("You are a child")
elif age>=13 and age<18:
    print("You are a teenager")
elif age>=18 and age<65:
    print("You are an adult")
else:
    print("You are a pensioner")
