import re


our_numbers="12345"

pattern=r"^\d+$"

if re.match(pattern, our_numbers):
    print("Only numbers")
else:
    print("Not only numbers")

sentence="I love python"

pattern1=r"^[a-zA-Z\s]+$"

if re.match(pattern1,sentence):
    print("Only letters")
else:
    print("Not only letters")

important_sentence="Today will rain"

big_letter_pattern=r"^[A-Z]"

if (big_letter_pattern,important_sentence):
    print("Capital letter")

phone_number="382555333"

phone_pattern=r"^38(1|2|5|9)"

phone_match=re.match(phone_pattern,phone_number)

phone_map={
    "381": "Serbia",
    "382":"Montenegro",
    "385":"Bosnia",
    "389":"Croatia"
}

if phone_match:
    prefix="38"+phone_match.group(1)
    print(f"Starting number is {prefix} and country is {phone_map[prefix]}")

