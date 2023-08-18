#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(k for k in a_dictionary.keys())
