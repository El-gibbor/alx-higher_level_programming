#!/usr/bin/python3

def search_replace(my_list, search, replace):
    replaced_list = []
    for i in my_list:
        if i == search:
            i = replace
        replaced_list.append(i)
    return replaced_list
