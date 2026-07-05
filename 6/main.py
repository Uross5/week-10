#Make a list of students
#Each student has: name,score(0-100), active:true/false

students=[
    {"name": "John",
     "score": 92,
     "active": True},

    {"name": "Eric",
     "score": 88,
     "active": False},

    {"name": "Breon",
     "score": 55,
     "active": True}]

#Make a loop which print only students who are active
#If a student score is (this is only for active students)
#from 80-100 -> "grade":"A"
#from 60-80 -> "grade":"B"
#from 40-60 -> "grade":"C"
#from 20-40 -> "grade":"D"
#from < 20 -> "grade":"F"

for i in students:
    if i['active']==True:
        if i['score']>=80 and i['score']<=100:
            i['grade']="A"
        elif i['score']>=60 and i['score'] < 80:
            i['grade']="B"
        elif i['score']>=40 and i['score'] < 60:
            i['grade']="C"
        elif i['score']>=20 and i['score'] < 40:
            i['grade']="D"
        elif i['score']<20:
            i['score']="F"






print(students)
