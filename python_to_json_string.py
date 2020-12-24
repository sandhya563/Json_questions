import json

# a Python object (dict):
data = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
string= json.dumps(data)
# the result is a JSON string:
print(string)
