import json


def load_data(filepath):
    data = open(filepath, 'r').read()
    json_data = json.loads(''.join(data))
    return json_data


def pretty_print_json(data):
    return json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    path = input("введите имя файла с данными\n")
    data = load_data(path)
    print(pretty_print_json(data))