#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

print(from_json_string("[1, 2, 3]"))
print(type(from_json_string("[1, 2, 3]")))

json_dict = '{"id": 12, "name": "John", "is_active": true}'
print(from_json_string(json_dict))
print(type(from_json_string(json_dict)))
