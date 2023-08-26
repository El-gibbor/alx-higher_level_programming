#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    score, weight = 0, 0
    score = sum(i * j for i, j in my_list)
    weight = sum(j for _, j in my_list)

    return score / weight
