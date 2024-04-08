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
        dat = json.load(data_file)
    for key in dat.keys():
        if field == key:
            sequential_data = dat[field]
            return sequential_data
        else:
            return None



def linear_search(prohledavana_sekvence, hledane_cislo):
    #klic positions = seznam pozic
    pozice = []
    pocet_vyskytu = 0
    #for index in range(len(prohledavana_sekvence)):
    #    if hledane_cislo == prohledavana_sekvence[index]:
    #        pozice.append(index)
    #        pocet_vyskytu = pocet_vyskytu + 1
    #return {"positions": pozice, "count": pocet_vyskytu}
    for i, num in enumerate(prohledavana_sekvence):
        if num == hledane_cislo:
            pozice.append(i)
            pocet_vyskytu += 1
    return {"positions": pozice, "count": pocet_vyskytu}


def pattern_search(prohledavana_sekvence, hledany_vzor):
    pozice = set()
    delka_vzoru = len(hledany_vzor)
    delka_sekvence = len(prohledavana_sekvence)
    for i in range(delka_sekvence - delka_vzoru + 1):
        if prohledavana_sekvence[i:delka_vzoru + i] == hledany_vzor:
            pozice.add((i + delka_vzoru)/2)
    return pozice



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print("Sequential Data:", sequential_data)
    with open("sequential.json", "r") as data_file:
        dat = json.load(data_file)
    overeni = pattern_search(dat["dna_sequence", "ATA"])

if __name__ == '__main__':
    main()