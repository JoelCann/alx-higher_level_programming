#!/usr/bin/python3
def best_score(the_dict):
    if the_dict and len(the_dict):
        max = list(the_dict.keys())[0]
        for key in the_dict:
            if the_dict[key] > the_dict[max]:
                max = key
        return max
    return None
