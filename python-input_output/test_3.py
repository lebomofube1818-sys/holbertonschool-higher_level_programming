#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
print(to_json_string(my_list))
print(type(to_json_string(my_list)))

my_dict = {
    'id': 12,
    'name': "John",
    'places': ["San Francisco", "Tokyo"],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
print(to_json_string(my_dict))
print(type(to_json_string(my_dict)))

try:
    print(to_json_string({1, 2, 3}))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
