#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if (leng == 0):
        new_tuple = (leng, None)
    else:
        new_tuple = (leng, sentence[0])
    return (new_tuple)
