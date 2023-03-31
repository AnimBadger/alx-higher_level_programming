#!/usr/bin/python3
'''
    function that finds the peak of an unsorted list
'''


def find_peak(list_of_integers):
    '''find peak of list of integers'''
    if list_of_integers is None or list_of_integers == []:
        return None
    low = 0
    high = len(list_of_integers)
    mid = int(len(list_of_integers) // 2)

    if high == 1:
        return list_of_integers[0]
    if high == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
