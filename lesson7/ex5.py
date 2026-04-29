import json
import csv

with open ("employees.json", "r", ) as f:
    data = json.load(f)
    print(data)
    #print(data[0]['name'])    
    #print(type(data[0]))
    #print((data[0]))
    #x = data [0]
    #print(x['languages'])
    #print(type(x))
    #print(x["name"])
    #print(z)
    #print(len(x))
    #print(len(data))
with open ("emp.csv", "w") as c:
    file_write = csv.writer(c, delimiter=",")
    file_write.writerow(["name","birthday","height","weight","car","languages"])
    i = 0
    while i < len(data):
        name = data[i]["name"]
        birthday = data[i]["birthday"]
        height = data[i]["height"]
        weight = data[i]["weight"]
        car = data[i]["car"]
        languages = data[i]["languages"]
        i += 1
        file_write.writerow([name,birthday,height,weight,car,languages]) 