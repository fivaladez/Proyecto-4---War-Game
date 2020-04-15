"""Archivo para extraer datos de muestra para el proyecto 4"""
import os
import re


def extract_data(file):
    results = list()
    if os.path.exists(file):
        with open(file) as fd:
            data_file = fd.read()

        # Looking for nn...n - 500
        regex_1 = r"(?P<n_regex>^\d+\D*)\n"
        match_1 = re.search(regex_1, data_file)
        if match_1:
            results.append(match_1.group("n_regex"))
        else:
            print("Regex not found: {}".format(match_1))

        # Looking for n nn...n nn...n - 3 224 190
        regex_2 = r"(?P<data>^\d{1}\s\d+\s\d+)"
        matches = re.finditer(regex_2, data_file, re.MULTILINE)
        if matches:
            for _, match in enumerate(matches, start=1):
                results.append(match.group("data"))
        else:
            print("Regex not found: {}".format(matches))

        results = "\n".join(results)
        # print(results)
        return results

    else:
        print("File not found")



if __name__ == "__main__":
    data = extract_data("datos_prueba_wargame/war_1000_recs_500_ppl.txt")
    print(data)
    with open("test_data.txt", "w") as fw:
        fw.write(data)
