#checking if it is email
import re

email="toma@gmail.com"

email_pattern=r"^[\w\.]+@[\w\.]+\.\w{2,}$"

if re.match(email_pattern,email):
    print("Bingo")