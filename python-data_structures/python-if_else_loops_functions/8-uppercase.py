#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    result = ""
    for ch in str:
        code = ord(ch)
        if 97 <= code <= 122:  # 'a'..'z'
            result += chr(code - 32)
        else:
            result += ch
    print("{}".format(result))
