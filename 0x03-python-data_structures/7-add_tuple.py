#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """concartinate 2 tuple elements (0 0) to the given tuples"""
    first_tup = tuple_a + (0, 0)  tuple_a(0, 0)
    sec_tup = tuple_b + (0, 0)
    """get the index sum of both tuples"""
    added_tuples = first_tup[0] + sec_tup[0], first_tup[1] + sec_tup[1]
    return added_tuples
