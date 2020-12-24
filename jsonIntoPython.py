import json
data='{"name":"ram","class":"IV","age":"9" }'
process= json.loads(data)
print(type(data))
print(type(process))
print(process) 

