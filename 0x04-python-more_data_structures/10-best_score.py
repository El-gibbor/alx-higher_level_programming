#!/usr/bin/python3

def best_score(a_dictionary):
    if not len(a_dictionary):
        return None
    return max(k for k in a_dictionary.keys())

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))