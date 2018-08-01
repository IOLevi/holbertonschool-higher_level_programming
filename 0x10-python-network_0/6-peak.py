#!/usr/bin/python3 
'finds a peak in a list of unsorted ints'

def find_peak(list_of_integers):
    'find peak'
    """
    go to mid point ()
    check if it is peak
    if yes, return
    if not, go t 
    """
    try:
        a = max(list_of_integers)
        return a
    except:
        return None