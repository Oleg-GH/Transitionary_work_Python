import json


def read_file(file):
    with open(file, 'r', encoding='UTF-8') as f:
        return json.load(f)


def write_file(data, file):
    with open(file, 'w', encoding='UTF-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def create_file(data, file):
    with open(file, 'w', encoding='UTF-8') as f:
        json.dump([data, ], f, indent=4, ensure_ascii=False)


def get_id(file):
    try:
        content = read_file(file)
        return max(note['id'] for note in content)
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0