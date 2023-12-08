#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """Recursively finds a peak in a list of unsorted ints."""
    if not list_of_integers:
        return None
    theList = list_of_integers

    if len(theList) == 1:
        return theList[0]
    elif len(theList) == 2:
        return max(theList)

    mid = len(theList) // 2

    if theList[mid] > theList[mid + 1] and theList[mid] > theList[mid - 1]:
        return theList[mid]
    elif theList[mid] < theList[mid - 1]:
        return find_peak(theList[:mid])
    elif theList[mid] == theList[mid - 1]:  # case of equality in both sides
        left_peak = find_peak(theList[:mid])
        right_peak = find_peak(theList[mid:])
        return max(left_peak, right_peak)
    else:
        return find_peak(theList[mid:])
