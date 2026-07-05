#ask the user for their age
#if the user does not enter anything, ask agian

age=" "

while not age.isdigit() or int(age)<18:
    age=input("What's your age? ")

print(age)

