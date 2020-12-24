import json
data={"name": "David",
    "class":"I",
    "age":6}
stor=json.dumps(data)
print(type(data))
print(type(stor))
print(stor)