#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    listed = list(a_dictionary.keys())
    for i in listed:
        new_dic[i] *= 2
    return new_dic
    