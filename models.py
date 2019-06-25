import torch.nn as nn
import torch
import torch.nn.functional as F


class BugNet(nn.Module):
    def __init__(self, args):
        super(BugNet, self).__init__()
        self.args = args

        descriptions_dict_len = args.descriptions_dict_len
        codes_dict_len = args.codes_dict_len

        embedding_len = args.embedding_len
        class_num = args.class_num

        in_channels = 1
        out_channals = args.num_filters
        conv_heights = args.sizes_filters

        # CNN-2D for descriptions
        self.embed_descriptions = nn.Embedding(descriptions_dict_len, embedding_len)
        self.descriptions_conv = nn.ModuleList([
            nn.Conv2d(in_channels, out_channals, (h, embedding_len)) for h in conv_heights])

        # CNN-2D for codes
        self.embed_codes = nn.Embedding(codes_dict_len, embedding_len)
        self.codes_conv = nn.ModuleList([
            nn.Conv2d(in_channels, out_channals, (h, embedding_len)) for h in conv_heights])

        # Other info
        self.dropout = nn.Dropout(args.dropout_keep_prob)
        self.fc1 = nn.Linear(2 * len(conv_heights) * out_channals, args.hidden_units)
        self.fc2 = nn.Linear(args.hidden_units, class_num)
        self.sigmoid = nn.Sigmoid()

    def forward_descriptions(self, x, convs):
        x = x.unsqueeze(1)
        x = [F.relu(conv(x)).squeeze(3) for conv in convs]


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
