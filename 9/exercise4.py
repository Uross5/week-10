# students={
#     "s1":{
#         "name":"Jake",
#         "grades":[5,4,5]
#     },
#     "s2":{
#         "name":"Paul",
#         "grades":[3,4,4]
#     }
# }
#
# def average_grade(students):
#     averages={}
#     for student in students:
#         name = students[student]['name']
#         grades = students[student]['grades']
#         sum_of_grades=0
#         number_of_grades=len(students[student]['grades'])
#
#         for grade in grades:
#             sum_of_grades+=grade
#             number_of_grades=len(grades)
#             average=sum_of_grades/number_of_grades
#             averages[name]=average
#
#     return averages
#
# print(average_grade(students))

# numbers=[44,31,90,55,12,5]
#
# def larger_than_average(numbers):
#     if len(numbers)==0:
#         return []
#
#     larger=[]
#     sum_of_numbers=0
#     for number in numbers:
#         sum_of_numbers+=number
#
#     average=sum_of_numbers/len(numbers)
#
#     for number in numbers:
#         if number>average:
#             larger.append(number)
#     return larger
#
# print(larger_than_average(numbers))

# products={
#     "chocolate":{
#         "price":300,
#         "quantity":3
#     },
#     "juice":{
#         "price":100,
#         "quantity":2
#     },
#     "chips":{
#         "price":50,
#         "quantity":1
#     }
# }
#
# def total_price_of_products(products):
#     total_amount=0
#     for product in products:
#         prices=products[product]['price']
#         quantity=products[product]['quantity']
#         total_amount+=prices*quantity
#
#     return total_amount
#
#
#
# total_amount=total_price_of_products(products)
# print(total_amount)

# strings=["egg","apple","plane","legends",]
#
# def shortest_word_from_the_list(strings):
#     if len(strings)==0:
#         return []
#     shortest=strings[0]
#     for i in strings:
#         if len(i)<len(shortest):
#             shortest=i
#     return shortest
#
# print(shortest_word_from_the_list(strings))


# employees = {
#     "e1": {
#         "name": "Mark",
#         "salary": 3000
#     },
#     "e2": {
#         "name": "Anna",
#         "salary": 4500
#     },
#     "e3": {
#         "name": "John",
#         "salary": 2500
#     }
# }
#
# def above_average(employees):
#     above=[]
#     total_salary=0
#     average_salary = 0
#     for employee in employees:
#         salaries=employees[employee]['salary']
#         total_salary+=salaries
#
#     average_salary=total_salary/len(employees)
#
#
#     for employee in employees:
#         name=employees[employee]['name']
#         salaries=employees[employee]['salary']
#         if salaries>average_salary:
#             above.append(name)
#     return above
#
#
# print(above_average(employees))



# temperatures = [5, -3, 0, -7, 12, -1, 4]
#
# def temperatures_below_zero(temperatures):
#     count=0
#     for temp in temperatures:
#         if temp<0:
#             count+=1
#     return count
#
# print(temperatures_below_zero(temperatures))


# cities = {
#     "Belgrade": {
#         "country": "Serbia",
#         "population": 1400000
#     },
#     "Novi Sad": {
#         "country": "Serbia",
#         "population": 370000
#     },
#     "Paris": {
#         "country": "France",
#         "population": 2100000
#     },
#     "Lyon": {
#         "country": "France",
#         "population": 520000
#     }
# }
#
# def cities_in_countries(cities, countries):
#     result=[]
#     for city in cities:
#         country=cities[city]["country"]
#         if country==countries:
#             result.append(city)
#     return result
#
# print(cities_in_countries(cities,"Serbia"))


# numbers=[12,23,56,77,90,865]
#
# def even_numbers(numbers):
#     even=[]
#     if len(numbers)<=0:
#         return []
#     for number in numbers:
#         if number%2==0:
#             even.append(number)
#     return even
#
# result=even_numbers(numbers)
# print(result)

# subjects = {
#     "Mathematics": {
#         "points": [60, 45, 70]
#     },
#     "Programming": {
#         "points": [80, 75, 90]
#     },
#     "History": {
#         "points": [30, 40, 45]
#     }
# }
#
# def enough_to_pass(subjects):
#     result={}
#     for subject in subjects:
#         points=subjects[subject]['points']
#         total_points=0
#         average_to_pass=0
#
#         for point in points:
#             total_points+=point
#
#         average_to_pass=total_points/len(points)
#
#         if average_to_pass>=50:
#             result[subject]=True
#         else:
#             result[subject]=False
#     return result
#
# print(enough_to_pass(subjects))

# names=["Jacob","Steph","Seraphine","Will","James"]
#
# def name_starting_with(names,letter):
#     result=[]
#     if len(names)<0:
#         return []
#     for name in names:
#         if name[0]==letter:
#             result.append(name)
#     return result
#
# answer=name_starting_with(names,"W")
# print(answer)

