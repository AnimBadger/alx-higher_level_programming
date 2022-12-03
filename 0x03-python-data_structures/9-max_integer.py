#!/usr/bin/python3
def max_integer(my_list=[]):
    leng = len(my_list)
    if (leng == 0):
        return None
    maximum = my_list[0]
    counter = 1
    for counter in range(leng):
        if (my_list[counter] > maximum):
            maximum = my_list[counter]
    return (maximum)
