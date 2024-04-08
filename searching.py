import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open("sequential.json", "r") as data_file:
        dat = json.load(data_file)["allowed_keys"]

    if field not in dat:
        return None

    with open(file_name, "r") as file:
        data = json.load(file)

    return data.get(field, None)





def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print("Sequential Data:", sequential_data)


if __name__ == '__main__':
    main()