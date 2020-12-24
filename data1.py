import json
b='{"Name":"Ram","Class":"IV","Age":"9" }'
a=json.loads(b)
print(type(b))
print(type(a))
print(a["Name"])
print(a["Age"])