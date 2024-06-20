import json

def serialize_and_save_to_file(data, filename):
    with open(f"{filename}", "w") as write_file:
        json.dump(data, write_file)

def load_and_deserialize(filename):
    with open(f"{filename}", "r") as read_file:
        data = json.load(read_file)