# athletes = {
#     "a1": {
#         "name": "Novak",
#         "medals": 12
#     },
#     "a2": {
#         "name": "Ana",
#         "medals": 7
#     },
#     "a3": {
#         "name": "Marko",
#         "medals": 4
#     }
# }
#
# def more_medals(athletes,number_of_medals):
#     result=[]
#     for athlete in athletes:
#         name=athletes[athlete]["name"]
#         medals=athletes[athlete]["medals"]
#
#         if medals>number_of_medals:
#             result.append(name)
#     return result


# print(more_medals(athletes,4))


# random=[1,"Python","Code",3.5,7,2.2,1]
#
# def number_of_tips(list):
#     result={
#         "int":0,
#         "string":0,
#         "float":0
#     }
#
#     for i in list:
#         if type(i) == int:
#             result["int"]+=1
#         elif type(i)==str:
#             result["string"]+=1
#         elif type(i)==float:
#             result["float"]+=1
#     return result
#
# print(number_of_tips(random))

# movies = {
#     "The Shawshank Redemption": {
#         "year": 1994,
#         "rating": 9.3
#     },
#     "Interstellar": {
#         "year": 2014,
#         "rating": 8.7
#     },
#     "The Lion King": {
#         "year": 1994,
#         "rating": 8.5
#     },
#     "Avatar": {
#         "year": 2009,
#         "rating": 7.9
#     }
# }
#
# def high_rate(movies):
#     result=[]
#     if len(movies)<=0:
#         return []
#
#     for movie in movies:
#         rating=movies[movie]["rating"]
#         if rating>8:
#             result.append(movie)
#     return result
#
# print(high_rate(movies))

# prices = [50, 120, 200, 80]
#
# def discount(prices, threshold, percentage):
#     result=[]
#     for price in prices:
#         if price>threshold:
#             discount_amount=price*percentage/100
#             new_price=price-discount_amount
#             result.append(new_price)
#         else:
#             result.append(price)
#     return result
#
# print(discount(prices,100,20))

# students = {
#     "s1": {
#         "name": "Ana",
#         "age": 17
#     },
#     "s2": {
#         "name": "Marko",
#         "age": 19
#     },
#     "s3": {
#         "name": "Jovan",
#         "age": 18
#     },
#     "s4": {
#         "name": "Mila",
#         "age": 16
#     }
# }
#
# def adult(students):
#     names=[]
#     if len(names)==0:
#         return []
#
#     for student in students:
#         age=students[student]["age"]
#         if age>=18:
#             names.append(students[student]["name"])
#     return names
#
# print(adult(students))

# numbers = [10, 15, 20, 8, 12, 30]
#
# def sum_until_limit(list,limit):
#     sum=0
#
#     for number in list:
#         sum+=number
#         if sum>limit:
#             break
#     return sum
#
#
# print(sum_until_limit(numbers,65))

# restaurants = {
#     "Bella Italia": {
#         "ratings": [5, 4, 5, 4]
#     },
#     "Sushi House": {
#         "ratings": [4, 3, 5, 4]
#     },
#     "Burger King": {
#         "ratings": [3, 4, 3, 5]
#     }
# }
#
# def average_restaurant(restaurants):
#     result={}
#
#     for restaurant in restaurants:
#         grades=restaurants[restaurant]["ratings"]
#         sum_of_grades = 0
#
#         for grade in grades:
#             sum_of_grades+=grade
#             average_grade=sum_of_grades/len(grades)
#             result[restaurant]=average_grade
#     return result
#
# print(average_restaurant(restaurants))


# sentences = [
#     "Python is easy to learn.",
#     "Today is a beautiful day.",
#     "I enjoy learning programming.",
#     "This is short.",
#     "Practice helps us become better programmers."
# ]
#
# def long_sentences(list,n):
#     result=[]
#
#     for sentence in list:
#         if len(sentence)>n:
#             result.append(sentence)
#     return result
#
# print(long_sentences(sentences,14))


# courses = {
#     "Python": {
#         "participants": ["Ana", "Marko", "Jovan", "Mila"]
#     },
#     "Java": {
#         "participants": ["Nikola", "Sara"]
#     },
#     "SQL": {
#         "participants": ["Luka", "Teodora", "Ivan", "Petar", "Marija"]
#     }
# }
#
# def course_capacity(courses,threshold):
#     result=[]
#     for course in courses:
#         participants=courses[course]["participants"]
#         if len(participants)>threshold:
#             result.append(course)
#     return result
# print(course_capacity(courses,2))

# students = [
#     {
#         "name": "Anna",
#         "age": 17,
#         "grades": [5, 4, 5]
#     },
#     {
#         "name": "Mark",
#         "age": 19,
#         "grades": [4, 3, 5]
#     },
#     {
#         "name": "John",
#         "age": 18,
#         "grades": [5, 5, 4]
#     },
#     {
#         "name": "Mia",
#         "age": 16,
#         "grades": [3, 4, 4]
#     }
# ]
#
# def average_adult(list_of_students):
#     result={}
#     for student in list_of_students:
#         age=student["age"]
#         if age >=18:
#             name=student["name"]
#             grades=student["grades"]
#             sum_of_grades=0
#
#             for grade in grades:
#                 sum_of_grades+=grade
#                 average_grade=sum_of_grades/len(grades)
#                 result[name]=average_grade
#     return result
#
# print(average_adult(students))



