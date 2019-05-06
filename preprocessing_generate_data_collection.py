import os


def collect_ids_labels(path_label):
    ids = []
    labels = []
    with open(path_label, "r") as file_obj:
        for line in file_obj:
            ids.append(line.strip().split("\t")[0])
            labels.append(line.strip().split("\t")[1])
    return ids, labels






if __name__ == '__main__':
    project = "AspectJ"
    path_data = "./../CollectData/datasets/" + project + "/codes"
    path_label = "./../CollectData/datasets/" + project + "/" + project + "_ids_labels.txt"

    ids, labels = collect_ids_labels(path_label)
    print(labels)
#    for i, l in zip(ids, labels):
#        print(i + " " + l)
