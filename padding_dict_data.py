from preprocessing_generate_data_collection import load_var, save_var
import numpy as np


def make_dict(data):
    data_list = ["<NULL>"]
    for d in data:
        data_list += d.split()

    data_dict = dict()
    i = 0
    for word in data_list:
        if word not in data_dict:
            data_dict[word] = i
            i += 1

    return data_dict


def mapping_dict(data, data_dict):
    mapping_list = []
    for line in data:
        new_line = []
        for word in line.split(" "):
            if word in data_dict:
                new_line.append(data_dict[word])
            else:
                new_line.append(data_dict["<NULL>"])
        mapping_list.append(new_line)

    return np.array([np.array(line) for line in mapping_list])


def padding_data(data, max_length):
    new_data = []
    for d in data:
        line_len = len(d.split(" "))
        if d.strip() == "":
            d = (d + " <NULL>" * max_length).strip()
        elif line_len < max_length:
            d = (d + " <NULL>" * (max_length - line_len)).strip()
        elif line_len > max_length:
            d = " ".join(d.split(" ")[:max_length])
        new_data.append(d)
    
    return new_data


if __name__ == '__main__':
    project = "AspectJ"
    path_data = "./../CollectData/datasets/" + project + "/codes"
    path_label = "./../CollectData/datasets/" + project + "/" + project + "_ids_labels.txt"

#    descriptions, codes = get_raw_data(ids, path_data)
#    descriptions, codes = tokenize(descriptions, codes)
    
    descriptions_path = "./vars/" + project + "_descriptions.pkl"
    codes_path = "./vars/" + project + "_codes.pkl"
    ids_path = "./vars/" + project + "_ids.pkl"
    labels_path = "./vars/" + project + "_lables.pkl"
    dict_codes_path = "./vars/" + project + "_dict_code.pkl"
    dict_descriptions_path = "./vars/" + project + "_dict_description.pkl"

    
#    save_var(descriptions_path, descriptions)
#    save_var(codes_path, codes)
#    save_var(ids_path, ids)
#    save_var(labels_path, labels)

    descriptions, codes = load_var(descriptions_path), load_var(codes_path)
    dict_descriptions = make_dict(descriptions)
    dict_codes = make_dict(codes)
    print(len(dict_codes))
    print(len(dict_descriptions))
    pad_codes = padding_data(codes, 500)
#    print(len(pad_codes[0]))
#    print(pad_descriptions)
    k = mapping_dict(pad_codes, dict_codes)
    print(k.shape)
#    save_var(dict_descriptions_path, dict_descriptions)
#    save_var(dict_codes_path, dict_codes)

#    print(descriptions[0])
#    print("\n\n")
#    print(codes[0])

#    print(labels)
#    for i, l in zip(ids, labels):
#        print(i + " " + l)
