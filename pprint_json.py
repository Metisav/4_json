import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    return json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    path = input("введите имя файла с данными\n")
    json_data = load_data(path)
    print(pretty_print_json(json_data))