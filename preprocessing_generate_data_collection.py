import os
from nltk.tokenize import word_tokenize
import pickle


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


def save_var(path, var):
    with open(path, "wb") as file_obj:
        pickle.dump(var, file_obj)


def load_var(path):
    with open(path, "rb") as file_obj:
        var = pickle.load(file_obj)

    return var


if __name__ == '__main__':
    project = "AspectJ"
    path_data = "./../CollectData/datasets/" + project + "/codes"
    path_label = "./../CollectData/datasets/" + project + "/" + project + "_ids_labels.txt"

    ids, labels = collect_ids_labels(path_label)
#    descriptions, codes = get_raw_data(ids, path_data)
#    descriptions, codes = tokenize(descriptions, codes)
    
    descriptions_path = "./vars/" + project + "_descriptions.pkl"
    codes_path = "./vars/" + project + "_codes.pkl"
    ids_path = "./vars/" + project + "_ids.pkl"
    labels_path = "./vars/" + project + "_lables.pkl"


#    save_var(descriptions_path, descriptions)
#    save_var(codes_path, codes)
#    save_var(ids_path, ids)
#    save_var(labels_path, labels)

#    descriptions, codes = load_var(descriptions_path), load_var(codes_path)
#    print(descriptions[0])
#    print("\n\n")
#    print(codes[0])

#    print(labels)
#    for i, l in zip(ids, labels):
#        print(i + " " + l)
