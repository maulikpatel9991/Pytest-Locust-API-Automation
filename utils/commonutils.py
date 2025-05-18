import json


def write_json_data(file_name, data):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def write_json_data_append(file_name, data):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file)


def read_json_data(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def read_json_data_env(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data