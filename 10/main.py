import json
from textwrap import indent

with open("data.json", "r") as file:
    data=json.load(file)
    data.append({
        "name":"Luke Thompson",
        "age":25,
        "height":170,
        "gender":"male"
    })

    with open("data.json","w") as file:
        json.dump(data,file,indent=4)