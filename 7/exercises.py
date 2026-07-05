# students={
#     "s1":{
#         "name":"John",
#         "grades":[5,2,3,4,5]
#     },
#     "s2":{
#         "name":"Michael",
#         "grades":[3,4,3,2]
#     },
#     "s3":{
#         "name":"Jacob",
#         "grades":[4,4,5,1,5]
#     }
# }


# for student in students:
#     print(students[student]["grades"])
#     number_of_grades=len(students[student]["grades"])
#     sum_of_grades = 0
#
#
#     for grade in students[student]["grades"]:
#         sum_of_grades+=grade
#         print(sum_of_grades)
#
#     average_grade = sum_of_grades / number_of_grades
#     print(students[student]["name"],average_grade)

# numbers=[22,9,88,102,503,44,66]
# length=len(numbers)
# sum_of_numbers=0
# average=0
# above_average=[]
#
# for number in numbers:
#     sum_of_numbers+=number
#     average=sum_of_numbers/length
#
# for number in numbers:
#     if number>average:
#         above_average.append(number)
#
# print(above_average)

# products={
#     "candy":{
#         "price":5,
#         "quantity":40
#     },
#     "chips":{
#         "price":4,
#         "quantity":35
#     },
#     "peach tea":{
#         "price":2,
#         "quantity":15
#     }
# }
# total_price=0
#
#
# for product in products:
#     price=products[product]["price"]
#     quantity=products[product]["quantity"]
#     total_price+=price*quantity
#
# print(total_price)

# words=["palindrome","strawberry","fishing","google"]
# shortest_word=words[0]
# for word in words:
#     if len(word)<len(shortest_word):
#         shortest_word=word
#
# print(shortest_word)

# workers={
#     "w1":{
#         "name":"Stephanie",
#         "salary":7000
#     },
#     "w2":{
#         "name":"Shaw",
#         "salary":2500
#     },
#     "w3":{
#         "name":"Jesse",
#         "salary":9000
#     }
# }

# sum_of_salaries=0
# average_salary=0
#
# for worker in workers:
#     salary=workers[worker]["salary"]
#     sum_of_salaries+=salary
#
# average_salary=sum_of_salaries/len(workers)
#
# for worker in workers:
#     name=workers[worker]["name"]
#     salary=workers[worker]["salary"]
#     if salary>average_salary:
#         print(name)

# temperatures=[22,4,5,30,-2,0,-4]
#
# number_of_days=0
#
# for temperature in temperatures:
#     if temperature<0:
#         number_of_days+=1
#
# print(number_of_days)


# cities = {
#     "Belgrade": {
#         "country": "Serbia",
#         "population": 1400000
#     },
#     "Paris": {
#         "country": "France",
#         "population": 2100000
#     },
#     "Novi Sad": {
#         "country": "Serbia",
#         "population": 290000
#     },
#     "Lyon": {
#         "country": "France",
#         "population": 520000
#     }
# }
#
# for city in cities:
#     if cities[city]["country"]=="France":
#         print(city)

# numbers=[3,88,90,73,65,2,4]
# even_numbers=[]
#
# for number in numbers:
#     if number%2==0:
#         even_numbers.append(number)
#
# print(even_numbers)

# subjects = {
#     "Math": {
#         "points": [45, 60, 75, 50]
#     },
#     "Physics": {
#         "points": [30, 40, 55, 35]
#     },
#     "Chemistry": {
#         "points": [80, 65, 70, 90]
#     }
# }
#
# for subject in subjects:
#     points=subjects[subject]["points"]
#     number_of_points=len(points)
#     sum_of_points=0
#
#     for point in points:
#         sum_of_points+=point
#         # print(sum_of_grades)
#
#     average_grade=sum_of_points/number_of_points
#
#     if average_grade>=50:
#         print(subject,"ima dovoljan prosek")

# names=["Alex","Michael","Kobe","Steph","Aphelios"]
#
# for name in names:
#     if name[0]=='A':
#         print(name)

# athletes={
#     "a1":{
#         "name":"Michael",
#         "medals":28
#     },
#     "a2":{
#         "name":"Larisa",
#         "medals":18,
#     },
#     "a3":{
#         "name":"Marit",
#         "medals":15
#     },
#     "a4":{
#         "name":"John",
#         "medals":1
#     },
#     "a5":{
#         "name":"James",
#         "medals":2
#     }
#
# }
#
# for athlete in athletes:
#     medal=athletes[athlete]["medals"]
#     name=athletes[athlete]["name"]
#     if medal>3:
#         print(name)

