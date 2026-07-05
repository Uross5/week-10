shop={
    "Maxi":{
        "Bread":100,
        "Newspaper":50
    },
    "Idea":{
        "Bread":95,
        "Newspaper":62
    },
    "Tempo":{
        "Bread":93,
        "Newspaper":70
    },
    "Roda":{
        "Newspaper":70
    }
}
#Print the store which has the higest price of bread
max_price=0

for i in shop:
    if "Bread" in shop[i]:
        if max_price<shop[i]["Bread"]:
            max_price=shop[i]["Bread"]
            print([i])



print(max_price)