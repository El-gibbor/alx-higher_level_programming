#!/usr/bin/python3

def search_replace(my_list, search, replace):
    replaced = [replace if i == search else i for i in my_list]
    return replaced

# ====== a respect to Guido van Rossum =====
# def search_replace(my_list, search, replace):
#     replaced = []
#     for i in my_list:
#         if i == search:
#             i = replace
#         replaced.append(i)
#     return replaced
