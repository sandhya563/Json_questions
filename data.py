import json
dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
with open("data1.json","w") as a:
    json.dump(dict1,a,indent=3)
    print(type(dict1))
    print(dict1["emp2"])

# with open("data.json","r") as a:
#     kumar=json.load(a)
#     print(type(kumar))
#     print(kumar)

#a={"name":"kumar"}
# b=json.dumps(dict1)
# print(type(b))
# print(dict1)
# print(b)