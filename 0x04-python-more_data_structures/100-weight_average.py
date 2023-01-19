#!/usr/bin/python3
def weight_average(my_list=[]):
    return sum(i[0] * i[1] for i in my_list)/sum(i[1] for i in my_list) if my_list else 0
