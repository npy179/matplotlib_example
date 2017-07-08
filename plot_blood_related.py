#!/usr/bin/python
from __future__ import print_function
import re
from collections import OrderedDict
import numpy as np

def main():

    with open("Zhou_Labels_Row") as fin:
        label_list = [line.strip() for line in fin.readlines()]



    cell_types = ["HUVEC","AoAF", "AoSMC", "HAoAF", "HAoEC", "HBMEC",
                  "HBVP", "HBVSMC", "HMVEC","HPAEC", "HPAF","HSaVEC",
                  "HSaVEC","HCF","HCFaa","HCM","Heart",]


    related_list = []

    with open("Zhou_Labels_Row") as fin:
        for cell in cell_types:
            for line in fin.readlines():
                pattern = re.compile(cell, re.IGNORECASE)
                if pattern.search(line):
                    related_list.append(line.strip())

    #rest_label = list(set(label_list) - set(related_list))
    rest_label = [item for item in label_list if item not in related_list]
    sorted_cell_list = related_list + rest_label
    print(len(sorted_cell_list))

    label_index_dict = OrderedDict()
    for i, item in enumerate(sorted_cell_list):
        label_index_dict[item] = i
        print(i, " ", item)

    sorted_index = []

    for label in label_list:
        sorted_index.append(label_index_dict[label])


    H_C_diff = np.load("H_C_predict_diff.npy")
    H_C_diff_sort = H_C_diff[:, sorted_index]

    np.save("H_C_predict_diff_sorted", H_C_diff_sort)






if __name__=="__main__":
    main()
