
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

# Make a loop which will print all prices of bread from every store
total_bread=0
total_bread_shop=0
most_expensive_bread=0

for i in shop:
    if "Bread" in shop[i]:
        total_bread+=shop[i]["Bread"]
        total_bread_shop+=1
        
average_bread_price=total_bread/total_bread_shop

print(average_bread_price)