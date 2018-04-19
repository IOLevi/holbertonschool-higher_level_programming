#!/usr/bin/python3
def best_score(a_dictionary):
    a = []
    winner = None
    if type(a_dictionary) is not dict:
        return None
    for k, v in a_dictionary.items():
        a.append(v)
        if max(a) == v:
            winner = k

    return winner
