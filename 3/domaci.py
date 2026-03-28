tajni_pin=5067

#ako je tajni pin 4321 ili ako je 3124 ipisiati poruku 'Pin je tacan'
# u suprotnom ispisati poruku 'PIN JE NETACAN'
#Zabranjeno koriscenje elif i vise od 1 IF-a

if tajni_pin==4321 or tajni_pin==3124:
    print("PIN JE TACAN")
else:
    print("PIN JE NETACAN")