import json


def write_to_file(content, file_path):
    with open(file_path, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def read_from_file(file_path):
    with open(file_path, encoding='utf-8') as file_obj:
        content = file_obj.read()

    return content


def add_to_file(content, file_path):
    with open(file_path, 'a+', encoding='UTF-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
