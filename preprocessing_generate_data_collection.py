import os
from nltk.tokenize import word_tokenize


def collect_ids_labels(path_label):
    ids = []
    labels = []
    with open(path_label, "r") as file_obj:
        for line in file_obj:
            ids.append(line.strip().split("\t")[0])
            labels.append(line.strip().split("\t")[1])
    return ids, labels


def get_raw_data(ids, path_data):
    descriptions = []
    codes = []
    for i in ids:
        description = ""
        code = ""
        with open(os.path.join(path_data, i + ".description"), "r", errors="ignore") as file_obj:
            for line in file_obj:
                description = description + line.strip() + " "
        description = description.strip()
        descriptions.append(description)
        
        with open(os.path.join(path_data, i + ".java"), "r", errors="ignore") as file_obj:
            for line in file_obj:
                code = code + line.strip() + " "
        code = code.strip()
        codes.append(code)

    return descriptions, codes


def tokenize(raw_descriptions, raw_codes):
    descriptions = []
    codes = []

    for description in raw_descriptions:
        descriptions.append(" ".join(word_tokenize(description)))

    for code in raw_codes:
        codes.append(" ".join(word_tokenize(code)))

    return descriptions, codes


if __name__ == '__main__':
    project = "AspectJ"
    path_data = "./../CollectData/datasets/" + project + "/codes"
    path_label = "./../CollectData/datasets/" + project + "/" + project + "_ids_labels.txt"

    ids, labels = collect_ids_labels(path_label)
    descriptions, codes = get_raw_data(ids, path_data)
    descriptions, codes = tokenize(descriptions, codes)

#    print(labels)
#    for i, l in zip(ids, labels):
#        print(i + " " + l)
