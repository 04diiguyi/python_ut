import os

def _add(x, y):
    return x + y

def main(x, y):
    file_name = "dummyfile"

    if not os._exists(file_name):
        os.makedirs(file_name, exist_ok=True)

    result = _add(x, y)

    return result
    