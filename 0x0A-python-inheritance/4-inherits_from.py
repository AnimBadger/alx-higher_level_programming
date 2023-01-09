#!/usr/bin/python3
'''only subclass of'''


def inherits_from(obj, a_class):
    '''returns True is object is instance of class that is
    inherited (directly or indirectly)
    from specific class, False if otherwise
    '''
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
