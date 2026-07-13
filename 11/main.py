#1. Budget
#2. Add expense
#3. delete expense
#4. expense log
import json
import sys
from datetime import datetime
from winreg import error

user=None

with open("data/user.json",'r')as file:
    user=json.load(file)
    # print(user['budget'])

# def max budget, if the user has larger budget then max budget or less then 0,
#prin the error

user_budget=user["budget"]+user["credit"]
max_budget=500000

if user_budget>max_budget or user_budget<0:
    print("Error, your budget is either above or below the allowed amount")
    sys.exit()

print(f"Welcome back, your budget is {user_budget}")

expense=0

while expense<=0 or expense>user_budget:
    expense=int(input("Enter the amount of your expense "))

with open("logs/expense_log.txt","a") as file:
    remaining_budget=user_budget-expense
    message=(f"\nAmount{expense},User:{user["id"]},Budget:{user_budget}, "
             f"Remaining budget: {remaining_budget},"
             f"DataTime: {datetime.now()}")
    file.write(message)