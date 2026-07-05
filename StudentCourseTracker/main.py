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


for student in students:
    name=student["name"]
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

    if average_grade>=6:
        print(f"{name} - average: {average_grade} - passed")





