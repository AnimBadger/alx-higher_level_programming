#!/usr/bin/python3
def uniq_add(my_list=[]):
    sums = 0
    seen = []
    for i in range(len(my_list)):
        if my_list[i] in seen:
            continue
        else:
            sums += my_list[i]
            seen.append(my_list[i])
    return sums