# random=[1,"Python",3.5,"Code",7]
# number_of_string=0
# number_of_digits=0
#
# for i in random:
#     if isinstance(i,str):
#         number_of_string+=1
#     elif isinstance(i,float) or isinstance(i,int):
#         number_of_digits+=1
#
# print(number_of_digits)
# print(number_of_string)

# movies = {
#     "m1": {
#         "title": "Inception",
#         "year": 2010,
#         "rating": 8.8
#     },
#     "m2": {
#         "title": "Titanic",
#         "year": 1997,
#         "rating": 7.9
#     },
#     "m3": {
#         "title": "The Dark Knight",
#         "year": 2008,
#         "rating": 9.0
#     },
#     "m4": {
#         "title": "Avatar",
#         "year": 2009,
#         "rating": 7.8
#     }
# }
#
# for movie in movies:
#     name=movies[movie]["title"]
#     rating=movies[movie]["rating"]
#     if rating>8:
#         print(name)

# prices=[4600,225.6,2300,1958.35,2500]
# new_prices=[]
#
# for price in prices:
#     if price>1000:
#         price=price-price*0.1
#         new_prices.append(price)
#
# print(new_prices)

# students = {
#     "s1": {
#         "name": "John",
#         "age": 17
#     },
#     "s2": {
#         "name": "Michael",
#         "age": 19
#     },
#     "s3": {
#         "name": "Emma",
#         "age": 18
#     },
#     "s4": {
#         "name": "Sophia",
#         "age": 16
#     }
# }
#
# for student in students:
#     name=students[student]["name"]
#     age=students[student]["age"]
#     if age>=18:
#         print(name)

# numbers=[23,55,61,60,44,43,77]
# sum_of_numbers = 0
# i = 0
#
# while i < len(numbers) and sum_of_numbers <= 200:
#     sum_of_numbers += numbers[i]
#     print(sum_of_numbers)
#     i += 1

# while (sum_of_numbers<=200):
#     for number in numbers:
#         sum_of_numbers+=number
#         print(sum_of_numbers)
#         if sum_of_numbers>200:
#             break



# restaurants = {
#     "r1": {
#         "name": "Pizza House",
#         "ratings": [5, 4, 4, 5]
#     },
#     "r2": {
#         "name": "Burger Town",
#         "ratings": [3, 4, 2, 5]
#     },
#     "r3": {
#         "name": "Sushi World",
#         "ratings": [5, 5, 4, 4]
#     }
# }
#
#
# for restaurant in restaurants:
#     name=restaurants[restaurant]["name"]
#     ratings=restaurants[restaurant]["ratings"]
#     sum_of_ratings=0
#
#     for i in ratings:
#         sum_of_ratings+=i
#
#     average_rating=sum_of_ratings/len(ratings)
#     print(name,average_rating)

# sentences = [
#     "Python is fun",
#     "I love coding in Python",
#     "Hello world",
#     "This is a long sentence",
#     "Code every day"
# ]
#
# for sentence in sentences:
#     if len(sentence)>15:
#         print(sentence)

# courses = {
#     "c1": {
#         "name": "Python Basics",
#         "participants": ["John", "Emma", "Michael", "Sophia", "Daniel", "Olivia"]
#     },
#     "c2": {
#         "name": "Web Development",
#         "participants": ["Liam", "Noah", "Ava", "Mia"]
#     },
#     "c3": {
#         "name": "Data Science",
#         "participants": ["James", "Charlotte", "Amelia", "Benjamin", "Elijah", "Lucas", "Harper"]
#     }
# }
#
# for course in courses:
#     name=courses[course]["name"]
#     participant=courses[course]["participants"]
#     if len(participant)>5:
#         print(name)


students = {
    "student1": {
        "name": "John",
        "age": 17,
        "grades": [5, 4, 3, 5]
    },
    "student2": {
        "name": "Emma",
        "age": 19,
        "grades": [4, 5, 5, 4]
    },
    "student3": {
        "name": "Michael",
        "age": 18,
        "grades": [3, 4, 4, 5]
    },
    "student4": {
        "name": "Sophia",
        "age": 16,
        "grades": [5, 5, 4, 5]
    }
}

for student in students:
    name=students[student]["name"]
    age=students[student]["age"]
    grades=students[student]["grades"]
    sum_of_grades=0
    if age>=18:
        # print(name)
        for grade in grades:
            sum_of_grades+=grade
        average_grade=sum_of_grades/len(grades)
        print(name,average_grade)


