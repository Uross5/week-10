cars=["Audi","BMW","Zastava"]
print(cars)

#BMW->Mercedes
cars[1]="Mercedes"
print(cars)

#dodati skodu
cars.append("Skoda")
print(cars)
cars.sort()
print(cars)

#Trenutno na stanju imamo x automobila

cars_number=len(cars)
#print(cars_number)
print(f"Trenutno na stanju imamo {cars_number} autobomila")