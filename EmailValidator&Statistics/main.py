import re

users=[
    {
        "name":"Marko",
        "email":"marko@example.com",
        "stats":{}
    },
    {
        "name":"Ana",
        "email":"ana@example",
        "stats":{}
    },
    {
        "name":"Petar",
        "email":"petar123@gmail.com",
        "stats":{}

    },

]


def validate_email(email):
    pattern=r"^[\w+\-\.]+@[\w+\-]+\.\w{2,}$"
    match=re.search(pattern,email)
    if match:
        return True
    else:return False

def calculate_stats(users):
    stats = {
        "valid": 0,
        "invalid": 0,
        "domains": {}
    }
    for user in users:
        email = user["email"]
        if validate_email(email):
            stats["valid"]+=1
            domain=email.split("@")[1]
            if domain in stats["domains"]:
                stats["domains"][domain]+=1
            else:
                stats["domains"][domain]=1
        else:
            stats["invalid"]+=1
    return stats

#print(calculate_stats(users))

def list_valid_users(users):
    for user in users:
        email=user["email"]
        if validate_email(email):
            print(user["name"]," - ",email)

def list_invalid_users(users):
    for user in users:
        email=user["email"]
        if not validate_email(email):
            print(user["name"],' - ',email)

def adding_new_users(users,name,email):
    for user in users:
        user_email=user["email"]
        if user_email==email:
            print("User already exists")
            return False

    new_user={
        "name":name,
        "email":email,
        "stats":{}
    }
    users.append(new_user)
    return True

def users_by_domain(users):
    domains = {}
    for user in users:
        user_email=user["email"]
        if validate_email(user_email):
            domain=user_email.split("@")[1]
            if domain in domains:
                domains[domain].append(user["name"])
            else:
                domains[domain]=[user["name"]]
    return domains

def check_email_length(users):
    for user in users:
        email=user['email']
        if len(email)>=6 and len(email)<=254 and validate_email(email):
           user["stats"]["valid_length"]=True
        else:
           user["stats"]["valid_length"]=False
    return users

def fix_email(users):
    for user in users:
        email=user["email"]
        fixed_email = email.replace(" ", "").replace(",com", ".com")
        user["email"]=fixed_email
    return users


#stats=calculate_stats(users)
#print("\u2022Valid emails",stats["valid"])
#print("\u2022Invalid emails",stats["invalid"])
#print("\u2022Users per domain:")
#for domain in stats["domains"]:
 #   print("\u2022 ",domain,":",stats["domains"][domain])
#print(adding_new_users(users, "Jovan", "jovan@example.com"))
#print(adding_new_users(users, "Jovan", "jovan@example.com"))
#print(users_by_domain(users))
#check_email_length(users)
#print(users)








