#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

save_to_json_file([1, 2, 3], "list.json")
save_to_json_file({"id": 1, "name": "Holberton"}, "dict.json")

print(open("list.json").read())
print(open("dict.json").read())
