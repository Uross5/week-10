import re

#must be 3 letters follow by 3 numbers
bonus_codes="ABC123, bonus455, bonus22,xvc111"
pattern=r"\b[A-Za-z]{3}\d{3}\b"

product_codes=re.findall(pattern,bonus_codes)
print(product_codes)

username="toma1993"

username_pattern=r"[A-Za-z]{1,5}\d{2,}"
match=re.match(username_pattern,username)
if match:
    print(match.group())