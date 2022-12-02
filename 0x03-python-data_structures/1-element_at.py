#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    for i in range(len(my_list)):
        if (i == idx):
            return (my_list[i])
        elif (i > len(my_list)):
            return (None)