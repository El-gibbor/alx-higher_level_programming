#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length=0):
    list_div = []
    for i in range(list_length):
        try:
            list_div.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print('division by 0')
            list_div.append(0)
        except TypeError:
            print('wrong type')
            list_div.append(0)
        except IndexError:
            print('out of range')
        finally:
            pass
    return list_div
