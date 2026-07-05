students=[
    {
        "name":"John",
        "courses":{
            "Python":9,
            "Math":8,
            "Algorithm":10
        }
    },
    {
        "name":"Ana",
        "courses":{
            "Python":6,
            "Math":7,
            "Algorithm":5
        }
    },
    {
        "name":"Ashley",
        "courses":{
            "Python":10,
            "Math":9,
            "Algorithm":8
        }
    }

]
max_grade=1
min_grade=10
max_name=[]
min_name=[]
sort_results=[]
percent_of_successes=0
passed_count=0
total_students=len(students)

for student in students:
    name=student["name"]
    if name=="John":
        student["courses"]["English"]=7
    elif name=="Ana":
        student["courses"]["English"]=8
    elif name=="Ashley":
        student["courses"]["English"]=10
    #print(name)
    course=student["courses"]
    #print(course)
    sum_of_grades=0
    number_of_courses=len(student["courses"])
    #print(number_of_courses)

    for subject in course:
        grade=(course[subject])
        sum_of_grades+=grade

    #print(sum_of_grades)
    average_grade=sum_of_grades/number_of_courses
    #print(average_grade)
    sort_results.append((name,average_grade))

    if average_grade>=6:
       #print(f"{name} - average: {average_grade} - passed")
       passed_count += 1

    if average_grade>max_grade:
        max_grade=average_grade
        max_name=[name]
    elif average_grade==max_grade:
        max_name.append(name)

    if average_grade<min_grade:
        min_grade=average_grade
        min_name=[name]

sort_results.sort(key=lambda x: x[1], reverse=True)

for name, average_grade in sort_results:
    print(f"{name} - average: {average_grade} - passed")
    

percentage=(passed_count/total_students)*100
print(f"percentage of students who passed is: {percentage:.2f}%")

#print(f"student with the highest average grade is {max_name}")
#print(f"student with the lowest average grade is {min_name}")
#print(sort_results)