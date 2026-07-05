# random=[5,"New York","apple", 3.3, 14,22.4,19.4]
#
# count_str=0
# count_int=0
# count_float=0
#
# for i in random:
#     if isinstance(i, int):
#         count_int+=1
#
#     elif isinstance(i,str):
#         count_str+=1
#
#     elif isinstance(i,float):
#         count_float+=1
#
# print(f"Number of integers {count_int} ")
# print(f"Number of strings {count_str}")
# print(f"Number of float {count_float}")


# From the list of numbers, add up only positive numbers.

# numbers=[44,-5,-12,2,98,506]
# sum_of_numbers=0
#
# for i in numbers:
#     if i>=0:
#         #print(i)
#         sum_of_numbers+=i
#
# print(sum_of_numbers)


#Using a loop, find the first negative number in the list and print it.

# numbers=[44,53.6,-12,2,98,506]
#
# for i in numbers:
#     if i <0:
#         print(i)
#         break

#From the list of string, find the longest word

# words=["apple","palindrome","square","mouse"]
# x=""
#
# for i in words:
#     if len(i)>len(x):
#         x=i
#
# print(x)

# grades=[1,2,3,4,5]
# new_grades=[]
#
# for i in grades:
#     if i>1:
#         new_grades.append(i)
#
# print(new_grades)


# Count how many even numbers and how many odd numbers are in the list

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
#
# count_odd=0
# count_even=0
#
# for i in numbers:
#     if i%2==0:
#         count_even+=1
#     else:
#         count_odd+=1
# print(count_odd)
# print(count_even)

#From the list of temperatures:
#calculate the average temperature
#using conditions, print whether it is cold / pleasant / hot

# temperatures = [12, 18, 22, 27, 30, 16, 20]
# average= average=sum(temperatures)/len(temperatures)

#From the list of names, using a loop:
#print only the names that have more than 5 characters

# names = ["Michael", "Emma", "Sophia", "Daniel", "Olivia", "James", "Charlotte"]
#
# for i in names:
#     if len(i)>5:
#         print(i)

# Go through the list and print only the elements that are of type string

# items = [42, "apple", 3.14, "banana", True, "orange", 7]
#
# for i in items:
#     if isinstance(i,str):
#         print(i)

# Find the smallest and the largest number in the list without using min and max

# numbers=[0,-2,65,90,5,11,75]
# min=numbers[0]
# max=numbers[0]
# for i in numbers:
#     if i<min:
#         min=i
#     elif i>max:
#         max=i
#
# print(min)
# print(max)

# numbers=[11,45.6,88,50,0,99,1054,294]
# for i in numbers:
#     print(i)
#     if i==0:
#         break

# Add numbers from the list until the sum exceeds 100, then stop the loop.

# numbers = [15, 20, 30, 25, 18, 24,10]
#
# count=0
#
# for i in numbers:
#     count+=i
#     print(count)
#     if count>100:
#         break

#Count how many sentences in the list have more than 10 characters.

# sentences = [
#     "I like pizza.",
#     "Hello there!",
#     "Python is fun.",
#     "Good morning.",
#     "Nice day."
# ]
# count=0
#
# for i in sentences:
#     if len(i)>10:
#         count+=1
#
# print(count)

# Make a new list from the list of numbers that contains the squares of the numbers.

# numbers = [2, 4, 6, 8, 10]
# new_list=[]
#
# for i in numbers:
#     new_list.append(math.pow(i,2))
#
# print(new_list)

#Print each element of the list together with its index.

# items = ["apple", "banana", "orange", "grape", "mango"]
# for i in range (len(items)):
#     print(i,items[i])

# Ask the user to enter numbers until they enter a negative number
#At the end, print the sum of the entered numbers.

# total=0
# number=0
#
# while not number<0:
#     number=int(input("Enter the number "))
#     if number>=0:
#         total+=number
#
# print(total)

#Check using a loop whether the number 7 is in the list.

# numbers = [3, 5, 7, 9, 12, 15]
#
# for i in numbers:
#     if i==7:
#         print("bingo")

# From the list of numbers,
# find and print the numbers that appear more than once.

# numbers = [4, 7, 2, 9, 7, 5, 2, 8, 4, 4]
# duplicates=[]

# for i in numbers:
#     if numbers.count(i)>1 and i not in duplicates:
#         duplicates.append(i)
#
# print(duplicates)

# From the list of prices:
#increase each price by 10% and store the new prices in a new list

# prices = [12.50, 25.00, 8.99, 15.75, 30.00]
# new_prices=[]
#
# for i in prices:
#     new_prices.append(i*0.1+i)
#
# print(new_prices)

# Make a list of students with their points.
# calculate the average number of points
# print all students who have more points than the average

# students = [
#     ["John", 78],
#     ["Emma", 92],
#     ["Michael", 85],
#     ["Sophia", 88],
#     ["Daniel", 73]
# ]
#
# total=0
#
# for i in students:
#     total+=i[1]
#     average=total/len(students)
#
# print(average)
#
# for i in students:
#     if i[1]>average:
#         print(f"this student has more points than average -> {i[0]} ")
