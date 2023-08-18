#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is not None or not a_dictionary:
        return None
    return max(k for k in a_dictionary.keys())
