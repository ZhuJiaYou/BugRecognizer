from preprocessing_generate_data_collection import load_var, save_var
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit


def convert_label(labels):
    new_labels = []
    for l in labels:
        if l == "False":
            new_labels.append(0)
        elif l == "True":
            new_labels.append(1)

    return np.array(new_labels)


def data_info(ids, labels, descriptions, codes):
    print("Descriptions num:{}".format(len(descriptions)))
    print("codes num: {}".format(len(codes)))
    print("labels num: {}".format(len(labels)))
    print("ids num: {}".format(len(ids)))

    pos = [l for l in labels if l == 1]
    neg = [l for l in labels if l == 0]

    print("Positive labels: {0} ==== Negative labels: {1}".format(len(pos), len(neg)))


def split_data_with_fold(descriptions, codes, labels, ids, folds_num):
    sss = StratifiedShuffleSplit(n_splits = folds_num, random_state=None)
    for train_index, test_index in sss.split(descriptions, labels):
        descriptions_train = [descriptions[i] for i in train_index]
        descriptions_test = [descriptions[i] for i in test_index]
        codes_train = [codes[i] for i in train_index]
        codes_test = [codes[i] for i in test_index]
        labels_train = labels[train_index]
        labels_test = labels[test_index]
        ids_train = [ids[i] for i in train_index]
        ids_test = [ids[i] for i in test_index]
        
        train = (ids_train, labels_train, descriptions_train, codes_train)
        test = (ids_test, labels_test, descriptions_test, codes_test)

        return train, test
        

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
    data_info(ids, labels, descriptions, codes)

    train, test = split_data_with_fold(descriptions, codes, labels, ids, 5)
    ids_train, labels_train, msg_train, code_train = train
    ids_test, labels_test, msg_test, code_test = test
    print(type(labels_train))

#    print(ids_train[0])
#    print(labels_train[0])
#    print(msg_train[0])
    print(code_train[1])
#    print(ids_test[0])
#    print(labels_test[0])
#    print(msg_test[0])
#    print(code_test[0])

#    print(descriptions[0])
#    print("\n\n")
#    print(codes[0])

#    print(labels)
#    for i, l in zip(ids, labels):
#        print(i + " " + l)
