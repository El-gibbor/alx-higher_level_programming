#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(key for key in a_dictionary.keys())
