#!/usr/bin/python3

def uniq_add(my_list=[]):
    return (sum(set(my_list)))  # set returns unique items only

# ===== for julien & bernard =====
    # uniq, add_uniq = [], 0
    # for i in my_list:
    #     if i not in uniq:
    #         uniq.append(i)
    # for j in uniq:
    #     add_uniq += j
    # return add_uniq
