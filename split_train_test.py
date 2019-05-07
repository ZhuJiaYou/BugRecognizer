from preprocessing_generate_data_collection import load_var, save_var
import numpy as np


def convert_label(labels):
    return np.array([0 if d == "False" else 1 for d in labels])







if __name__ == '__main__':
    project = "AspectJ"
    path_data = "./../CollectData/datasets/" + project + "/codes"
    path_label = "./../CollectData/datasets/" + project + "/" + project + "_ids_labels.txt"

    descriptions_path = "./vars/" + project + "_descriptions.pkl"
    codes_path = "./vars/" + project + "_codes.pkl"
    ids_path = "./vars/" + project + "_ids.pkl"
    labels_path = "./vars/" + project + "_lables.pkl"

#    save_var(labels_path, labels)
    descriptions, codes = load_var(descriptions_path), load_var(codes_path)
    ids, labels = load_var(ids_path), load_var(labels_path)

    labels = convert_label(labels)
    print(labels)


#    print(descriptions[0])
#    print("\n\n")
#    print(codes[0])

#    print(labels)
#    for i, l in zip(ids, labels):
#        print(i + " " + l)
